#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	docopt
Summary:	Pythonic argument parser, that will make you smile
Summary(pl.UTF-8):	Przyjemny pythonowy parser argumentów
Name:		python-%{module}
Version:	0.6.2
Release:	12
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/docopt/
Source0:	https://files.pythonhosted.org/packages/source/d/docopt/%{module}-%{version}.tar.gz
# Source0-md5:	4bc74561b37fad5d3e7d037f82a4c3b1
URL:		http://docopt.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
docopt creates beautiful command-line interfaces.

%description -l pl.UTF-8
docopt tworzy ładne interfejsy linii poleceń.

%package -n python3-%{module}
Summary:	Pythonic argument parser, that will make you smile
Summary(pl.UTF-8):	Przyjemny pythonowy parser argumentów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{module}
docopt creates beautiful command-line interfaces.

%description -n python3-%{module} -l pl.UTF-8
docopt tworzy ładne interfejsy linii poleceń.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/git/git.py
%endif
%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}/git/git.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE-MIT README.rst
%{py_sitescriptdir}/docopt.py[co]
%{py_sitescriptdir}/docopt-%{version}-py*.egg-info
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE-MIT README.rst
%{py3_sitescriptdir}/__pycache__/docopt.cpython-*.py[co]
%{py3_sitescriptdir}/docopt.py
%{py3_sitescriptdir}/docopt-%{version}-py*.egg-info
%{_examplesdir}/python3-%{module}-%{version}
%endif
