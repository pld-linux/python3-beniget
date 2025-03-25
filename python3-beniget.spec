#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Extract semantic information about static Python code
Summary(pl.UTF-8):	Wydobywanie informacji semantycznych o statycznym kodzie w Pythonie
Name:		python3-beniget
Version:	0.4.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/beniget/
Source0:	https://files.pythonhosted.org/packages/source/b/beniget/beniget-%{version}.tar.gz
# Source0-md5:	499c6c442b54ec297970de80adba330d
URL:		https://pypi.org/project/beniget/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-gast >= 0.5.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A static analyzer for Python3 code.

Beniget provides a static over-approximation of the global and local
definitions inside Python Module/Class/Function. It can also compute
def-use chains from each definition.

%description -l pl.UTF-8
Statyczny analizator kodu Pythona 3.

Beniget zapewnia statyczną (nad)aproksymację globalnych i lokalnych
definicji wewnątrz modułów/klas/funkcji pythonowych. Potrafi także
wyliczać łańcuchy def-użyć z każdej definicji.

%prep
%setup -q -n beniget-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/beniget
%{py3_sitescriptdir}/beniget-%{version}-py*.egg-info
