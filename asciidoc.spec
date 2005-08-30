Summary: Text based document generation
Name: asciidoc
Version: 7.0.2
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.methods.co.nz/asciidoc/
Source0: http://www.methods.co.nz/asciidoc/%{name}-%{version}.tar.gz
Requires: python >= 2.3
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc(1) command.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters
%{__install} -d $RPM_BUILD_ROOT/%{_datadir}/asciidoc
%{__install} -d $RPM_BUILD_ROOT/%{_mandir}/man1

%{__install} -m 0644 *.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc
(cd $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc; ln -s ../../%{_datadir}/asciidoc/stylesheets .)
%{__install} -m 0644 filters/{code-filter.conf,code-filter.py} $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/
%{__install} -D -m 0755 asciidoc.py $RPM_BUILD_ROOT/%{_bindir}/asciidoc
%{__install} -m 0644 doc/asciidoc.1  $RPM_BUILD_ROOT/%{_mandir}/man1
%{__cp} -av images/ stylesheets/ $RPM_BUILD_ROOT/%{_datadir}/asciidoc/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_sysconfdir}/asciidoc
%{_bindir}/asciidoc
%{_mandir}/man1/*
%{_datadir}/asciidoc/
%doc README BUGS CHANGELOG COPYRIGHT doc examples

%changelog
* Mon Aug 29 2005 Josh Boyer <jwboyer@jdub.homelinux.org> - 7.0.2-1
- Update to latest version
- Fix remaining issues from review

* Fri Aug 19 2005 Chris Wright <chrisw@osdl.org> - 7.0.1-3
- consistent use of RPM_BUILD_ROOT

* Thu Aug 18 2005 Chris Wright <chrisw@osdl.org> - 7.0.1-2
- Update BuildRoot
- use _datadir
- use config and _sysconfdir

* Wed Jun 29 2005 Terje Røsten <terje.rosten@ntnu.no> - 7.0.1-1
- 7.0.1
- Drop patch now upstream
- Build as noarch (Petr Klíma)

* Sat Jun 11 2005 Terje Røsten <terje.rosten@ntnu.no> - 7.0.0-0.3
- Add include patch 

* Fri Jun 10 2005 Terje Røsten <terje.rosten@ntnu.no> - 7.0.0-0.2
- Fix stylesheets according to Stuart

* Fri Jun 10 2005 Terje Røsten <terje.rosten@ntnu.no> - 7.0.0-0.1
- Initial package
- Based on Debian package, thx!

