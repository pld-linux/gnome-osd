Summary:	OSD notification system for the GNOME desktop
Summary(pl):	System powiadamiania OSD dla GNOME
Name:		gnome-osd
Version:	0.5.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://yang.inescn.pt/~gjc/gnome-osd/%{name}-%{version}.tar.bz2
# Source0-md5:	13ae7be2502ca22d616cd1dfd8b79c06
BuildRequires:	GConf2-devel
BuildRequires:	python-gnome-devel >= 2.5.90
BuildRequires:	python-pyorbit-devel >= 2.0.0
Requires(post):	GConf2
Requires:	python-gnome-devel >= 2.5.90
Requires:	python-pyorbit-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME OSD is an OSD (On Screen Display) notification system for the
GNOME desktop.

%description -l pl
GNOME OSD jest systemem powiadamiania OSD dla GNOME.

%prep
%setup -q

# Regenerat
rm -f gnome_osd_conf.py

%build
%configure \
	--disable-schemas-install

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
%{py_sitedir}/*.py[co]
%{py_sitedir}/gnome_osd_conf.py
%{_pixmapsdir}/*
%{_datadir}/gnome/capplets/*.desktop
