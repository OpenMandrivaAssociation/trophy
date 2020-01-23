%define name trophy
%define version 2.0.4
%define release 1
%define Summary A 2D car racing action game for Linux

Name: %{name}
Summary: %{Summary}
Version: %{version}
Release: %{release}
Source: http://downloads.sourceforge.net/trophy/%{name}-%{version}.tar.gz
Source1: trophy-designer-manual.tar.bz2
Source10: %{name}.16.png
Source11: %{name}.32.png
Source12: %{name}.48.png
# patch from upstream, according to https://qa.mandriva.com/show_bug.cgi?id=49361#c8
#Patch1: trophy-1.1.5-fix_crash.diff
URL: https://trophy.sourceforge.io/
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
%autopatch -p1

%build
# (gc) workaround g++ exception bug when -fomit-frame-pointer is set
#export CFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer" CXXFLAGS="$RPM_OPT_FLAGS -fno-omit-frame-pointer"
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make_build

%install
rm -rf "$RPM_BUILD_ROOT"

%make_install

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


%changelog
* Sat Jun 11 2011 Funda Wang <fwang@mandriva.org> 1.1.6-1mdv2011.0
+ Revision: 684274
- new version 1.1.6

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.1.5-7mdv2010.0
+ Revision: 445560
- rebuild

* Tue Apr 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.5-6mdv2009.1
+ Revision: 366873
- rpmdrake compliant summary

* Mon Apr 13 2009 Michael Scherer <misc@mandriva.org> 1.1.5-5mdv2009.1
+ Revision: 366835
- add patch 1 from upstream, to fix #49361

* Mon Apr 13 2009 Michael Scherer <misc@mandriva.org> 1.1.5-4mdv2009.1
+ Revision: 366777
- fix summary
- rebuild for new gcc, fix 49361

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 1.1.5-1mdv2008.0
+ Revision: 72009
- clean spec, use standard install macro, drop old menu
- BR clanlib 0.8
- New version 1.1.5
- Import trophy



* Mon Aug 14 2006 Emmanuel Andry <eandry@mandriva.org> 1.1.3-8mdv2007.0
- %%mkrel
- xdg menu

* Mon May 08 2006 Stefan van der Eijk <stefan@eijk.nu> 1.1.3-7mdk
- rebuild for sparc

* Mon Aug 16 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1.3-6mdk
- Rebuild with new menu

* Tue Jul 13 2004 Michael Scherer <misc@mandrake.org> 1.1.3-5mdk
- really fix #10164 

* Mon Jun 28 2004 Michael Scherer <misc@mandrake.org> 1.1.3-4mdk 
- fix #10164, thanks to <luizd@ig.com.br>
- remove Packager tag
- rebuild for new clanlib
- patch for gcc3.4

* Tue Sep  2 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.3-3mdk
- fix deps for 64bit build

* Fri Jul 25 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.1.3-2mdk
- rebuild
- change summary macro to avoid possible conflicts if we were to build debug package
- convert icons to png format
- drop Prefix tag
- use %%make macro

* Wed May 28 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.3-1mdk
- new release

* Mon Jan 20 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.1-1mdk
- take good work from Crispin Boylan <viewtronix@uklinux.net>
  - New version 1.1.1

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.6-10mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Mon Jul 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.6-9mdk
- Remove NO_XALF from menu entry

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0.6-8mdk
- Automated rebuild with gcc3.2

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-7mdk
- recompile against latest libstdc++ and latest clanlib

* Sat Jan 19 2002 Stefan van der Eijk <stefan@eijk.nu> 1.0.6-6mdk
- BuildRequires

* Mon Nov 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-5mdk
- recompile against clanlib-0.5.1 (binary datafiles are not compatible
  with 0.5.0)

* Tue Oct 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-4mdk
- fix obsolete-tag Copyright

* Tue Sep 11 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-3mdk
- use absolute path in script to prevent from PATH's without /usr/games

* Mon Sep 10 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-2mdk
- don't use launch_x11_clanapp anymore (cl 0.5)

* Tue Jun 26 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-1mdk
- trophy 1.0.6 that is (really) compliant with ClanLib 0.5

* Tue May  1 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.2-1mdk
- trophy 1.0.2 that is compliant with ClanLib 0.5

* Thu Apr 12 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 1.0.1-9mdk
- Correct GNOME menu entry

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-8mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Fri Feb 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-7mdk
- add 48x48 icon
- add designal manual
- fix requires on launch_x11_clanapp

* Fri Dec  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-6mdk
- fix BuildRequires

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-5mdk
- recompile against newest libstdc++
- against lowercased hermes and clanlib

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-4mdk
- menu: now launches automatically the x11 target

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-3mdk
- automatically added packager tag

* Wed Aug 16 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- really work (forgot support for PKGDATADIR in some places, forgot
  some data)

* Wed Aug 16 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-1mdk
- first mdk package. thanks to alix.
