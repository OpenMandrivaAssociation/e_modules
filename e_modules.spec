#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/E-MODULES-EXTRA E-MODULES-EXTRA; \
#cd E-MODULES-EXTRA; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#PKG_VERSION=0.0.1.$SVNREV; \
#cd ..; \
#tar -Jcf E-MODULES-EXTRA-$PKG_VERSION.tar.xz E-MODULES-EXTRA/ --exclude .svn --exclude .*ignore


%define	svnrev	66640
%define	svnname	E-MODULES-EXTRA

Summary: 	Loose collection of third party E17 modules
Name: 		e_modules
Version:	0.0.1
Release:	1.%{svnrev}.1
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://enlightenment.org/
Source0: 	%{svnname}-%{version}.%{svnrev}.tar.xz
Patch0:		e_modules-0.0.1-20101229-po.patch
Patch1:		e_modules-0.0.1.62680_everything-pidgin_localization.patch
Patch2:		e_modules-0.0.1.62680_everything-tracker_localization.patch
Patch3:		e_modules-0.0.1.62680_xkbswitch_makefile.patch

BuildRequires:	edje
BuildRequires:  embryo
BuildRequires:	emprint
BuildRequires:	elementary
BuildRequires:	evas
Buildrequires:	imagemagick
Buildrequires:	gettext-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(edbus)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(eina)
BuildRequires:  pkgconfig(embryo)
BuildRequires:	pkgconfig(enlightenment)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(exalt)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(eweather)
BuildRequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(libmpd)

Requires:	e >= 0.16.999.050-3
Requires:	emprint

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

%prep
%setup -qn %{svnname}
%apply_patches

# itask-ng-moved-to-engage
rm -fr itask-ng
rm -fr weather eenvader.fractal

%build
%define Werror_cflags %nil

for i in `find * -type d|awk -F'/' '{print $1}'|sort|uniq`
do
(
	pushd $i
	NOCONFIGURE=yes ./autogen.sh
	%configure2_5x
	make
	popd
)
done

%install
rm -rf %{buildroot}
for i in `find * -type d|awk -F'/' '{print $1}'|sort|uniq`
do 
	%makeinstall_std -C $i
done

%find_lang %{name} --all-name

# do not provide devel stuffs
rm -fr %{buildroot}%{_includedir}/drawer %{buildroot}%{_libdir}/pkgconfig

%files -f %{name}.lang
%doc AUTHORS README
%{_libdir}/enlightenment/modules/*

