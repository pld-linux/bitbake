Summary:	BitBake build tool
Summary(pl.UTF-8):	BitBake - narzędzie do budowania
Name:		bitbake
Version:	2.12.0
Release:	1
License:	GPL v2
Group:		Development
# Upstream stopped providing cgit snapshots. Regenerate the tarball with:
#   git clone https://git.openembedded.org/bitbake
#   cd bitbake && git archive --format=tar.gz --prefix=bitbake-VER/ VER -o ../bitbake-VER.tar.gz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	8f9ebc56c30c9d402b418a8ef4fcee27
URL:		https://www.yoctoproject.org/software-item/bitbake/
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	bash
Requires:	python3 >= 1:3.8
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitBake is a generic task execution engine that allows shell and Python
tasks to be run efficiently and in parallel while working within
complex inter-task dependency constraints. One of BitBake's main users,
OpenEmbedded, takes this core and builds embedded Linux software
stacks using a task-oriented approach. BitBake is co-maintained by the
Yocto Project and the OpenEmbedded project.

%description -l pl.UTF-8
BitBake to ogólnego przeznaczenia silnik wykonywania zadań,
pozwalający uruchamiać zadania powłoki oraz Pythona wydajnie i
równolegle, z poszanowaniem złożonych zależności między zadaniami.
Głównym użytkownikiem BitBake jest OpenEmbedded, który na jego
podstawie buduje stosy oprogramowania wbudowanego dla Linuksa, używając
podejścia zorientowanego na zadania.

%prep
%setup -q

sed -i -e 's@#!/bin/sh[[:space:]]@#!/bin/bash @' lib/bb/build.py

grep -rlE '^#! ?/usr/bin/env python3' bin lib | \
	xargs %{__sed} -i -e '1s,#!/usr/bin/env python3,#!%{__python3},' \
		  -e '1s,#! /usr/bin/env python3,#!%{__python3},'

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 bin/* $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{py3_sitescriptdir}
cp -a lib/. $RPM_BUILD_ROOT%{py3_sitescriptdir}

install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644 conf/bitbake.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/bitbake.conf
ln -s %{_sysconfdir}/%{name}/bitbake.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/bitbake.conf

cp -a classes $RPM_BUILD_ROOT%{_datadir}/%{name}/

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 doc/bitbake.1 $RPM_BUILD_ROOT%{_mandir}/man1/bitbake.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/bitbake.conf
%attr(755,root,root) %{_bindir}/bitbake
%attr(755,root,root) %{_bindir}/bitbake-config-build
%attr(755,root,root) %{_bindir}/bitbake-diffsigs
%attr(755,root,root) %{_bindir}/bitbake-dumpsig
%attr(755,root,root) %{_bindir}/bitbake-getvar
%attr(755,root,root) %{_bindir}/bitbake-hashclient
%attr(755,root,root) %{_bindir}/bitbake-hashserv
%attr(755,root,root) %{_bindir}/bitbake-layers
%attr(755,root,root) %{_bindir}/bitbake-prserv
%attr(755,root,root) %{_bindir}/bitbake-selftest
%attr(755,root,root) %{_bindir}/bitbake-server
%attr(755,root,root) %{_bindir}/bitbake-worker
%attr(755,root,root) %{_bindir}/git-make-shallow
%attr(755,root,root) %{_bindir}/toaster
%attr(755,root,root) %{_bindir}/toaster-eventreplay
%{_datadir}/%{name}
%{py3_sitescriptdir}/bb
%{py3_sitescriptdir}/bblayers
%{py3_sitescriptdir}/bs4
%{py3_sitescriptdir}/codegen.py
%{py3_sitescriptdir}/hashserv
%{py3_sitescriptdir}/layerindexlib
%{py3_sitescriptdir}/ply
%{py3_sitescriptdir}/progressbar
%{py3_sitescriptdir}/prserv
%{py3_sitescriptdir}/pyinotify.py
%{py3_sitescriptdir}/simplediff
%{py3_sitescriptdir}/toaster
%{_mandir}/man1/bitbake.1*
