%define version 0.16.6
%define release %mkrel 3

Name:		sitecopy
Version:	%{version}
Release:	%{release}
Summary:	Tool for easily maintaining remote web sites
License:	GPL
Group:		Networking/File transfer
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	http://www.lyra.org/sitecopy/sitecopy-%{version}.tar.bz2
Source1:	%{name}.bash-completion
Patch0:		configure-0.16.6.patch
URL:		http://www.lyra.org/sitecopy/
BuildRequires:	neon-devel

%description
sitecopy allows you to easily maintain remote Web sites.  The program
will upload files to the server which have changed locally, and delete
files from the server which have been removed locally, to keep the
remote site synchronized with the local site, with a single
command. sitecopy will also optionally try to spot files you move
locally, and move them remotely.  FTP and WebDAV servers are
supported.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%optflags -fPIE"
export LDFLAGS="%ldflags -pie"
%configure2_5x \
	--enable-debug \
	--with-ssl \
	--with-neon \
	--disable-rsh
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

# (sb) remove fr man pages
rm -fr $RPM_BUILD_ROOT/%{_mandir}/fr

# fix doc file permissions
chmod 0644 COPYING ChangeLog INSTALL NEWS README* THANKS TODO

# (sb) installed but unpackaged files
rm -fr $RPM_BUILD_ROOT/%{_prefix}/doc

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/sitecopy
%{_mandir}/man1/*
%{_prefix}/share/sitecopy
%doc COPYING ChangeLog INSTALL NEWS README* THANKS TODO
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.16.6-3mdv2011.0
+ Revision: 614893
- the mass rebuild of 2010.1 packages

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 0.16.6-2mdv2010.1
+ Revision: 534176
- add fedora patch to build with system neon

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.16.6-2mdv2010.0
+ Revision: 445129
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 0.16.6-1mdv2009.1
+ Revision: 333006
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.16.3-4mdv2009.0
+ Revision: 260734
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.16.3-3mdv2009.0
+ Revision: 252482
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.16.3-1mdv2008.1
+ Revision: 127298
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import sitecopy


* Mon Mar 13 2006 Lenny Cartier <lenny@mandriva.com> 0.16.3-1mdk
- 0.16.3

* Fri Sep 30 2005 Lenny Cartier <lenny@mandriva.com> 0.16.1-1mdk
- 0.16.1

* Mon Sep 12 2005 Stew Benedict <sbenedict@mandriva.com> 0.16.0-1mdk
- 0.16.0
- drop French man page (S2, provided by man-pages-fr, #18475)

* Thu Jun 09 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.15.1-2mdk
- Rebuild for libkrb53-devel 1.4.1

* Mon May 02 2005 Stew Benedict <sbenedict@mandriva.com> 0.15.1-1mdk
- New release 0.15.1

* Mon Mar 07 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.15.0-1mdk
- 0.15.0

* Fri Mar 12 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.13.4-5mdk
- add French man page from Nicolas Girard

* Fri Jan 30 2004 Stew Benedict <sbenedict@mandrakesoft.com> 0.13.4-4mdk
- remove file specific BuildRequires (unresolved dependencies in distro)

* Sat Jan 17 2004 Abel Cheung <deaddog@deaddog.org> 0.13.4-3mdk
- Remove bash-completion dependency
- configure2_5x
- Fix BuildRequires
- Really link against openssl

* Tue Dec 30 2003 Guillaume Rousse <guillomovitch@mandrake.org> 0.13.4-2mdk
- added bash-completion

* Thu Dec 11 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.13.4-1mdk
- 0.13.4

* Wed Jul  2 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.13.3-1mdk
- 0.13.3

* Thu May 22 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.13.0-1mdk
- 0.13.0

* Mon Apr 28 2003 Stew Benedict <sbenedict@mandrakesoft.com> 0.12.1-1mdk
- 0.12.1, BuildRequires, drop xsitecopy - pretty broken 

* Mon Dec 30 2002 Stew Benedict <sbenedict@mandrakesoft.com> 0.11.4-2mdk
- rebuild for new glibc/rpm

* Sun Jul 14 2002 Roger <roger@linuxfreemail.com> 0.11.4-1mdk
- ok. i'm stumped. (didn't know a cvs existed) rebuilt for 0.11.4 release.
- now builds both sitecopy/xsitecopy
- fix BuildRoot, s/Copyright/License/, rpmlint fixes (sb)

* Tue Jul  2 2002 Stew Benedict <sbenedict@mandrakesoft.com> 0.11.4-0.20020206.1mdk
- first Mandrake release

