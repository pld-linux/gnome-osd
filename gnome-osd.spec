# TODO:
# - really devel package are required??
Summary:	OSD notification system for the GNOME desktop
Summary(pl.UTF-8):	System powiadamiania OSD dla GNOME
Name:		gnome-osd
Version:	0.8.0
Release:	0.9
License:	GPL
Group:		X11/Applications
Source0:	http://telecom.inescporto.pt/~gjc/gnome-osd/%{name}_%{version}-1.tar.gz
# Source0-md5:	7dea83abc9c69cf76925b22110499702
URL:		http://www.gnomefiles.org/app.php?soft_id=350
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	python-gnome-devel >= 2.6.0
BuildRequires:	python-pyorbit-devel >= 2.0.0
Requires(post):	GConf2
Requires:	python-gnome-devel >= 2.6.0
Requires:	python-pyorbit-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME OSD is an OSD (On Screen Display) notification system for the
GNOME desktop.

%description -l pl.UTF-8
GNOME OSD jest systemem powiadamiania OSD dla GNOME.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	PYTHON=%{__python}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/control-center-2.0/capplets/*.desktop \
	$RPM_BUILD_ROOT%{_datadir}/gnome/capplets

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/bonobo/servers/*.server
%attr(755,root,root)  %{_libdir}/gnome-osd-server
%dir %{py_sitedir}/gnomeosd
%{py_sitedir}/gnomeosd/*.py[co]
%{py_sitedir}/gnomeosd/gnome_osd_conf.py
%{_pixmapsdir}/*
%{_datadir}/gnome/capplets/*.desktop
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/*.py
