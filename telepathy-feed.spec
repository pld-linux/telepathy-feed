Summary:	Galago feed for Telepathy
Summary(pl.UTF-8):	Feed Galago dla Telepathy
Name:		telepathy-feed
Version:	0.13
Release:	1
License:	LGPL
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-feed/%{name}-%{version}.tar.gz
# Source0-md5:	ff6273a82c96db813526ea599ac3b6ff
URL:		https://telepathy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.8
BuildRequires:	libgalago-devel >= 0.3.3.90
BuildRequires:	libtelepathy-devel >= 0.0.30
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libgalago >= 0.3.3.90
Requires:	libtelepathy >= 0.0.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Galago feed for Telepathy.

%description -l pl.UTF-8
Feed Galago dla Telepathy.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/galago/telepathy-feed
