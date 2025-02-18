#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 542402611043
#
Name     : libmikmod
Version  : 3.3.11.1
Release  : 1
URL      : https://downloads.sourceforge.net/project/mikmod/libmikmod/3.3.11.1/libmikmod-3.3.11.1.tar.gz
Source0  : https://downloads.sourceforge.net/project/mikmod/libmikmod/3.3.11.1/libmikmod-3.3.11.1.tar.gz
Summary  : sound library for module files
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1
Requires: libmikmod-bin = %{version}-%{release}
Requires: libmikmod-info = %{version}-%{release}
Requires: libmikmod-lib = %{version}-%{release}
Requires: libmikmod-license = %{version}-%{release}
Requires: libmikmod-man = %{version}-%{release}
BuildRequires : alsa-lib-dev
BuildRequires : buildreq-configure
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A portable sound library for Unix and other systems, capable of playing
samples as well as module files, on a wide range of sound devices.

%package bin
Summary: bin components for the libmikmod package.
Group: Binaries
Requires: libmikmod-license = %{version}-%{release}

%description bin
bin components for the libmikmod package.


%package dev
Summary: dev components for the libmikmod package.
Group: Development
Requires: libmikmod-lib = %{version}-%{release}
Requires: libmikmod-bin = %{version}-%{release}
Provides: libmikmod-devel = %{version}-%{release}
Requires: libmikmod = %{version}-%{release}

%description dev
dev components for the libmikmod package.


%package info
Summary: info components for the libmikmod package.
Group: Default

%description info
info components for the libmikmod package.


%package lib
Summary: lib components for the libmikmod package.
Group: Libraries
Requires: libmikmod-license = %{version}-%{release}

%description lib
lib components for the libmikmod package.


%package license
Summary: license components for the libmikmod package.
Group: Default

%description license
license components for the libmikmod package.


%package man
Summary: man components for the libmikmod package.
Group: Default

%description man
man components for the libmikmod package.


%prep
%setup -q -n libmikmod-3.3.11.1
cd %{_builddir}/libmikmod-3.3.11.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732038045
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1732038045
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libmikmod
cp %{_builddir}/libmikmod-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libmikmod/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/libmikmod-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libmikmod/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libmikmod-config

%files dev
%defattr(-,root,root,-)
/usr/include/mikmod.h
/usr/lib64/libmikmod.so
/usr/lib64/pkgconfig/libmikmod.pc
/usr/share/aclocal/*.m4

%files info
%defattr(0644,root,root,0755)
/usr/share/info/mikmod.info

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmikmod.so.3
/usr/lib64/libmikmod.so.3.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libmikmod/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libmikmod/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/libmikmod-config.1
