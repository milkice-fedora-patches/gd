Summary: A graphics library for quick creation of PNG or JPEG images.
Name: gd
Version: 1.8.4
Release: 11
URL: http://www.boutell.com/gd/
Source0: http://www.boutell.com/gd/http/gd-%{version}.tar.gz
Patch0: gd-1.8.4-redhat.patch
License: BSD-style
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Prereq: /sbin/ldconfig
BuildPrereq: freetype-devel, libjpeg-devel, libpng-devel, zlib-devel
%define shlibver %(echo %{version} | cut -f-2 -d.)

%description
The gd graphics library allows your code to quickly draw images
complete with lines, arcs, text, multiple colors, cut and paste from
other images, and flood fills, and to write out the result as a PNG or
JPEG file. This is particularly useful in Web applications, where PNG
and JPEG are two of the formats accepted for inline images by most
browsers. Note that gd is not a paint program.

%package progs
Requires: gd = %{version}, perl
Summary: Utility programs that use libgd.
Group: Applications/Multimedia

%description progs
The gd-progs package includes utility programs supplied with gd, a
graphics library for creating PNG and JPEG images. If you install
these, you must also install gd.

%package devel
Requires: gd = %{version}
Summary: The development libraries and header files for gd.
Group: Development/Libraries

%description devel
The gd-devel package contains the development libraries and header
files for gd, a graphics library for creating PNG and JPEG graphics.

%prep
%setup -q
%patch0 -p1 -b .redhat

%build
make
gcc -shared -o libgd.so.%{version} -Wl,-soname=libgd.so.%{shlibver} \
	`ar t libgd.a` -L/usr/X11R6/lib -lfreetype -ljpeg -lpng -lz -lm

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}
make install \
	INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
	INSTALL_INCLUDE=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}
install -m 755 libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
ln -s libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgd.so
ln -s libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgd.so.1
ln -s libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgd.so.1.8

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc readme.txt index.html
%{_libdir}/*.so.*

%files progs
%defattr(-,root,root)
%{_bindir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 1.8.4-10
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jan 24 2002 Phil Knirsch <pknirsch@redhat.com>
- Specfile update to add URL for homepage (#54608)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Oct 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.8.4-5
- Rebuild with current libpng

* Mon Aug 13 2001 Philipp Knirsch <pknirsch@redhat.de> 1.8.4-4
- Fixed a wrong double ownership of libgd.so (#51599).

* Fri Jul 20 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.8.4-3
- There's really no reason to link against both freetype 1.x and 2.x,
  especially when gd is configured to use just freetype 2.x. ;)

* Mon Jun 25 2001 Philipp Knirsch <pknirsch@redhat.de>
- Forgot to include the freetype library in the shared library linking. Fixed.

* Thu Jun 21 2001 Philipp Knirsch <pknirsch@redhat.de>
- Update to 1.8.4

* Tue Dec 19 2000 Philipp Knirsch <pknirsch@redhat.de>
- Updates the descriptions to get rid of al references to gif

* Tue Dec 12 2000 Philipp Knirsch <Philipp.Knirsch@redhat.de>
- Fixed bug #22001 where during installation the .so.1 and the so.1.8 links
  didn't get installed and therefore updates had problems.

* Wed Oct  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- define HAVE_LIBTTF to actually enable ttf support (oops, #18299)
- remove explicit dependencies on libpng, libjpeg, et. al.
- add BuildPrereq: freetype-devel

* Wed Aug  2 2000 Matt Wilson <msw@redhat.com>
- rebuilt against new libpng

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- add %%postun run of ldconfig (#14915)

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Nalin Dahyabhai <nalin@redhat.com> 
- update to 1.8.3

* Sat Jun  4 2000 Nalin Dahyabhai <nalin@redhat.com> 
- rebuild in new environment

* Mon May 22 2000 Nalin Dahyabhai <nalin@redhat.com> 
- break out a -progs subpackage
- disable freetype support

* Fri May 19 2000 Nalin Dahyabhai <nalin@redhat.com> 
- update to latest version (1.8.2)
- disable xpm support

* Thu Feb 03 2000 Nalin Dahyabhai <nalin@redhat.com> 
- auto rebuild in the new build environment (release 6)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 5)

* Thu Dec 17 1998 Cristian Gafton <gafton@redhat.com>
- buiuld for glibc 2.1

* Fri Sep 11 1998 Cristian Gafton <gafton@redhat.com>
- built for 5.2
