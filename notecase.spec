%define name	notecase
%define version 1.5.6
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	A hierarchical text notes manager
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}_src.tar.bz2
URL:		http://notecase.sourceforge.net/
License:	GPL
Group:		Office
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig ImageMagick
BuildRequires:	gtk2-devel unix2dos
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
%makeinstall

#menu
desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-Office-Accessories" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

perl -pi -e 's|.xpm|.png||g' %buildroot/%_datadir/applicaitons/*

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

%post
%update_menus
update-mime-database "%{_datadir}/mime/"		

%postun
%clean_menus
update-mime-database "%{_datadir}/mime/"

%files -f %{name}.lang
%defattr(-,root,root)
%doc readme.txt
%{_bindir}/%name
%{_datadir}/applications/*
#%{_datadir}/doc/%name
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

