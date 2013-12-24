%define	gitdate	20131224

Summary:	Loose collection of third party Enlightenment modules
Name:		e_modules
Epoch:		1
Version:	0.0.1
Release:	2.%{gitdate}.1
License:	BSD
Group:		Graphical desktop/Enlightenment
Url:		http://enlightenment.org/
Source0:	%{name}-%{version}.%{gitdate}.tar.bz2
BuildRequires:	edje
BuildRequires:	embryo
BuildRequires:	elementary
BuildRequires:	evas
Buildrequires:	imagemagick
Buildrequires:	gettext-devel
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(eldbus)
BuildRequires:	pkgconfig(edje)
BuildRequires:	pkgconfig(eet)
BuildRequires:	pkgconfig(eeze)
BuildRequires:	pkgconfig(efreet)
BuildRequires:	pkgconfig(eina)
BuildRequires:	pkgconfig(embryo)
BuildRequires:	pkgconfig(enlightenment)
BuildRequires:	pkgconfig(evas)
BuildRequires:	pkgconfig(elementary)
BuildRequires:	pkgconfig(eweather)
BuildRequires:	pkgconfig(ethumb)
BuildRequires:	pkgconfig(json)
BuildRequires:	pkgconfig(libmpd)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	v8-devel
Requires:	e

%description
e_modules is a loose collection of third party Enlightenment modules written
by various authors. They are not officially a part of Enlightenment, but they
are allowed to use the Enlightenment git repository. The modules are all
separate modules, written by separate authors.

%files
%doc AUTHORS README
%{_libdir}/enlightenment/modules/*

#----------------------------------------------------------------------------

%prep
%setup -qn %{name}-%{version}.%{gitdate}

rm -fr eenvader.fractal everything-websearch packagekit

%build
%define Werror_cflags %nil

for i in `find * -type d|awk -F'/' '{print $1}'|sort|uniq`
do
(
	pushd $i
	autoreconf -fi
	%configure2_5x --disable-static
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

