%define	name e_modules
%define	version 0.0.1
%define release %mkrel 1


Summary: 	Enlightenment modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.038, esmart-devel >= 0.9.0.008
BuildRequires:	ecore-devel >= 0.9.9.038, edje-devel >= 0.5.0.038
BuildRequires:	eet-devel >= 0.9.10.038, %{mklibname e0}-devel >= 0.16.999.038, %{mklibname exml1}-devel >= 0.1.1
BuildRequires:  edje >= 0.5.0.038, etk-devel >= 0.1.0.003
BuildRequires:  embryo >= 0.9.1.038
requires:	e >= 0.16.999.038
Buildrequires:	gettext-devel, cvs, %{mklibname exml1} >= 0.1.1
Buildrequires:  %{mklibname xkbfile1}-devel
Buildrequires:	ImageMagick, efreet-devel

%description
e_modules - a collection of modules for enlightenment

Snow module for the Enlightenment window manager.
Flame module for the Enlightenment window manager.
Weather module for the Enlightenment window manager.
Monitor module for the Enlightenment window manager.

This package is part of the Enlightenment DR17 desktop shell.

%prep
%setup -q

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/ephoto.mo
%find_lang %{name}
cd $RPM_BUILD_ROOT/%_datadir/locale/
LIST=`find . -name \*.mo -exec echo {} \;| cut -d '.' -f 2`
for mo in `$LIST`;
do
LG=`echo $mo | cut -d '/' -f 2`
echo "%lang($LG) $(echo %_datadir/locale/$mo)" >> $RPM_BUILD_DIR/%{name}-%{version}/%{name}.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_bindir}/emu_client
%_datadir/locale/*
%{_libdir}/enlightenment/modules/*
