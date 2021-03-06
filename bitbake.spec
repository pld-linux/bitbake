Summary:	BitBake build tool
Summary(pl.UTF-8):	BitBake - narzędzie do budowania
Name:		bitbake
Version:	1.17.0
Release:	1
License:	GPL v2
Group:		Development
Source0:	http://git.openembedded.org/bitbake/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	6ff19a24fdd20623b792225d84017506
URL:		https://www.yoctoproject.org/tools-resources/projects/bitbake
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	libxml2-progs
BuildRequires:	libxslt
BuildRequires:	libxslt-progs
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-sqlite
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildConflicts:	bitbake
Requires:	bash
Requires:	python
Requires:	python-modules
Requires:	python-ply
Requires:	python-progressbar
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitBake is a make-like build tool with the special focus of
distributions and packages for embedded Linux cross compilation
although it is not limited to that. It is inspired by Portage, which
is the package management system used by the Gentoo Linux
distribution. BitBake existed for some time in the OpenEmbedded
project until it was separated out into a standalone, maintained,
distribution-independent tool. BitBake is co-maintained by the Yocto
Project and the OpenEmbedded project.

%description -l pl.UTF-8
BitBake to proste narzędzie do wykonywania zadań. Wywodzi się z
Portage, które jest systemem zarządzania pakietami używanym w
dystrybucji Linuksa Gentoo. Najczęściej jest używane do budowania
pakietów, jako że może łatwo używać swojej elementarnej dziedziczności
do abstrahowania wspólnych operacji, takich jak pobieranie źródeł,
rozpakowywanie ich, łatanie, kompilowanie i tak dalej. Jest podstawą
projektu OpenEmbedded, używanego przez projekty OpenZaurus, Familiar i
wiele innych dystrybucji Linuksa.

%package manual
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description manual
Documentation for %{name}.

%description manual -l fr.UTF-8
Documentation pour %{name}.

%description manual -l it.UTF-8
Documentazione di %{name}.

%description manual -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q
sed -i -e 's@#!/bin/sh[[:space:]]@#!/bin/bash @' lib/bb/build.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
ln -s %{_sysconfdir}/%{name}/%{name}.conf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/%{name}.conf
%attr(755,root,root) %{_bindir}/bitbake
%attr(755,root,root) %{_bindir}/bitbake-diffsigs
%attr(755,root,root) %{_bindir}/bitbake-layers
%attr(755,root,root) %{_bindir}/bitbake-prserv
%attr(755,root,root) %{_bindir}/bitbake-selftest
%attr(755,root,root) %{_bindir}/image-writer
%{_datadir}/%{name}
%{py_sitescriptdir}/bb
%{py_sitescriptdir}/bitbake-%{version}-py*.egg-info
%{py_sitescriptdir}/codegen.py[co]
%{py_sitescriptdir}/prserv

%files manual
%defattr(644,root,root,755)
%doc doc/manual/html/*
