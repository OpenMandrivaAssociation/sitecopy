%define version 0.16.3
%define release %mkrel 1

Name:		sitecopy
Version:	%{version}
Release:	%{release}
Summary:	Tool for easily maintaining remote web sites
License:	GPL
Group:		Networking/File transfer
Source0:	http://www.lyra.org/sitecopy/sitecopy-%{version}.tar.bz2
Source1:	%{name}.bash-completion.bz2
URL:		http://www.lyra.org/sitecopy/
BuildRequires:	openssl-devel
BuildRequires:	krb5-devel

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
bzcat %{SOURCE1} > %{name}.bash-completion

%build
# vanilla sitecopy.
mkdir sitecopy; cd sitecopy

CONFIGURE_TOP=.. %configure2_5x \
	--enable-debug \
	--with-ssl \
	--with-included-expat \
	--with-included-neon \
	--disable-rsh
%make

%install
rm -rf $RPM_BUILD_ROOT
pushd sitecopy
%makeinstall_std
popd

%find_lang %{name}

# (sb) remove fr man pages
rm -fr $RPM_BUILD_ROOT/%{_mandir}/fr

# fix doc file permissions
chmod 0644 COPYING ChangeLog INSTALL NEWS README* THANKS TODO

# (sb) installed but unpackaged files
rm -fr $RPM_BUILD_ROOT/%{_prefix}/doc

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d
install -m 644 %{name}.bash-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/sitecopy
%{_mandir}/man1/*
%{_prefix}/share/sitecopy
%doc COPYING ChangeLog INSTALL NEWS README* THANKS TODO
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}

