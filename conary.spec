Summary:	Distributed software management system for Linux distributions
Name:		conary
Version:	0.9.0
Release:	1
License:	CPL 1.0
Group:		Applications/System
Source0:	ftp://download.specifixinc.com/pub/conary/%{name}-%{version}.tar.bz2
# Source0-md5:	011f2410365102b56fc79369cccccbf1
URL:		http://wiki.specifixinc.com/
BuildRequires:	rpm-pythonprov
BuildRequires:	python-devel
BuildRequires:	sqlite-devel >= 3.0.0
Requires:	python-devel-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conary is a distributed software management system for Linux
distributions. It replaces traditional package management solutions
(such as RPM and dpkg) with one designed to enable loose collaboration
across the Internet. It enables sets of distributed and loosely
connected repositories to define the components which are installed on
a Linux system. Rather then having a full distribution come from a
single vendor, it allows administrators and developers to branch a
distribution, keeping the pieces which fit their environment while
grabbing components from other repositories across the Internet.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	PYTHON=%{_bindir}/python

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON=%{_bindir}/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/build
%dir %{_datadir}/%{name}/deps
%dir %{_datadir}/%{name}/lib
%dir %{_datadir}/%{name}/local
%dir %{_datadir}/%{name}/repository
%dir %{_datadir}/%{name}/sqlite3
%{_datadir}/%{name}/*.py[oc]
%{_datadir}/%{name}/*/*.py[oc]
%attr(755,root,root) %{_datadir}/%{name}/*.so
%attr(755,root,root) %{_datadir}/%{name}/*/*.so
%attr(755,root,root) %{_datadir}/%{name}/conary
%attr(755,root,root) %{_datadir}/%{name}/cvc
%{_mandir}/man*/*
