Name:           libasyncns
Version:        0.8
Release:        1
License:        LGPL-2.1+
Summary:        A C library for executing name service queries asynchronously
URL:            http://0pointer.de/lennart/projects/libasyncns
Group:          System/Libraries
Source:         %{name}-%{version}.tar.gz
Source1001: 	libasyncns.manifest

%description
Libasyncns is a C library for executing name service queries
asynchronously. It is an asynchronous wrapper around getaddrinfo(3),
getnameinfo(3), res_query(3) and res_search(3) from libc and libresolv.

%package devel
Summary:        libasyncns development package
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Development package for libasyncns, a C library for executing name
service queries asynchronously. It is an asynchronous wrapper around
getaddrinfo(3), getnameinfo(3), res_query(3) and res_search(3) from libc
and libresolv.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure

make %{?_smp_mflags}

%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest %{name}.manifest
%{_libdir}/libasyncns.so.*

%files devel
%manifest %{name}.manifest
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc
