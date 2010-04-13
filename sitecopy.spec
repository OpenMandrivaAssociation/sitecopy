%define version 0.16.6
%define release %mkrel 2

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

