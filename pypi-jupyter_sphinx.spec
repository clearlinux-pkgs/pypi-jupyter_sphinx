#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyter_sphinx
Version  : 0.3.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/19/b0/46405f8cea06cc60a851db29486c10244691d014e4ff21a887a17fbed574/jupyter_sphinx-0.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/19/b0/46405f8cea06cc60a851db29486c10244691d014e4ff21a887a17fbed574/jupyter_sphinx-0.3.2.tar.gz
Summary  : Jupyter Sphinx Extensions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jupyter_sphinx-license = %{version}-%{release}
Requires: pypi-jupyter_sphinx-python = %{version}-%{release}
Requires: pypi-jupyter_sphinx-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: jupyter_sphinx
Provides: jupyter_sphinx-python
Provides: jupyter_sphinx-python3
BuildRequires : pypi(ipython)
BuildRequires : pypi(ipywidgets)
BuildRequires : pypi(nbconvert)
BuildRequires : pypi(nbformat)
BuildRequires : pypi(sphinx)

%description
``jupyter-sphinx`` enables running code embedded in Sphinx documentation and
        embedding output of that code into the resulting document. It has support
        for rich output such as images and even Jupyter interactive widgets.
        
        ## Installation

%package license
Summary: license components for the pypi-jupyter_sphinx package.
Group: Default

%description license
license components for the pypi-jupyter_sphinx package.


%package python
Summary: python components for the pypi-jupyter_sphinx package.
Group: Default
Requires: pypi-jupyter_sphinx-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyter_sphinx package.


%package python3
Summary: python3 components for the pypi-jupyter_sphinx package.
Group: Default
Requires: python3-core
Provides: pypi(jupyter_sphinx)
Requires: pypi(ipython)
Requires: pypi(ipywidgets)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(sphinx)

%description python3
python3 components for the pypi-jupyter_sphinx package.


%prep
%setup -q -n jupyter_sphinx-0.3.2
cd %{_builddir}/jupyter_sphinx-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641451795
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyter_sphinx
cp %{_builddir}/jupyter_sphinx-0.3.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyter_sphinx/ae6eafc2360a1460abcaa0567a06a78fd44f0c5e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyter_sphinx/ae6eafc2360a1460abcaa0567a06a78fd44f0c5e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*