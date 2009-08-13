Summary: Text based document generation
Name: asciidoc
Version: 8.4.5
Release: 3%{?dist}
# The python code does not specify a version.
# The javascript example code is GPLv2+.
License: GPL+ and GPLv2+
Group: Applications/System
URL: http://www.methods.co.nz/asciidoc/
Source0: http://www.methods.co.nz/asciidoc/%{name}-%{version}.tar.gz
# http://groups.google.com/group/asciidoc/browse_thread/thread/7f7a633c5b11ddc3
Patch0: asciidoc-8.4.5-datadir.patch
# https://bugzilla.redhat.com/506953
Patch1: asciidoc-8.4.5-use-unsafe-mode-by-default.patch
Requires: python >= 2.3
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
AsciiDoc is a text document format for writing short documents,
articles, books and UNIX man pages. AsciiDoc files can be translated
to HTML and DocBook markups using the asciidoc(1) command.

%prep
%setup -q
%patch0 -p1 -b .datadir
%patch1 -p1 -b .use-unsafe-mode-by-default

# Fix line endings on COPYRIGHT file
sed -i "s/\r//g" COPYRIGHT

# Convert CHANGELOG and README to utf-8
for file in CHANGELOG README; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done

%build

%install
rm -rf %{buildroot}
# make directory structure
%{__install} -d							\
	%{buildroot}%{_sysconfdir}/asciidoc/filters/code	\
	%{buildroot}%{_sysconfdir}/asciidoc/filters/graphviz	\
	%{buildroot}%{_sysconfdir}/asciidoc/filters/music	\
	%{buildroot}%{_sysconfdir}/asciidoc/filters/source	\
	%{buildroot}%{_datadir}/asciidoc/docbook-xsl		\
	%{buildroot}%{_datadir}/asciidoc/stylesheets		\
	%{buildroot}%{_datadir}/asciidoc/javascripts		\
	%{buildroot}%{_datadir}/asciidoc/images/icons/callouts	\
	%{buildroot}%{_datadir}/asciidoc/filters/code		\
	%{buildroot}%{_datadir}/asciidoc/filters/graphviz	\
	%{buildroot}%{_datadir}/asciidoc/filters/music		\
	%{buildroot}%{_bindir}					\
	%{buildroot}%{_mandir}/man1

# real conf data goes to sysconfdir, rest goes to datadir
%{__install} -m 0644 *.conf %{buildroot}%{_sysconfdir}/asciidoc
for filter in code graphviz music source ; do
	%{__install} -p -m 0644 filters/$filter/*.conf \
	%{buildroot}%{_sysconfdir}/asciidoc/filters/$filter/
done

# filter scripts
for filter in code graphviz music ; do
	%{__install} -p -m 0755 filters/$filter/*.py \
	%{buildroot}%{_datadir}/asciidoc/filters/$filter/
done

# symlinks so asciidoc works
ln -s %{_datadir}/asciidoc/docbook-xsl %{buildroot}%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/stylesheets %{buildroot}%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/javascripts %{buildroot}%{_sysconfdir}/asciidoc/
ln -s %{_datadir}/asciidoc/images %{buildroot}%{_sysconfdir}/asciidoc/

# binaries
%{__install} -p asciidoc.py %{buildroot}%{_bindir}/asciidoc
%{__install} -p a2x %{buildroot}%{_bindir}/

# manpages
%{__install} -m 0644 doc/*.1  %{buildroot}%{_mandir}/man1

# ancillary data
%{__install} -p -m 0644 docbook-xsl/*.xsl %{buildroot}%{_datadir}/asciidoc/docbook-xsl
%{__install} -p -m 0644 stylesheets/*.css %{buildroot}%{_datadir}/asciidoc/stylesheets/
%{__install} -p -m 0644 javascripts/*.js %{buildroot}%{_datadir}/asciidoc/javascripts
%{__install} -p -m 0644 images/icons/callouts/* %{buildroot}%{_datadir}/asciidoc/images/icons/callouts
%{__install} -p -m 0644 images/icons/{README,*.png} %{buildroot}%{_datadir}/asciidoc/images/icons

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%config(noreplace) %{_sysconfdir}/asciidoc
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/asciidoc/
%doc README BUGS CHANGELOG COPYRIGHT

%changelog
* Thu Aug 13 2009 Todd Zullinger <tmz@pobox.com> - 8.4.5-3
- Use 'unsafe' mode by default (bug 506953)
- Install filter scripts in %%{_datadir}/asciidoc
- Convert spec file, CHANGELOG, and README to utf-8
- Preserve timestamps on installed files, where feasible
- s/$RPM_BUILD_ROOT/%%{buildroot} and drop duplicated /'s
- Fix rpmlint mixed-use-of-spaces-and-tabs and end-of-line-encoding warnings

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

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
