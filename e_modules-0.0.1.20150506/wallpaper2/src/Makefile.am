MAINTAINERCLEANFILES = Makefile.in

AM_CPPFLAGS = -I. \
	   -I$(top_srcdir) \
	   -I$(includedir) \
	   -DLOCALEDIR=\"$(datadir)/locale\" \
	   -DPACKAGE_DATA_DIR=\"$(module_dir)/$(PACKAGE)\" \
	   @E_CFLAGS@

pkgdir = $(module_dir)/$(PACKAGE)/$(MODULE_ARCH)
pkg_LTLIBRARIES = module.la
module_la_SOURCES = e_mod_main.h \
		    e_mod_main.c \
                    e_int_config_wallpaper.c

module_la_LIBADD = @E_LIBS@
module_la_LDFLAGS = -module -avoid-version
module_la_DEPENDENCIES = $(top_builddir)/config.h

clean-local:
	rm -rf *~
