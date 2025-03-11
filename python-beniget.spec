#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Extract semantic information about static Python code
Summary(pl.UTF-8):	Wydobywanie informacji semantycznych o statycznym kodzie w Pythonie
Name:		python-beniget
Version:	0.4.1
Release:	5
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/beniget/
Source0:	https://files.pythonhosted.org/packages/source/b/beniget/beniget-%{version}.tar.gz
# Source0-md5:	a2bbe7f17f10f9c127d8ef00692ddc55
URL:		https://pypi.org/project/beniget/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-gast >= 0.5.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-gast >= 0.5.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A static analyzer for Python2 and Python3 code.

Beniget provides a static over-approximation of the global and local
definitions inside Python Module/Class/Function. It can also compute
def-use chains from each definition.

%description -l pl.UTF-8
Statyczny analizator kodu Pythona 2 i 3.

Beniget zapewnia statyczną (nad)aproksymację globalnych i lokalnych
definicji wewnątrz modułów/klas/funkcji pythonowych. Potrafi także
wyliczać łańcuchy def-użyć z każdej definicji.

%package -n python3-beniget
Summary:	Extract semantic information about static Python code
Summary(pl.UTF-8):	Wydobywanie informacji semantycznych o statycznym kodzie w Pythonie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-beniget
A static analyzer for Python2 and Python3 code.

Beniget provides a static over-approximation of the global and local
definitions inside Python Module/Class/Function. It can also compute
def-use chains from each definition.

%description -n python3-beniget -l pl.UTF-8
Statyczny analizator kodu Pythona 2 i 3.

Beniget zapewnia statyczną (nad)aproksymację globalnych i lokalnych
definicji wewnątrz modułów/klas/funkcji pythonowych. Potrafi także
wyliczać łańcuchy def-użyć z każdej definicji.

%prep
%setup -q -n beniget-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/beniget
%{py_sitescriptdir}/beniget-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-beniget
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/beniget
%{py3_sitescriptdir}/beniget-%{version}-py*.egg-info
%endif
