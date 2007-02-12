Summary:	Distributed software management system for Linux distributions
Summary(pl.UTF-8):   Rozproszony system zarządzania oprogramowaniem dla dystrybucji Linuksa
Name:		conary
Version:	0.62.14
Release:	0.1
License:	CPL 1.0
Group:		Applications/System
Source0:	ftp://download.rpath.com/pub/conary/%{name}-%{version}.tar.bz2
# Source0-md5:	c7e665a227c59f610cbce84971b82ebf
URL:		http://wiki.conary.com/
BuildRequires:	python-kid
BuildRequires:	python-devel
BuildRequires:	sqlite3-devel >= 3.0.0
Requires:	python-devel-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	%{_libdir}

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

%description -l pl.UTF-8
Conary to rozproszony system zarządzania oprogramowaniem dla
dystrybucji Linuksa. Zastępuje tradycyjne rozwiązania zarządzania
pakietami (takie jak RPM czy dpkg) jednym, zaprojektowanym aby
umożliwić luźną współpracę poprzez Internet. Umożliwia zbiorom
rozproszonych i luźno powiązanych repozytoriów na definiowanie
komponentów, które są instalowane w systemie linuksowym. Zamiast
posiadania pełnej dystrybucji pochodzącej od jednego producenta,
pozwala administratorom i deweloperom na odgałęzienie dystrybucji,
trzymanie kawałków pasujących do ich środowiska i wyciąganie
komponentów ż innych repozytoriów z Internetu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	PYTHON=%{_bindir}/python \
	conarydir=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PYTHON=%{_bindir}/python \
	conarydir=%{_datadir}/%{name}

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
