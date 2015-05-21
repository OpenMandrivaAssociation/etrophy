
%define major 0
%define libname %mklibname etrophy %{major}
%define devname %mklibname etrophy -d
%define gitdate 20150521


Summary: 	ETrophy is a library that manages scores, trophies and unlockables
Name: 		etrophy
Version: 	0.5.1.%{gitdate}
Release: 	0.1
License:	BSD
Group: 		System/Libraries
Source: 	%{name}-%{gitdate}.tar.xz
Source100:	%{name}.rpmlintrc
URL: 		https://git.enlightenment.org/games/efbb.git

BuildRequires:	pkgconfig(efl) 
BuildRequires:	pkgconfig(ecore)
BuildRequires:	pkgconfig(elementary)
Requires: 	efl
Requires:	ecore

%description
ETrophy is a library that manages scores, trophies and unlockables. It will
store them and provide views to display them. Could be used by games based
on EFL.

%package -n %{libname}
Summary:	Libraries for the %{name} project
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_libdir}/*.so.*
%{_datadir}/etrophy/*

%package -n %{devname}
Summary:	Etrophy headers, static libraries, documentation and test programs
Group:		System/Libraries
Requires:	 %{libname} = %{EVRD}
Provides:       %{name}-devel = %{EVRD}

%description -n %{devname}
%{name} development headers and libraries

%files -n %{devname}
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/
%{_localedir}/*/LC_MESSAGES/%{name}.mo

%prep
%setup -qn %{name}-%{gitdate}

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
