%define name trophy
%define version 1.1.3
%define release %mkrel 8
%define Summary Trophy is a 2D car racing action game for Linux.

Name: %{name}
Summary: %{Summary}
Version: %{version}
Release: %{release}
Source: http://heanet.dl.sourceforge.net/sourceforge/trophy/%{name}-%{version}-src.tar.bz2
Source1: trophy-designer-manual.tar.bz2
Source10: %{name}.16.png
Source11: %{name}.32.png
Source12: %{name}.48.png
Patch:    %{name}.gcc34.diff.bz2 
URL: http://trophy.sourceforge.net/index.php3
License: GPL
Group: Games/Arcade
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clanlib0.6-devel	libclanlib-network libclanlib-sound libhermes-devel
# (gc) needed because of binary incompatibility of datafiles between versions of clanlib
Requires: clanlib0.6 = 0.6.5

%description
Trophy is a single-player racing game for Linux. Even though the goal is
basically to finish the laps as the first, Trophy is an action game which
offers much more than just a race. Lots of extras enable "unusual" features for
races such as shooting, putting mines and many others.

%prep
%setup -q -n %{name}-%{version}-src -a 1
%patch
rm -rf `find -type d -name CVS`

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
cd trophy
autoconf
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p $RPM_BUILD_ROOT/%{_gamesbindir}
cp trophy/trophy $RPM_BUILD_ROOT/%{_gamesbindir}/trophy.real
cat > $RPM_BUILD_ROOT/%{_gamesbindir}/trophy << EOF
#!/bin/sh
pushd %{_gamesdatadir}/trophy
%{_gamesbindir}/trophy.real \$*
popd
EOF
chmod a+x $RPM_BUILD_ROOT/%{_gamesbindir}/trophy
mkdir -p $RPM_BUILD_ROOT/%{_gamesdatadir}/trophy
cp -a trophy/resources* $RPM_BUILD_ROOT/%{_gamesdatadir}/trophy

mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="Amusement/Arcade" title="Trophy" \
  longtitle="%{Summary}" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Trophy
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
Encoding=UTF-8
EOF


install -m644 %{SOURCE10} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README designer_manual_en
%{_gamesbindir}/*
%{_gamesdatadir}/trophy
%{_datadir}/applications/mandriva-%{name}.desktop
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
