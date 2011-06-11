%define name trophy
%define version 1.1.6
%define release %mkrel 1
%define Summary A 2D car racing action game for Linux

Name: %{name}
Summary: %{Summary}
Version: %{version}
Release: %{release}
Source: http://heanet.dl.sourceforge.net/sourceforge/trophy/%{name}-%{version}.tar.gz
Source1: trophy-designer-manual.tar.bz2
Source10: %{name}.16.png
Source11: %{name}.32.png
Source12: %{name}.48.png
# patch from upstream, according to https://qa.mandriva.com/show_bug.cgi?id=49361#c8
Patch1: trophy-1.1.5-fix_crash.diff
URL: http://trophy.sourceforge.net/index.php3
License: GPL
Group: Games/Arcade
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clanlib0.8-devel	libclanlib-network libclanlib-sound libhermes-devel
# (gc) needed because of binary incompatibility of datafiles between versions of clanlib

%description
Trophy is a single-player racing game for Linux. Even though the goal is
basically to finish the laps as the first, Trophy is an action game which
offers much more than just a race. Lots of extras enable "unusual" features for
races such as shooting, putting mines and many others.

%prep
%setup -q -n %{name}-%{version} -a 1
%patch1 -p0

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
#export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf "$RPM_BUILD_ROOT"

%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Trophy
Comment=Trophy is a 2D car racing action game for Linux
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF


install -m644 %{SOURCE10} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README designer_manual_en
%{_gamesbindir}/*
%{_gamesdatadir}/trophy
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
