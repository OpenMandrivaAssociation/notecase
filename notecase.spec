%define Werror_cflags %nil

Name: 	 	notecase
Summary: 	A hierarchical text notes manager
Version: 	1.9.8
Release: 	5

Source:		http://kent.dl.sourceforge.net/sourceforge/notecase/%{name}-%{version}_src.tar.gz
URL:		http://notecase.sourceforge.net/
License:	BSD
Group:		Office
BuildRequires:	pkgconfig
BuildRequires:	imagemagick
BuildRequires:	gtk2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gtksourceview-devel
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Patch0: notecase-1.9.8-gtksourceview.patch
Patch1: notecase-1.9.8-gcc44.patch
Patch2: notecase-1.9.8-Makefile-X11.patch

%description
NoteCase is a hierarchical text notes manager (AKA outliner).

It helps you organize your everyday text notes into a single document with
individual notes placed into a tree-like structure. To ensure your privacy
an encrypted document format is supported along with a standard unencrypted
one.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0


%build
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

#menu
desktop-file-install --vendor="" \
  --add-category="GTK" \
  --remove-key='Encoding' \
  --remove-key='Office' \
  --remove-key='Version' \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 res/%name.xpm %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 res/%name.xpm %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 res/%name.xpm %{buildroot}/%_miconsdir/%name.png

%find_lang %name

%files -f %{name}.lang
%defattr(-,root,root)
%doc readme.txt docs/help.ncd

%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png


%changelog
* Wed May 23 2012 Eugene Budanov <eugene.budanov@rosalab.ru> 1.9.8-1rosa2012lts
- Spec file was cleaned. Deleted contructions for old Mandriva releases
- Added patch from Gentoo for build with new gtksourceview versions
- Added patch from Gentoo for build with gcc4.4+

* Tue Dec 09 2008 Funda Wang <fundawang@mandriva.org> 1.9.8-1mdv2009.1
+ Revision: 312226
- BR gtksourceview
- update to new version 1.9.8

* Tue Oct 28 2008 Funda Wang <fundawang@mandriva.org> 1.9.7-1mdv2009.1
+ Revision: 298099
- New version 1.9.7

* Mon Aug 25 2008 Funda Wang <fundawang@mandriva.org> 1.9.5-1mdv2009.0
+ Revision: 275729
- New version 1.9.5

* Sun Jun 29 2008 Funda Wang <fundawang@mandriva.org> 1.9.3-1mdv2009.0
+ Revision: 229943
- update to new version 1.9.3

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - normalize call to %%update_mime_database/%%clean_mime_database: don't be overly cautious

* Fri May 23 2008 Funda Wang <fundawang@mandriva.org> 1.9.1-1mdv2009.0
+ Revision: 210370
- fix license
- New version 1.9.1

* Fri Feb 08 2008 Funda Wang <fundawang@mandriva.org> 1.7.9-1mdv2008.1
+ Revision: 163887
- update to new version 1.7.9

* Thu Jan 24 2008 Olivier Thauvin <nanardon@mandriva.org> 1.7.6-1mdv2008.1
+ Revision: 157288
- 1.7.6

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Funda Wang <fundawang@mandriva.org> 1.6.6-1mdv2008.0
+ Revision: 79903
- New version 1.6.6

* Wed Jun 13 2007 Austin Acton <austin@mandriva.org> 1.5.6-2mdv2008.0
+ Revision: 38880
- fix for non-versioned docdir while allowing backports

* Wed Jun 13 2007 Austin Acton <austin@mandriva.org> 1.5.6-1mdv2008.0
+ Revision: 38752
- buildrequires gnome-vfs
- buildrequires desktop-file-utils
- new version (new era really)
- XDG menu
- png icon
- mkrel


* Wed Jul 20 2005 Austin Acton <austin@mandriva.org> 1.0.0-1mdk
- New release 1.0.0

* Wed Jun 22 2005 Austin Acton <austin@mandriva.org> 0.9.3-1mdk
- New release 0.9.3

* Mon May 30 2005 Austin Acton <austin@mandriva.org> 0.8.9-1mdk
- New release 0.8.9

* Tue May 10 2005 Austin Acton <austin@mandriva.org> 0.8.7-1mdk
- New release 0.8.7

* Thu Mar 31 2005 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- initial package

