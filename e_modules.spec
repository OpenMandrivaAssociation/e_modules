#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/E-MODULES-EXTRA E-MODULES-EXTRA; \
#cd E-MODULES-EXTRA; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#PKG_VERSION=0.0.1.$SVNREV; \
#cd ..; \
#tar -Jcf E-MODULES-EXTRA-$PKG_VERSION.tar.xz E-MODULES-EXTRA/ --exclude .svn --exclude .*ignore


%define	svnrev	84419
%define	svnname	E-MODULES-EXTRA

Summary:	Loose collection of third party E17 modules
Name:		e_modules
Epoch:		1
Version:	0.0.1
Release:	1.%{svnrev}.1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://enlightenment.org/
Source0:	%{svnname}-%{version}.%{svnrev}.tar.xz

BuildRequires:	edje
BuildRequires:	embryo
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
BuildRequires:	pkgconfig(embryo)
BuildRequires:	pkgconfig(enlightenment)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(exalt)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(eweather)
BuildRequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(json)
BuildRequires:	pkgconfig(libmpd)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	v8-devel

Requires:	e >= 0.16.999.050-3
Requires:	emprint

%description
e_modules is a loose collection of third party E17 modules written by
various authors.  They are not officially a part of E17, but they are
allowed to use the E cvs repository.  The modules are all separate
modules, written by separate authors.

%prep
%setup -qn %{svnname}

# itask-ng-moved-to-engage
rm -fr itask-ng
rm -fr weather eenvader.fractal

%build
%define Werror_cflags %nil

# Is it still needed? Looks like it breaks build so comment it out:
#for m in itask winlist-ng; do pushd $m; sed -i 's@po/Makefile@@' configure.ac ; sed -i 's@ po@@' Makefile.am; popd; done

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
for i in `find * -type d|awk -F'/' '{print $1}'|sort|uniq`
do
	%makeinstall_std -C $i
done

# Don't use it to avoid file listed twice rpm error
#find_lang %{name} --all-name

# do not provide devel stuffs
rm -fr %{buildroot}%{_includedir}/drawer %{buildroot}%{_libdir}/pkgconfig
find %{buildroot} -type f -name "*.a" -exec rm -f {} ';'

%files
%doc AUTHORS README
%{_libdir}/enlightenment/modules/*

%changelog
* Thu Jan 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 1:0.0.1-1.67107.1
+ Revision: 760556
- add back BR
- added back epoch
- new snapshot 0.0.1.67107
- fix for build errors in winlist-ng and itask
- removed static libs for modules
- new snapshot 0.0.1-20101229
- cleaned up spec
- merged UnityLinux spec
- maded p0 a p1 level patch

* Mon Jan 03 2011 Crispin Boylan <crisb@mandriva.org> 1:0.0.1-0.20101229.1mdv2011.0
+ Revision: 627878
- New tarball release

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Mon Dec 14 2009 Funda Wang <fwang@mandriva.org> 1:0.0.1-0.20091213.1mdv2010.1
+ Revision: 478424
- new snapshot

* Sun Aug 09 2009 Funda Wang <fwang@mandriva.org> 1:0.0.1-0.20090808.1mdv2010.0
+ Revision: 411853
- new snapshot
- rebuild

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 1:0.0.1-0.20090525.1mdv2010.0
+ Revision: 379503
- New snapshot

* Thu Mar 05 2009 Antoine Ginies <aginies@mandriva.com> 1:0.0.1-0.20090227.2mdv2009.1
+ Revision: 348772
- rebuild against exalt

* Tue Mar 03 2009 Antoine Ginies <aginies@mandriva.com> 1:0.0.1-0.20090227.1mdv2009.1
+ Revision: 347687
- fix exalt-devel buildrequires
- add builrequires, patch to fix e_util_dialog
- remove patch0
- add exalt-devel buildrequires
- fix tarball name
- update buildrequires
- new SVN snapshot 20090227, fix buildrequires version

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Oct 15 2008 Funda Wang <fwang@mandriva.org> 1:0.0.1-0.20080306.3mdv2009.1
+ Revision: 293990
- add conflicts to ease upgrade

* Wed Oct 15 2008 Funda Wang <fwang@mandriva.org> 1:0.0.1-0.20080306.2mdv2009.1
+ Revision: 293952
- fix conflicts with e

* Thu Mar 06 2008 Antoine Ginies <aginies@mandriva.com> 1:0.0.1-0.20080306.1mdv2008.1
+ Revision: 180815
- use %%name-%%cvs as tarball name
- fix %%setup error
- fix etk-devl buildrequires
- update tarball
- new snapshot
- update e_modules release
- restore buildrequires

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Sun Feb 03 2008 Austin Acton <austin@mandriva.org> 1:0.0.1-0.20080202.1mdv2008.1
+ Revision: 161825
- new checkout

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Antoine Ginies <aginies@mandriva.com>
    - CVS Snapshot 10071031

* Fri Aug 31 2007 Antoine Ginies <aginies@mandriva.com> 0.1.0-1mdv2008.0
+ Revision: 76859
- fix xkbfile-devel buildrequires
- CVS snapshot 07/08/31, release 0.1.0
- increase release

* Thu May 31 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1-2mdv2008.0
+ Revision: 33146
- fix exml buildrequires
- adjust e-devel and exml-devel buildrequires
- update description, CVS snapshot 20070530

* Sun May 27 2007 Antoine Ginies <aginies@mandriva.com> 0.0.1-1mdv2008.0
+ Revision: 31772
- remove missing NEWS and COPYING file
- add xcomposite1-devel buildrequires
- add efreet-devel buildrequires
- add ImageMagick buildrequires
- add a buildrequire
- adjust .lang
- adjust spec file
- add gettext-devel and cvs buildrequires
- CVS snapshot 20070526
- Import e_modules



* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20051124.1mdk
- new cvs checkout

* Thu Nov 10 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20051109.1mdk
- new cvs checkout

* Thu Oct 06 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.1-0.20050904.2mdk
- Fix BuildRequires

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050904.1mdk
- new cvs checkout

* Wed Aug 17 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050627.1mdk
- new cvs checkout

* Thu Jun 09 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050608.1mdk
- new cvs checkout

* Mon May 16 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050511.2mdk
- don't own modules_extra

* Mon May 16 2005 Austin Acton <austin@mandriva.org> 0.0.1-0.20050511.1mdk
- initial package
