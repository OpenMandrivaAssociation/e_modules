%define	name	e_modules
%define	version	0.0.1
%define release 0.%{cvsrel}.1mdk

%define cvsrel 20051124

Summary: 	Enlightenment modules
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{cvsrel}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel esmart-devel
BuildRequires:	ecore-devel edje-devel 
BuildRequires:	eet-devel e-devel
BuildRequires:  edje
BuildRequires:  embryo

%description
e_modules - a collection of modules for enlightenment

Flame....: A module that displays flame at the bottom of the screen.
Notes....: A module that displays sticky notes.
Snow.....: A module that displays christmas trees and falling snow on
           your desktop.

This package is part of the Enlightenment DR17 desktop shell.

%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/%{name}
%{_libdir}/enlightenment/modules_extra/*
