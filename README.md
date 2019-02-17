## inPack for PHP

* Needs CentOS 7.x x86_64 (https://www.centos.org/)

## Install dependent packages

``` shell
yum install libmcrypt libmcrypt-devel libwebp-devel libjpeg-devel libpng-devel freetype-devel libXpm-devel postgresql-devel bzip2-devel curl-devel libstdc++-devel openssl-devel sqlite-devel  zlib-devel smtpdaemon libedit-devel pcre-devel bzip2 perl libtool gcc-c++ libtool-ltdl-devel  libzip-devel krb5-devel postgresql-devel libxml2-devel libxslt-devel gd-devel libmcrypt-devel aspell-devel libicu-devel gmp-devel
```


## Install inPack Tool

``` shell
go install github.com/sysinner/inpack/cmd/inpack
inpack build
```

## Build

``` shell
# 7.1.x
inpack build --spec inpack-71.spec --version 7.1.0 --release 1

# 7.2.x
inpack build --spec inpack-72.spec --version 7.2.0 --release 1
```

