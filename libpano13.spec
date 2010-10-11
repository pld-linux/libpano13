#
# Conditional build:
%bcond_with	java	# build with Java Native Interface
#
Summary:	Panorama Tools library
Summary(pl.UTF-8):	Panorama Tools - biblioteka do obróbki panoram
Name:		libpano13
Version:	2.9.17
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/panotools/%{name}-%{version}.tar.gz
# Source0-md5:	54ec7c505cf38521f2fbb6e2acd2c433
URL:		http://panotools.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Panorama Tools library.
%{!?with_java:Note: this version does not provide Java interface!}

%description -l pl.UTF-8
Panorama Tools - biblioteka do obróbki panoram.
%{!?with_java:Uwaga: ta wersja nie dostarcza interfesju dla Javy!}

%package devel
Summary:	Header files for Panorama Tools library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Panorama Tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel >= 6b
Requires:	libpng-devel
Requires:	libtiff-devel

%description devel
Header files for Panorama Tools library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Panorama Tools.

%package static
Summary:	Static Panorama Tools library
Summary(pl.UTF-8):	Statyczna biblioteka Panorama Tools
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Panorama Tools library.

%description static -l pl.UTF-8
Statyczna biblioteka Panorama Tools.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	%{?with_java:--with-java=/usr/%{_lib}/java}%{!?with_java:--without-java}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README.linux doc/*.txt
%attr(755,root,root) %{_bindir}/PTblender
%attr(755,root,root) %{_bindir}/PTcrop
%attr(755,root,root) %{_bindir}/PTinfo
%attr(755,root,root) %{_bindir}/PTmasker
%attr(755,root,root) %{_bindir}/PTmender
%attr(755,root,root) %{_bindir}/PToptimizer
%attr(755,root,root) %{_bindir}/PTroller
%attr(755,root,root) %{_bindir}/PTtiff2psd
%attr(755,root,root) %{_bindir}/PTtiffdump
%attr(755,root,root) %{_bindir}/PTuncrop
%attr(755,root,root) %{_bindir}/panoinfo
%attr(755,root,root) %{_libdir}/libpano13.so.*
%{_mandir}/man1/panoinfo.1.*
%{_mandir}/man1/PTAInterpolate.1.*
%{_mandir}/man1/PTblender.1.*
%{_mandir}/man1/PTcrop.1.*
%{_mandir}/man1/PTinfo.1.*
%{_mandir}/man1/PTmasker.1.*
%{_mandir}/man1/PTmender.1.*
%{_mandir}/man1/PToptimizer.1.*
%{_mandir}/man1/PTroller.1.*
%{_mandir}/man1/PTtiff2psd.1.*
%{_mandir}/man1/PTtiffdump.1.*
%{_mandir}/man1/PTuncrop.1.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpano13.so
%{_libdir}/libpano13.la
%{_includedir}/pano13
%{_pkgconfigdir}/libpano13.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libpano13.a
