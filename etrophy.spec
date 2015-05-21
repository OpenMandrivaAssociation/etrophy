
%define major 0
%define libname %mklibname etrophy %{major}
%define devname %mklibname etrophy -d
%define gitdate 20150521


Summary: 	ETrophy is a library that manages scores, trophies and unlockables.
Name: 		etrophy
Version: 	0.5.1.0.%{gitdate}
Release: 	0.1
License:	 BSD
Group: 		System Environment/Libraries
Source: 	%{name}-%{gitdate}.tar.xz
URL: 		https://git.enlightenment.org/games/efbb.git

BuildRequires:	pkgconfig(efl) 
BuildRequires:	pkgconfig(ecore)
Requires: 	efl 
Requires:	ecore

%description
ETrophy is a library that manages scores, trophies and unlockables. It will
store them and provide views to display them. Could be used by games based
on EFL.

%package devname
Summary: Etrophy headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description devname
Headers, static libraries, test programs and documentation for Etrophy

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std


%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%{_datadir}/etrophy/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/*

