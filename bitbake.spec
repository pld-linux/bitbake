Summary:	BitBake build tool
Summary(pl.UTF-8):	BitBake - narzędzie do budowania
Name:		bitbake
Version:	1.8.18
Release:	1
License:	GPL
Group:		Development
Source0:	http://download.berlios.de/bitbake/%{name}-%{version}.tar.gz
# Source0-md5:	f772ca3121103ab3500c7f1609a96271
URL:		http://developer.berlios.de/projects/bitbake/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	sed >= 4.0
%pyrequires_eq	python
Requires:	bash
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitBake is a simple tool for the execution of tasks. It is derived
from Portage, which is the package management system used by the
Gentoo Linux distribution. It is most commonly used to build packages,
as it can easily use its rudimentary inheritance to abstract common
operations, such as fetching sources, unpacking them, patching them,
compiling them, and so on. It is the basis of the OpenEmbedded
project, which is being used for OpenZaurus, Familiar, and a number of
other Linux distributions.

%description -l pl.UTF-8
BitBake to proste narzędzie do wykonywania zadań. Wywodzi się z
Portage, które jest systemem zarządzania pakietami używanym w
dystrybucji Linuksa Gentoo. Najczęściej jest używane do budowania
pakietów, jako że może łatwo używać swojej elementarnej dziedziczności
do abstrahowania wspólnych operacji, takich jak pobieranie źródeł,
rozpakowywanie ich, łatanie, kompilowanie i tak dalej. Jest podstawą
projektu OpenEmbedded, używanego przez projekty OpenZaurus, Familiar i
wiele innych dystrybucji Linuksa.

%prep
%setup -q
sed -i	-e 's@#!/bin/sh[[:space:]]@#!/bin/bash @'	\
	-e 's@%s%ssh[[:space:]]@%s%sbash @'	lib/bb/build.py

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

python setup.py install \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/%{name}/conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s %{_sysconfdir}/%{name} $RPM_BUILD_ROOT%{_datadir}/%{name}/conf

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}
%{_datadir}/%{name}
%dir %{py_sitescriptdir}/bb
%{py_sitescriptdir}/bb/*py[co]
%dir %{py_sitescriptdir}/bb/fetch
%{py_sitescriptdir}/bb/fetch/*py[co]
%dir %{py_sitescriptdir}/bb/parse
%{py_sitescriptdir}/bb/parse/*py[co]
%dir %{py_sitescriptdir}/bb/parse/parse_py
%{py_sitescriptdir}/bb/parse/parse_py/*py[co]
