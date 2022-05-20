#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-dask
Version  : 2022.5.0
Release  : 152
URL      : https://files.pythonhosted.org/packages/d5/61/2ab5b87c89a91e96aa2039722b60570d4cae4961afa47a8f3dacc66bbcd9/dask-2022.5.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/61/2ab5b87c89a91e96aa2039722b60570d4cae4961afa47a8f3dacc66bbcd9/dask-2022.5.0.tar.gz
Summary  : Parallel PyData with Task Scheduling
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-dask-license = %{version}-%{release}
Requires: pypi-dask-python = %{version}-%{release}
Requires: pypi-dask-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cloudpickle)
BuildRequires : pypi(fsspec)
BuildRequires : pypi(packaging)
BuildRequires : pypi(partd)
BuildRequires : pypi(pytest_runner)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(toolz)

%description
Dask
====
|Build Status| |Coverage| |Doc Status| |Discourse| |Version Status| |NumFOCUS|

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
Requires: pypi(cloudpickle)
Requires: pypi(fsspec)
Requires: pypi(packaging)
Requires: pypi(partd)
Requires: pypi(pyyaml)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-dask package.


%prep
%setup -q -n dask-2022.5.0
cd %{_builddir}/dask-2022.5.0
pushd ..
cp -a dask-2022.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653055392
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
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
cp %{_builddir}/dask-2022.5.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-dask/a13640c0c947476791b93d0878e07dc9cc7caeea
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-dask/a13640c0c947476791b93d0878e07dc9cc7caeea

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
