Summary: Text based document generation
Name: asciidoc
Version: 8.4.5
Release: 1%{?dist}
# The python code does not specify a version.
# The javascript example code is GPLv2+.
License: GPL+ and GPLv2+
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
# make directory structure
%{__install} -d $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/code	\
        -d $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/music	\
        -d $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/source	\
        -d $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/graphviz	\
	$RPM_BUILD_ROOT/%{_datadir}/asciidoc/docbook-xsl		\
	$RPM_BUILD_ROOT/%{_datadir}/asciidoc/stylesheets		\
	$RPM_BUILD_ROOT/%{_datadir}/asciidoc/javascripts		\
	$RPM_BUILD_ROOT/%{_datadir}/asciidoc/images/icons/callouts	\
	$RPM_BUILD_ROOT/%{_bindir}					\
	$RPM_BUILD_ROOT/%{_mandir}/man1

# real conf data goes to sysconfdir, rest goes to datadir
%{__install} -m 0644 *.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc
%{__install} -m 0644 filters/code/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/code/
%{__install} -m 0644 filters/music/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/music/
%{__install} -m 0644 filters/source/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/source/
%{__install} -m 0644 filters/graphviz/*.conf $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/graphviz/
%{__install} filters/code/*.py $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/code/
%{__install} filters/music/*.py $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/music/
%{__install} filters/graphviz/*.py $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/filters/graphviz/

# symlinks so asciidoc works
ln -s %{_datadir}/asciidoc/docbook-xsl $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/stylesheets $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/javascripts $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/images $RPM_BUILD_ROOT/%{_sysconfdir}/asciidoc/

# binaries
%{__install} asciidoc.py $RPM_BUILD_ROOT/%{_bindir}/asciidoc
%{__install} a2x $RPM_BUILD_ROOT/%{_bindir}/

# manpages
%{__install} -m 0644 doc/*.1  $RPM_BUILD_ROOT/%{_mandir}/man1

# ancillary data
%{__install} -m 0644 docbook-xsl/*.xsl $RPM_BUILD_ROOT/%{_datadir}/asciidoc/docbook-xsl
%{__install} -m 0644 stylesheets/*.css $RPM_BUILD_ROOT/%{_datadir}/asciidoc/stylesheets/
%{__install} -m 0644 javascripts/*.js $RPM_BUILD_ROOT/%{_datadir}/asciidoc/javascripts
%{__install} -m 0644 images/icons/callouts/* $RPM_BUILD_ROOT/%{_datadir}/asciidoc/images/icons/callouts
%{__install} -m 0644 images/icons/{README,*.png} $RPM_BUILD_ROOT/%{_datadir}/asciidoc/images/icons

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_sysconfdir}/asciidoc
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/asciidoc/
%doc README BUGS CHANGELOG COPYRIGHT

%changelog
* Fri Jun 19 2009 Dave Airlie <airlied@redhat.com> 8.4.5-1
- new upstream version 8.4.5 - required by X.org libXi to build

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 8.2.5-3
- fix license tag

* Wed Dec 05 2007 Florian La Roche <laroche@redhat.com> - 8.2.5-2
- remove doc/examples from filelist due to dangling symlinks

* Tue Nov 20 2007 Florian La Roche <laroche@redhat.com> - 8.2.5-1
- new upstream version 8.2.5

* Mon Oct 22 2007 Florian La Roche <laroche@redhat.com> - 8.2.3-1
- new upstream version 8.2.3

* Sat Sep 01 2007 Florian La Roche <laroche@redhat.com> - 8.2.2-1
- new upstream version 8.2.2

* Mon Mar 19 2007 Chris Wright <chrisw@redhat.com> - 8.1.0-1
- update to asciidoc 8.1.0

* Thu Sep 14 2006 Chris Wright <chrisw@redhat.com> - 7.0.2-3
- rebuild for Fedora Extras 6

* Tue Feb 28 2006 Chris Wright <chrisw@redhat.com> - 7.0.2-2
- rebuild for Fedora Extras 5

* Mon Aug 29 2005 Chris Wright <chrisw@osdl.org> - 7.0.2-1
- convert spec file to UTF-8
- Source should be URL
- update to 7.0.2

* Fri Aug 19 2005 Chris Wright <chrisw@osdl.org> - 7.0.1-3
- consistent use of RPM_BUILD_ROOT

* Thu Aug 18 2005 Chris Wright <chrisw@osdl.org> - 7.0.1-2
- Update BuildRoot
- use _datadir
- use config and _sysconfdir

* Wed Jun 29 2005 Terje RÃ¸sten <terje.rosten@ntnu.no> - 7.0.1-1
- 7.0.1
- Drop patch now upstream
- Build as noarch (Petr KlÃ­ma)

* Sat Jun 11 2005 Terje RÃ¸sten <terje.rosten@ntnu.no> - 7.0.0-0.3
- Add include patch 

* Fri Jun 10 2005 Terje RÃ¸sten <terje.rosten@ntnu.no> - 7.0.0-0.2
- Fix stylesheets according to Stuart

* Fri Jun 10 2005 Terje RÃ¸sten <terje.rosten@ntnu.no> - 7.0.0-0.1
- Initial package
- Based on Debian package, thx!


