%define	name e_modules
%define	version 0.1.0
%define release %mkrel 2


Summary: 	E_modules is a loose collection of third party E17 modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.041, esmart-devel >= 0.9.0.011
BuildRequires:	ecore-devel >= 0.9.9.041, edje-devel >= 0.5.0.041
BuildRequires:	eet-devel >= 0.9.10.041, e-devel >= 0.16.999.041, exml-devel >= 0.1.1
BuildRequires:  edje >= 0.5.0.041, etk-devel >= 0.1.0.007
BuildRequires:  embryo >= 0.9.1.041
requires:	e >= 0.16.999.041
Buildrequires:	gettext-devel, cvs, exml >= 0.1.1
Buildrequires:  %{mklibname xkbfile}-devel
Buildrequires:	ImageMagick, efreet-devel
Buildrequires:  %{mklibname xcomposite1}-devel

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

alarm - Sets reminders and timer.  (Replaces eveil.)
bling - EFLized Composite Manager for E17. (Not for users right now).
calendar - A module to display a desktop calendar.
cpu - A module to monitor cpu load.  (Will be replaced by something better.)
deskshow - A module to iconify/uniconify all current windows to show the
emu - Experimental generic scriptable module for E17.
engage - Icon bar / task bar / system tray.
flame - A module to display flames on the desktop.
forecasts - A module to display  the current condition and forecasts.
language - A module to control active keyboard/keyboard layout/layout variant.
mail - A module to periodically check for new email.
mem - A module to monitor memory and swap usage.  (Will be replaced by something better.)
mixer - A module to control volume for some mixers.  (Will be replaced by something better.)
moon - A module to display moon phase information.
net - A module to monitor traffic on a network device.
news - A module to display rss feeds.
photo - A module to display pictures on the desktop.
rain - A module to display rain on the desktop.
screenshot - A module to take screenshots, utilizing scrot or import.
slideshow - A module to cycle desktop backgrounds.
snow - A module to display snow on the desktop.
taskbar - A taskbar module.  (Will be replaced by something better.)
tclock - A module to display a digital clock on the desktop.  (Will be replaced by something better.)
uptime - A module to monitor computer uptime.
weather - A module to display a weather forecast.
winselector - A module to show menu-based access to open windows.
wlan - A module to monitor a wlan device.

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
%doc AUTHORS README
%{_bindir}/emu_client
%_datadir/locale/*
%{_libdir}/enlightenment/modules/*
