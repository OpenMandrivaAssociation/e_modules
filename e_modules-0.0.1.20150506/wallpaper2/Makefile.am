ACLOCAL_AMFLAGS = -I m4

MAINTAINERCLEANFILES = \
m4/libtool.m4 \
m4/wchar_t.m4 \
m4/uintmax_t.m4 \
m4/inttypes-pri.m4 \
m4/xsize.m4 \
m4/longdouble.m4 \
m4/nls.m4 \
m4/lt~obsolete.m4 \
m4/wint_t.m4 \
m4/isc-posix.m4 \
m4/printf-posix.m4 \
m4/po.m4 \
m4/signed.m4 \
m4/lcmessage.m4 \
m4/intmax.m4 \
m4/ltoptions.m4 \
m4/ulonglong.m4 \
m4/progtest.m4 \
m4/glibc21.m4 \
m4/inttypes.m4 \
m4/codeset.m4 \
m4/stdint_h.m4 \
m4/ltsugar.m4 \
m4/longlong.m4 \
m4/inttypes_h.m4 \
m4/lib-ld.m4 \
m4/lib-link.m4 \
m4/gettext.m4 \
m4/size_max.m4 \
m4/ltversion.m4 \
m4/lib-prefix.m4 \
m4/iconv.m4 \
m4/intdiv0.m4 \
Makefile.in \
aclocal.m4 \
config.guess \
config.h.in \
config.sub \
configure \
depcomp \
install-sh \
ltmain.sh \
missing \
module.\
desktop \
config.rpath \
mkinstalldirs

SUBDIRS = src

if HAVE_PO

SUBDIRS += po

endif

filesdir = $(module_dir)/$(PACKAGE)
files_DATA = module.desktop

EXTRA_DIST = module.desktop.in

clean-local:
	 rm -rf *.edj module.desktop *~

uninstall-local:
	 rm -rf $(DESTDIR)$(module_dir)/$(PACKAGE)

