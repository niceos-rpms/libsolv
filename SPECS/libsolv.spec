%define __cmake_switch(b:) %[%{expand:%%{?with_%{-b*}}} ? "ON" : "OFF"]

Name:           libsolv
Version:        0.7.35
Release:        1%{?dist}
Summary:        libsolv - a library for resolving package dependencies
Summary(ru):    libsolv — библиотека для разрешения зависимостей пакетов

License:        BSD-3-Clause
URL:            https://github.com/openSUSE/libsolv
Source0:        https://github.com/openSUSE/libsolv/archive/refs/tags/%{version}.tar.gz#%{name}-%{version}.tar.gz

Packager:       NICE SOFT GROUP LLC (ООО "НАЙС СОФТ ГРУПП") 5024245440 <niceos@ncsgp.ru>
Vendor:         NiceSOFT
Distribution:   NiceOS.Core
BugURL:         https://bugs.niceos.ru/
VCS:            https://specs.niceos.ru/rmps/%{name}

Requires:       expat-libs
Requires:       rpm-libs >= 4.19.1.1
Requires:       zlib

BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  zlib-devel

Provides:       libsolv-tools = %{version}-%{release}
Provides:       python3-solv = %{version}-%{release}

%description
libsolv is a fast and efficient dependency solver library used by package
management tools to resolve package dependencies and handle repository data.
It is optimized for speed and memory usage and supports multiple repository
formats.

%description -l ru
libsolv — быстрая и эффективная библиотека для решения зависимостей, используемая
в системах управления пакетами для разрешения зависимостей и работы с данными
репозиториев. Она оптимизирована по скорости и потреблению памяти и поддерживает
несколько форматов репозиториев.

%package        devel
Summary:        Developer files for the libsolv library
Summary(ru):    Файлы разработки для библиотеки libsolv
Requires:       %{name} = %{version}-%{release}
Requires:       expat-devel
Provides:       pkgconfig(libsolv)
Provides:       pkgconfig(libsolvext)

%description -n %{name}-devel
This subpackage contains header files, pkg-config metadata and development
symlinks required to build applications that use libsolv.

%description -l ru -n %{name}-devel
Подпакет содержит заголовочные файлы, метаданные pkg-config и ссылки для
разработки, необходимые для сборки приложений, использующих libsolv.

%prep
%autosetup -p1

%build
%{cmake} \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DENABLE_BZIP2_COMPRESSION=ON \
    -DENABLE_COMPLEX_DEPS=ON \
    -DENABLE_COMPS=ON \
    -DENABLE_LZMA_COMPRESSION=ON \
    -DENABLE_PYTHON=ON \
    -DENABLE_RPMDB=ON \
    -DENABLE_RPMDB_BYRPMHEADER=ON \
    -DENABLE_RPMDB_LIBRPM=ON \
    -DENABLE_RPMMD=ON \
    -DENABLE_RPMPKG_LIBRPM=ON \
    -DENABLE_ZCHUNK_COMPRESSION=ON \
    -DENABLE_ZSTD_COMPRESSION=ON \
    -DPYTHON_EXECUTABLE=%{python3} \
    -DWITH_SYSTEM_ZCHUNK=ON \
    %{nil}

%{cmake_build}

%install
%{cmake_install}

%check
%{cmake_build} test

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE.BSD
%doc README*
%{_bindir}/*
%attr(0755,root,root) %{_libdir}/libsolv.so.*
%attr(0755,root,root) %{_libdir}/libsolvext.so.*
%{_libdir}/python3.1*/site-packages/*
%{_mandir}/man1/*

%files devel
%{_includedir}/*
%{_libdir}/libsolv.so
%{_libdir}/libsolvext.so
%{_libdir}/pkgconfig/*
%{_datadir}/cmake/*
%{_mandir}/man3/*

%changelog
* Fri Jan 09 2026 NiceOS Team <niceos@ncsgp.ru> - 0.7.35-1
- Initial build for NiceOS (Первая сборка для НАЙС.ОС)
