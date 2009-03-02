%define	name e_modules
%define	version 0.0.1
%define	svn	20090227
%define release %mkrel 0.%{svn}.1

Summary: 	Loose collection of third party E17 modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Epoch:		1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%version-%{svn}.tar.bz2
Patch0:		notification-fix-datadir.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050
BuildRequires:	esmart-devel >= 0.9.0.050
BuildRequires:	ecore-devel >= 0.9.9.050
BuildRequires:	edje-devel >= 0.9.9.050, edje >= 0.9.9.0.050
BuildRequires:	efreet-devel >= 0.5.0.050
BuildRequires:	e-devel >= 0.16.999.050
BuildRequires:	exml-devel >= 0.1.1, exml >= 0.1.1
BuildRequires:  etk-devel >= 0.1.0.042
BuildRequires:  embryo-devel >= 0.9.9.050, embryo >= 0.9.9.050
BuildRequires:	e_dbus-devel >= 0.5.0.050
Buildrequires:	libexalt-devel >= 0.6
BuildRequires:	emprint
Buildrequires:	gettext-devel
Buildrequires:  libxkbfile-devel
Buildrequires:	imagemagick
Buildrequires:  libxcomposite-devel
BuildRequires:	libmpd-devel
Conflicts:	e < 0.16.999.050-3
Requires:	e >= 0.16.999.050-3
Requires:	emprint

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

%prep
%setup -q -n %name-%version-%svn
pushd notification
%patch0
popd

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}

# provided by e >= 0.16.999.050
rm -fr %buildroot%{_libdir}/enlightenment/modules/mixer

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
%{_libdir}/enlightenment/modules/*
