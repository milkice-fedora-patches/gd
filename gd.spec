Summary: A graphics library for drawing .gif files.
Name: gd
Version: 1.8.3
Release: 4
Source0: http://www.boutell.com/gd/http/gd-%{version}.tar.gz
Patch0: gd-1.8.2-redhat.patch
Copyright: BSD-style
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root
Prereq: /sbin/ldconfig
BuildPrereq: libjpeg-devel, libpng-devel, zlib-devel
Requires: libjpeg, libpng, zlib
%define shlibver %(echo %{version} | cut -f-2 -d.)

%description
Gd is a graphics library for drawing .gif files.  Gd allows your code to
quickly draw images (lines, arcs, text, multiple colors, cutting and
pasting from other images, flood fills) and write out the result as a
.gif file. Gd is particularly useful in web applications, where .gifs
are commonly used as inline images.  Note, however, that gd is not a
paint program.

Install gd if you are developing applications which need to draw .gif
files.  If you install gd, you'll also need to install the gd-devel
package.

%package progs
Requires: gd = %{version}, perl
Summary: Utility programs that use libgd.
Group: Applications/Multimedia

%description progs
These are utility programs supplied with gd, the .jpeg graphics library.
If you install these, you must install gd.

%package devel
Requires: gd = %{version}
Summary: The development libraries and header files for gd.
Group: Development/Libraries

%description devel
These are the development libraries and header files for gd, the .gif
graphics library.

If you're installing the gd graphics library, you must install gd-devel.

%prep
%setup -q
%patch0 -p1 -b .redhat

%build
make
gcc -shared -o libgd.so.%{version} -Wl,-soname=libgd.so.%{shlibver} \
	`ar t libgd.a` -L/usr/X11R6/lib -lttf -ljpeg -lpng -lz -lm

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_includedir},%{_libdir}}
make install \
	INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir} \
	INSTALL_INCLUDE=$RPM_BUILD_ROOT%{_includedir} \
	INSTALL_LIB=$RPM_BUILD_ROOT%{_libdir}
install -m 755 libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/
ln -s libgd.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libgd.so

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -fr $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc readme.txt index.html
%{_libdir}/*.so.*.*

%files progs
%defattr(-,root,root)
%{_bindir}/*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
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
