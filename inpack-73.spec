[project]
name = php73
version = 7.3.2
vendor = php.net
homepage = http://php.net
groups = dev/sys-runtime
description = fast, flexible, pragmatic and scripting language that is especially suited to web development

%build
PREFIX="/opt/php/php73"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "php-{{.project__version}}.tar.xz" ]; then
    wget http://php.net/distributions/php-{{.project__version}}.tar.xz
fi
if [ ! -d "php-{[.project__version}}" ]; then
    tar -pxf php-{{.project__version}}.tar.xz
fi

cd php-{{.project__version}}

./configure --prefix=$PREFIX \
  --with-config-file-path=$PREFIX/etc \
  --with-config-file-scan-dir=$PREFIX/etc/php.d \
  --disable-debug \
  --enable-static=yes \
  --with-pic \
  --disable-rpath \
  --without-pear \
  --enable-gd-native-ttf \
  --without-gdbm \
  --with-openssl \
  --with-zlib \
  --with-kerberos \
  --with-mhash \
  --enable-fpm \
  --enable-pcntl \
  --enable-opcache \
  --enable-opcache-file \
  --enable-mbstring=shared \
  --enable-mbregex \
  --with-gd=shared \
  --with-webp-dir \
  --with-jpeg-dir \
  --with-gmp=shared \
  --enable-bcmath=shared \
  --with-bz2=shared \
  --enable-ctype=shared \
  --enable-exif=shared \
  --enable-ftp=shared \
  --with-gettext=shared \
  --with-iconv=shared \
  --enable-sockets=shared \
  --enable-tokenizer=shared \
  --enable-exif=shared \
  --enable-ftp=shared \
  --with-xmlrpc=shared \
  --enable-simplexml=shared \
  --enable-xml=shared \
  --enable-wddx=shared \
  --enable-soap=shared \
  --with-xsl=shared \
  --enable-pdo=shared \
  --enable-mysqlnd=shared \
  --with-mysqli=shared,mysqlnd \
  --with-pdo-mysql=shared,mysqlnd \
  --with-pgsql=shared \
  --with-pdo-pgsql=shared \
  --with-sqlite3=shared \
  --with-pdo-sqlite=shared \
  --enable-json=shared \
  --enable-intl=shared \
  --with-curl=shared \
  --enable-zip=shared \
  --with-pspell=shared \
  --with-mcrypt=shared \
  --disable-phar

make -j8

INSTALL_ROOT=build_tmp make install-cli install-fpm install-modules
rm -rf build_tmp$PREFIX/php/man
find build_tmp$PREFIX/lib/php/extensions -type f -name "*.a"|xargs rm -f

rsync -av build_tmp$PREFIX/* {{.buildroot}}/

cd {{.inpack__pack_dir}}

mkdir -p {{.buildroot}}/etc/php.d
install misc/php73/php.ini.default {{.buildroot}}/etc/php.ini.default
install misc/php73/php-fpm.conf.default {{.buildroot}}/etc/php-fpm.conf.default
install misc/php73/php-fpm.d__www.conf.default {{.buildroot}}/etc/php-fpm.d/www.conf.default

find {{.buildroot}}/bin -type f|xargs strip -s
find {{.buildroot}}/sbin -type f|xargs strip -s
find {{.buildroot}}/lib/php/extensions -type f -name "*.so"|xargs strip -s

rm -rf {{.inpack__pack_dir}}/deps/php-{{.project__version}}

%files
