Summary:	Distributed software management system for Linux distributions
Summary(pl):	Rozproszony system zarz�dzania oprogramowaniem dla dystrybucji Linuksa
Name:		conary
Version:	0.11.0
Release:	0.1
License:	CPL 1.0
Group:		Applications/System
Source0:	ftp://download.specifixinc.com/pub/conary/%{name}-%{version}.tar.bz2
# Source0-md5:	d14347f4801c07a32cd6e76541287ed4
URL:		http://wiki.specifixinc.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite-devel >= 3.0.0
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

%description -l pl
Conary to rozproszony system zarz�dzania oprogramowaniem dla
dystrybucji Linuksa. Zast�puje tradycyjne rozwi�zania zarz�dzania
pakietami (takie jak RPM czy dpkg) jednym, zaprojektowanym aby
umo�liwi� lu�n� wsp�prac� poprzez Internet. Umo�liwia zbiorom
rozproszonych i lu�no powi�zanych repozytori�w na definiowanie
komponent�w, kt�re s� instalowane w systemie linuksowym. Zamiast
posiadania pe�nej dystrybucji pochodz�cej od jednego producenta,
pozwala administratorom i deweloperom na odga��zienie dystrybucji,
trzymanie kawa�k�w pasuj�cych do ich �rodowiska i wyci�ganie
komponent�w � innych repozytori�w z Internetu.

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
