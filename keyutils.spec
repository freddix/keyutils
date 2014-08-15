Summary:	Linux Key Management Utilities
Name:		keyutils
Version:	1.5.9
Release:	2
License:	LGPL v2+ (library), GPL v2+ (utility)
Group:		Base
Source0:	http://people.redhat.com/~dhowells/keyutils/%{name}-%{version}.tar.bz2
# Source0-md5:	7f8ac985c45086b5fbcd12cecd23cf07
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to control the kernel key management facility and to provide
a mechanism by which the kernel call back to userspace to get a key
instantiated.

%package libs
Summary:	Key utilities library
License:	LGPL v2+
Group:		Libraries

%description libs
This package provides a wrapper library for the key management
facility system calls.

%package devel
Summary:	Development package for building Linux key management utilities
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package provides the header files for building key utilities.

%prep
%setup -q

%build
%{__make} -j1 \
	CC="%{__cc}"			\
	CFLAGS="-Wall %{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"		\
	BINDIR=%{_bindir}		\
	SBINDIR=%{_sbindir}		\
	LIBDIR=%{_libdir}		\
	USRLIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT	\
	BINDIR=%{_bindir}	\
	SBINDIR=%{_sbindir}	\
	LIBDIR=%{_libdir}	\
	USRLIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/keyctl
%attr(755,root,root) %{_sbindir}/request-key
%attr(755,root,root) %{_sbindir}/key.dns_resolver
%dir %{_datadir}/keyutils
%attr(755,root,root) %{_datadir}/keyutils/*.sh
%{_mandir}/man1/keyctl.1*
%{_mandir}/man5/request-key.conf.5*
%{_mandir}/man8/key.dns_resolver.8*
%{_mandir}/man8/request-key.8*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/request-key.conf

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkeyutils.so.?
%attr(755,root,root) %{_libdir}/libkeyutils.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkeyutils.so
%{_includedir}/keyutils.h
%{_mandir}/man3/keyctl_*.3*
%{_mandir}/man3/recursive_key_scan.3*
%{_mandir}/man3/recursive_session_key_scan.3*

