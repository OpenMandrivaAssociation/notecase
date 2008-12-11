%define name	notecase
%define version 1.9.8
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A hierarchical text notes manager
Version: 	%{version}
Release: 	%{release}

Source:		http://kent.dl.sourceforge.net/sourceforge/notecase/%{name}-%{version}_src.tar.gz
URL:		http://notecase.sourceforge.net/
License:	BSD
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig imagemagick
BuildRequires:	gtk2-devel libgnome-vfs2-devel
BuildRequires:	desktop-file-utils gtksourceview-devel
Requires(post): shared-mime-info
Requires(postun): shared-mime-info

%description
NoteCase is a hierarchical text notes manager (AKA outliner).

It helps you organize your everyday text notes into a single document with
individual notes placed into a tree-like structure. To ensure your privacy
an encrypted document format is supported along with a standard unencrypted
one.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
desktop-file-install --vendor="" \
  --add-category="GTK" \
  --remove-key='Encoding' \
  --remove-key='Office' \
  --remove-key='Version' \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 res/%name.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 res/%name.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 res/%name.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%update_mime_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_mime_database
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%if %mdkver < 200800
%doc readme.txt
%{_datadir}/doc/%name
%else
%doc readme.txt docs/help.ncd
%endif
%{_bindir}/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
