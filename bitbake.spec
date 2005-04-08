Summary:	BitBake build tool
Name:		bitbake
Version:	1.2
Release:	1
License:	GPL
Group:		Development
Source0:	http://download.berlios.de/bitbake/%{name}-%{version}.tar.gz
# Source0-md5:	62c799d91d291a17078d6c23a94e793e
URL:		http://developer.berlios.de/projects/bitbake/
BuildRequires:	python-devel >= 2.0
%pyrequires_eq	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BitBake is a simple tool for the execution of tasks. It is derived
from Portage, which is the package management system used by the
Gentoo Linux distribution. It is most commonly used to build packages,
as it can easily use its rudamentary inheritence to abstract common
operations, such as fetching sources, unpacking them, patching them,
compiling them, and so on. It is the basis of the OpenEmbedded
project, which is being used for OpenZaurus, Familiar, and a number of
other Linux distributions.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}
python setup.py install \
	--prefix=%{_prefix} \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_prefix}/%{name} $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/%{name}
%dir %{py_sitescriptdir}/bb
%{py_sitescriptdir}/bb/*py[co]
%dir %{py_sitescriptdir}/bb/parse
%{py_sitescriptdir}/bb/parse/*py[co]
