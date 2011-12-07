%define archivever 1.02rc1

Name: lzop
Version: 1.02
Release: 0.9.rc1%{?dist}

Summary: Real-time file compressor

Group: Applications/Archiving
License: GPLv2+
URL: http://www.%{name}.org/
Source: http://www.%{name}.org/download/%{name}-%{archivever}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: lzo-devel

%description
lzop is a compression utility which is designed to be a companion to gzip. It
is based on the LZO library and its main advantages over gzip are much higher
compression and decompression speed at the cost of compression ratio.

lzop was designed with reliability, speed, portibility and as a reasonable
drop-in compatiblity to gzip.

%prep
%setup -q -n %{name}-%{archivever}

%build
%configure
make %{?_smp_mflags}

%install
rm -fr %{buildroot}
%makeinstall

%clean
rm -fr %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING NEWS README THANKS ChangeLog
%doc %{_mandir}/man?/*
%attr(0755,root,root) %{_bindir}/*

%changelog
* Tue Mar 02 2010 Kamil Dudka <kdudka@redhat.com> - 1.02-0.9.rc1
- license changed to GPLv2+
- added -q option to %%setup

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.02-0.8.rc1.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.02-0.8.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 1.02-0.7.rc1
- Rebuild against gcc 4.4 and rpm 4.6

* Tue Sep 18 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.6.rc1
- gcc 4.3 rebuild

* Tue Sep 18 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.5.rc1
- License fix

* Sat Sep 02 2006  Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.4.rc1
- FE6 Rebuild

* Sun Jul 30 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.3.rc1
- use new alphatag convention
- build with lzop 2 at last

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.2
- rebuilt for new gcc4.1 snapshot and glibc changes
- build with lzop 1 since lzop 2 hasn't been merged yet

* Thu Jan 19 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.02-0.1
- update to 1.02rc1
- build with lzop 2

* Wed Jan 18 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 1.01-4
- gcc 4.1 build time

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com>
- 1.01-3
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Apr 20 2004 Nicolas Mailhot <Nicolas.Mailhot at laPoste.net>
- 0:1.01-0.fdr.1
- Fedorization

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com>
- 1.01-1
- Initial package. (using DAR)
