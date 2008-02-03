%define	name e_modules
%define	version 0.0.1
%define	cvs	20080202
%define release %mkrel 0.%{cvs}.1

Summary: 	E_modules is a loose collection of third party E17 modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Epoch:		1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{cvs}.tar.bz2
Patch0:		notification-fix-datadir.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel
BuildRequires:	esmart-devel
BuildRequires:	ecore-devel
BuildRequires:	edje-devel, edje
BuildRequires:	efreet-devel
BuildRequires:	e-devel
BuildRequires:	exml-devel, exml
BuildRequires:  etk-devel
BuildRequires:  embryo-devel, embryo
BuildRequires:	e_dbus-devel
BuildRequires:	emprint
Buildrequires:	gettext-devel
Buildrequires:  libxkbfile-devel
Buildrequires:	ImageMagick
Buildrequires:  libxcomposite-devel
BuildRequires:	libmpd-devel
Requires:	e
Requires:	emprint

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

%prep
%setup -q -n %name
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

#cd $RPM_BUILD_ROOT/%_datadir/locale/
#LIST=`find . -name \*.mo -exec echo {} \;| cut -d '.' -f 2`
#for mo in `$LIST`;
#do
#LG=`echo $mo | cut -d '/' -f 2`
#echo "%lang($LG) $(echo %_datadir/locale/$mo)" >> $RPM_BUILD_DIR/%{name}-%{version}/%{name}.lang
#done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README
#%{_bindir}/emu_client
#%_datadir/locale/*
%{_libdir}/enlightenment/modules/*
