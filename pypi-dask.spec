#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dask
Version  : 2022.12.1
Release  : 177
URL      : https://files.pythonhosted.org/packages/9f/cb/e639a8499d9e0161f62439cbc1c2d4bb4ff27f6fc53244cc0d886cef70b5/dask-2022.12.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9f/cb/e639a8499d9e0161f62439cbc1c2d4bb4ff27f6fc53244cc0d886cef70b5/dask-2022.12.1.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-dask-bin = %{version}-%{release}
Requires: pypi-dask-license = %{version}-%{release}
Requires: pypi-dask-python = %{version}-%{release}
Requires: pypi-dask-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(cloudpickle)
BuildRequires : pypi(fsspec)
BuildRequires : pypi(packaging)
BuildRequires : pypi(partd)
BuildRequires : pypi(pytest_runner)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(toolz)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Dask
====
|Build Status| |Coverage| |Doc Status| |Discourse| |Version Status| |NumFOCUS|

%package bin
Summary: bin components for the pypi-dask package.
Group: Binaries
Requires: pypi-dask-license = %{version}-%{release}

%description bin
bin components for the pypi-dask package.


%package license
Summary: license components for the pypi-dask package.
Group: Default

%description license
license components for the pypi-dask package.


%package python
Summary: python components for the pypi-dask package.
Group: Default
Requires: pypi-dask-python3 = %{version}-%{release}

%description python
python components for the pypi-dask package.


%package python3
Summary: python3 components for the pypi-dask package.
Group: Default
Requires: python3-core
Provides: pypi(dask)
Requires: pypi(click)
Requires: pypi(cloudpickle)
Requires: pypi(fsspec)
Requires: pypi(packaging)
Requires: pypi(partd)
Requires: pypi(pyyaml)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-dask package.


%prep
%setup -q -n dask-2022.12.1
cd %{_builddir}/dask-2022.12.1
pushd ..
cp -a dask-2022.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672266778
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-dask
cp %{_builddir}/dask-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-dask/a13640c0c947476791b93d0878e07dc9cc7caeea || :
cp %{_builddir}/dask-%{version}/dask/array/NUMPY_LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-dask/dc62380a94a8f632cfd8afabbf101a51d6773ac8 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/dask

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dask/a13640c0c947476791b93d0878e07dc9cc7caeea
/usr/share/package-licenses/pypi-dask/dc62380a94a8f632cfd8afabbf101a51d6773ac8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
