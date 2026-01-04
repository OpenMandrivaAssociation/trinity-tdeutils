%bcond clang 1
%bcond gamin 1
%bcond klaptopdaemon 1
%bcond xscreensaver 1
%bcond consolehelper 1
%bcond superkaramba 1
%bcond tdefilereplace 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_pkg tdeutils
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# Avoids relinking, which breaks consolehelper
%define dont_relink 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Summary:	TDE Utilities
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		Applications/System
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	klaptop_acpi_helper.pam
Source2:	klaptop_acpi_helper.console
Source3:	kcmlaptoprc
Source4:	%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DCONFIG_INSTALL_DIR=%{_sysconfdir}/trinity
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DWITH_DPMS=ON -DWITH_ASUS=ON -DWITH_POWERBOOK=OFF
BuildOption:    -DWITH_POWERBOOK2=OFF -DWITH_VAIO=ON
BuildOption:    -DWITH_THINKPAD=ON -DWITH_I8K=ON
BuildOption:    -DWITH_SNMP=ON -DWITH_SENSORS=ON -DWITH_XMMS=ON
BuildOption:    -DWITH_TDENEWSTUFF=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_XSCREENSAVER=%{!?with_xscreensaver:OFF}%{?with_xscreensaver:ON}
BuildOption:    -DBUILD_KLAPTOPDAEMON=%{?!with_klaptopdaemon:OFF}%{?with_klaptopdaemon:ON}
BuildOption:    -DBUILD_SUPERKARAMBA=%{?!with_superkaramba:OFF}%{?with_superkaramba:ON}
BuildOption:    -DBUILD_TDEFILEREPLACE=%{?!with_tdefilereplace:OFF}%{?with_tdefilereplace:ON}

Obsoletes:	trinity-kdeutils < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeutils = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdeutils-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeutils-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdeutils < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdeutils = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-filesystem >= %{tde_version}
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes

BuildRequires:	gettext
BuildRequires:	net-snmp-devel
BuildRequires:	gmp-devel

# PYTHON support
BuildRequires:  pkgconfig(python)

# XTST support
BuildRequires:  pkgconfig(xtst)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# PCRE2 support
BuildRequires:	pkgconfig(libpcre2-posix)


# ACL support
BuildRequires:	pkgconfig(libacl)

# XSCREENSAVER support
%{?with_xscreensaver:BuildRequires:  pkgconfig(xscrnsaver)}

BuildRequires:  pkgconfig(xrender)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

Requires: trinity-ark = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kcalc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kcharselect = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdelirc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdessh = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kdf = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kedit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kfloppy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kgpg = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-khexedit = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kjots = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_klaptopdaemon:Requires: trinity-klaptopdaemon = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-kmilo = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmilo-legacy = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kregexpeditor = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ksim = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-ktimer = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdewalletmanager = %{?epoch:%{epoch}:}%{version}-%{release}
%if %{with superkaramba}
Requires: trinity-superkaramba = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%if %{with tdefilereplace}
Requires: trinity-tdefilereplace = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description
Utilities for the Trinity Desktop Environment, including:
* ark (tar/gzip archive manager)
* kcalc (scientific calculator)
* kcharselect (character selector)
* tdelirc (infrared control)
* tdessh (ssh front end)
* kdf (view disk usage)
* kedit (simple text editor)
* kfloppy (floppy formatting tool)
* kgpg (gpg gui)
* khexedit (hex editor)
* kjots (note taker)
%if %{with klaptopdaemon}
* klaptopdaemon (battery monitoring and management for laptops);
%endif
* kmilo
* kregexpeditor (regular expression editor)
* ksim (system information monitor);
* ktimer (task scheduler)
* kwikdisk (removable media utility)
* tdefilereplace: batch search and replace tool

%files

##########

%package -n trinity-ark
Summary:	Graphical archiving tool for Trinity
Group:		Applications/Utilities
#Requires:	ncompress
Requires:	unzip
Requires:	zip
#Requires:	zoo
Requires:	bzip2
#Requires:	p7zip
#Requires:	xz
#Requires:	lzma
#Requires:	rar, unrar

%description -n trinity-ark
Ark is a graphical program for managing various archive formats within the
TDE environment. Archives can be viewed, extracted, created and modified
from within Ark.

The program can handle various formats such as tar, gzip, bzip2, zip, rar and
lha (if appropriate command-line programs are installed).

Ark can work closely with Konqueror in the TDE environment to handle archives,
if you install the Konqueror Integration plugin available in the konq-plugins
package.

%files -n trinity-ark
%defattr(-,root,root,-)
%{tde_prefix}/bin/ark
%{tde_prefix}/%{_lib}/trinity/ark.la
%{tde_prefix}/%{_lib}/trinity/ark.so
%{tde_prefix}/%{_lib}/trinity/libarkpart.la
%{tde_prefix}/%{_lib}/trinity/libarkpart.so
%{tde_prefix}/%{_lib}/libtdeinit_ark.so
%{tde_prefix}/share/applications/tde/ark.desktop
%{tde_prefix}/share/apps/ark/
%{tde_prefix}/share/config.kcfg/ark.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/ark.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/ark.svgz
%{tde_prefix}/share/services/ark_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/ark/
%{tde_prefix}/share/man/man1/ark.1*

##########

%package -n trinity-kcalc
Summary:	Calculator for Trinity
Group:		Applications/Utilities

%description -n trinity-kcalc
KCalc is TDE's scientific calculator.

It provides:
* trigonometric functions, logic operations, and statistical calculations
* easy cut and paste of numbers from/into its display
* a results-stack which lets you conveniently recall previous results
* configurable precision, and number of digits after the period

%files -n trinity-kcalc
%defattr(-,root,root,-)
%{tde_prefix}/bin/kcalc
%{tde_prefix}/%{_lib}/trinity/kcalc.la
%{tde_prefix}/%{_lib}/trinity/kcalc.so
%{tde_prefix}/%{_lib}/libtdeinit_kcalc.so
%{tde_prefix}/share/applications/tde/kcalc.desktop
%{tde_prefix}/share/apps/kcalc/
%{tde_prefix}/share/apps/tdeconf_update/kcalcrc.upd
%{tde_prefix}/share/config.kcfg/kcalc.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kcalc.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kcalc.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kcalc/
%{tde_prefix}/share/man/man1/kcalc.1*

##########

%package -n trinity-kcharselect
Summary:	Character selector for Trinity
Group:		Applications/Utilities
Requires:	trinity-kicker

%description -n trinity-kcharselect
This package contains kcharselect, a character set selector for TDE.

%files -n trinity-kcharselect
%defattr(-,root,root,-)
%{tde_prefix}/bin/kcharselect
%{tde_prefix}/%{_lib}/trinity/kcharselect_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kcharselect_panelapplet.so
%{tde_prefix}/share/applications/tde/KCharSelect.desktop
%{tde_prefix}/share/apps/kcharselect/
%{tde_prefix}/share/apps/tdeconf_update/kcharselect.upd
%{tde_prefix}/share/apps/kicker/applets/kcharselectapplet.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kcharselect.png
%{tde_prefix}/share/doc/tde/HTML/en/kcharselect/
%{tde_prefix}/share/man/man1/kcharselect.1*

##########

%package -n trinity-tdelirc
Summary:	Infrared control for Trinity
Group:		Applications/Utilities
Requires:	trinity-filesystem

Obsoletes:	trinity-kdelirc < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdelirc = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdelirc
This is a frontend for the LIRC suite to use infrared devices with TDE.

%files -n trinity-tdelirc
%defattr(-,root,root,-)
%{tde_prefix}/bin/irkick
%{tde_prefix}/%{_lib}/trinity/irkick.la
%{tde_prefix}/%{_lib}/trinity/irkick.so
%{tde_prefix}/%{_lib}/trinity/kcm_kcmlirc.la
%{tde_prefix}/%{_lib}/trinity/kcm_kcmlirc.so
%{tde_prefix}/%{_lib}/libtdeinit_irkick.so
%{tde_prefix}/share/applications/tde/irkick.desktop
%{tde_prefix}/share/applications/tde/kcmlirc.desktop
%{tde_prefix}/share/apps/irkick/
%{tde_prefix}/share/apps/profiles/tdelauncher.profile.xml
%{tde_prefix}/share/apps/profiles/konqueror.profile.xml
%{tde_prefix}/share/apps/profiles/noatun.profile.xml
%{tde_prefix}/share/apps/profiles/profile.dtd
%dir %{tde_prefix}/share/apps/remotes
%{tde_prefix}/share/apps/remotes/RM-0010.remote.xml
%{tde_prefix}/share/apps/remotes/cimr100.remote.xml
%{tde_prefix}/share/apps/remotes/hauppauge.remote.xml
%{tde_prefix}/share/apps/remotes/remote.dtd
%{tde_prefix}/share/apps/remotes/sherwood.remote.xml
%{tde_prefix}/share/apps/remotes/sonytv.remote.xml
%{tde_prefix}/share/autostart/irkick.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/irkick.png
%{tde_prefix}/share/icons/locolor/*/apps/irkick.png
%{tde_prefix}/share/doc/tde/HTML/en/irkick/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmlirc/

##########

%package -n trinity-tdessh
Summary:	Ssh frontend for Trinity
Group:		Applications/Utilities
%if 0%{?suse_version}
Requires:	openssh
%else
Requires:	openssh-clients
%endif

Obsoletes:	trinity-kdessh < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdessh = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdessh
This package contains TDE's frontend for ssh.

%files -n trinity-tdessh
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdessh

##########

%package -n trinity-kdf
Summary:	Disk space utility for Trinity
Group:		Applications/Utilities
Requires:	trinity-kcontrol

%description -n trinity-kdf
KDiskFree displays the available file devices (hard drive partitions, floppy
and CD drives, etc.) along with information on their capacity, free space, type
and mount point. It also allows you to mount and unmount drives and view them
in a file manager.

%files -n trinity-kdf
%defattr(-,root,root,-)
%{tde_prefix}/bin/kdf
%{tde_prefix}/bin/kwikdisk
%{tde_prefix}/%{_lib}/trinity/kcm_kdf.la
%{tde_prefix}/%{_lib}/trinity/kcm_kdf.so
%{tde_prefix}/share/applications/tde/kcmdf.desktop
%{tde_prefix}/share/applications/tde/kdf.desktop
%{tde_prefix}/share/applications/tde/kwikdisk.desktop
%{tde_prefix}/share/apps/kdf/
%{tde_prefix}/share/icons/hicolor/*/apps/kdf.png
%{tde_prefix}/share/icons/hicolor/*/apps/kwikdisk.png
%{tde_prefix}/share/doc/tde/HTML/en/kdf/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/storagedevices/
%{tde_prefix}/share/man/man1/kdf.1*
%{tde_prefix}/share/man/man1/kwikdisk.1*

##########

%package -n trinity-kedit
Summary:	Basic text editor for Trinity
Group:		Applications/Utilities

%description -n trinity-kedit
A simple text editor for TDE.

It can be used with Konqueror for text and configuration file browsing.
KEdit also serves well for creating small plain text documents. KEdit's
functionality will intentionally remain rather limited to ensure a
reasonably fast start.

%files -n trinity-kedit
%defattr(-,root,root,-)
%{tde_prefix}/bin/kedit
%{tde_prefix}/%{_lib}/trinity/kedit.la
%{tde_prefix}/%{_lib}/trinity/kedit.so
%{tde_prefix}/%{_lib}/libtdeinit_kedit.so
%{tde_prefix}/share/applications/tde/KEdit.desktop
%{tde_prefix}/share/apps/kedit/
%{tde_prefix}/share/config.kcfg/kedit.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kedit.png
%{tde_prefix}/share/doc/tde/HTML/en/kedit/
%{tde_prefix}/share/man/man1/kedit.1*

##########

%package -n trinity-kfloppy
Summary:	Floppy formatter for Trinity
Group:		Applications/Utilities
Requires:	dosfstools

%description -n trinity-kfloppy
Kfloppy is a utility that provides a straightforward graphical means
to format 3.5" and 5.25" floppy disks.

%files -n trinity-kfloppy
%defattr(-,root,root,-)
%{tde_prefix}/bin/kfloppy
%{tde_prefix}/share/applications/tde/KFloppy.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/floppy_format.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kfloppy.png
%{tde_prefix}/share/doc/tde/HTML/en/kfloppy/
%{tde_prefix}/share/man/man1/kfloppy.1*

##########

%package -n trinity-kgpg
Summary:	GnuPG frontend for Trinity
Group:		Applications/Utilities
Requires:	trinity-konsole
Requires:	gnupg

%description -n trinity-kgpg
Kgpg is a frontend for GNU Privacy Guard (GnuPG). It provides file
encryption, file decryption and key management.

Features:
* an editor mode for easily and quickly encrypting or decrypting a file
  or message which is typed, copied, pasted or dragged into the editor,
  or which is double-clicked in the file manager
* Konqueror integration for encrypting or decrypting files
* a panel applet for encrypting / decrypting files or the clipboard
  contents, etc.
* key management functions (generation, import, export, deletion and
  signing)
* decrypting clipboard contents, including integration with Klipper

%files -n trinity-kgpg
%defattr(-,root,root,-)
%{tde_prefix}/bin/kgpg
%{tde_prefix}/share/applications/tde/kgpg.desktop
%{tde_prefix}/share/apps/kgpg/
%{tde_prefix}/share/apps/konqueror/servicemenus/encryptfile.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/encryptfolder.desktop
%{tde_prefix}/share/autostart/kgpg.desktop
%{tde_prefix}/share/config.kcfg/kgpg.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kgpg.png
%{tde_prefix}/share/doc/tde/HTML/en/kgpg/
%{tde_prefix}/share/man/man1/kgpg.1*

##########

%package -n trinity-khexedit
Summary:	Trinity hex editor
Group:		Applications/Utilities

%description -n trinity-khexedit
KHexEdit is an editor for the raw data of binary files.  It includes
find/replace functions, bookmarks, many configuration options, drag and drop
support and other powerful features.

%files -n trinity-khexedit
%defattr(-,root,root,-)
%{tde_prefix}/bin/khexedit
%{tde_prefix}/%{_lib}/trinity/libkbyteseditwidget.la
%{tde_prefix}/%{_lib}/trinity/libkbyteseditwidget.so
%{tde_prefix}/%{_lib}/trinity/libkhexedit2part.la
%{tde_prefix}/%{_lib}/trinity/libkhexedit2part.so
%{tde_prefix}/%{_lib}/libkhexeditcommon.so.*
%{tde_prefix}/share/applications/tde/khexedit.desktop
%{tde_prefix}/share/apps/khexedit/
%{tde_prefix}/share/apps/khexedit2part/
%{tde_prefix}/share/icons/hicolor/*/apps/khexedit.png
%{tde_prefix}/share/services/kbyteseditwidget.desktop
%{tde_prefix}/share/services/khexedit2part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/khexedit/
%{tde_prefix}/share/man/man1/khexedit.1*

##########

%package -n trinity-kjots
Summary:	Note taking utility for Trinity
Group:		Applications/Utilities

%description -n trinity-kjots
Kjots is a small note taker program. Name and idea are taken from the jots
program included in the tkgoodstuff package.

%files -n trinity-kjots
%defattr(-,root,root,-)
%{tde_prefix}/bin/kjots
%{tde_prefix}/share/applications/tde/Kjots.desktop
%{tde_prefix}/share/apps/kjots/
%{tde_prefix}/share/config.kcfg/kjots.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kjots.png
%{tde_prefix}/share/doc/tde/HTML/en/kjots/

##########

%if %{with klaptopdaemon}

%package -n trinity-klaptopdaemon
Summary:	Battery monitoring and management for laptops using Trinity
Group:		Applications/Utilities
Requires:	trinity-kcontrol

%if %{with consolehelper}
# package 'usermode' provides '/usr/bin/consolehelper-gtk'
Requires:	usermode
%endif

%description -n trinity-klaptopdaemon
This package contains utilities to monitor batteries and configure
power management, for laptops, from within TDE.

%files -n trinity-klaptopdaemon
%defattr(-,root,root,-)
%{tde_prefix}/bin/klaptop_acpi_helper
%{tde_prefix}/bin/klaptop_check
%{tde_prefix}/%{_lib}/trinity/kcm_laptop.la
%{tde_prefix}/%{_lib}/trinity/kcm_laptop.so
%{tde_prefix}/%{_lib}/trinity/kded_klaptopdaemon.la
%{tde_prefix}/%{_lib}/trinity/kded_klaptopdaemon.so
%{tde_prefix}/%{_lib}/libkcmlaptop.so.*
%{tde_prefix}/share/applications/tde/laptop.desktop
%{tde_prefix}/share/applications/tde/pcmcia.desktop
%{tde_prefix}/share/apps/klaptopdaemon/
%{tde_prefix}/share/icons/crystalsvg/*/apps/laptop_battery.png
%{tde_prefix}/share/icons/crystalsvg/*/apps/laptop_pcmcia.png
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/laptop_battery.svgz
%{tde_prefix}/share/services/kded/klaptopdaemon.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmlowbatcrit/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmlowbatwarn/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/laptop/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/powerctrl/

# ConsoleHelper support
%if %{with consolehelper}
%{_sysconfdir}/pam.d/klaptop_acpi_helper
%attr(644,root,root) %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%{tde_prefix}/sbin/klaptop_acpi_helper
%{_sbindir}/klaptop_acpi_helper
%endif

%config(noreplace) %{_sysconfdir}/trinity/kcmlaptoprc

%endif

##########

%package -n trinity-kmilo
Summary:	Laptop special keys support for Trinity
Group:		Applications/Utilities

%description -n trinity-kmilo
KMilo lets you use the special keys on some keyboards and laptops.

Usually this includes volume keys and other features. Currently, KMilo
comes with plugins for Powerbooks, Thinkpads, Vaios and generic keyboards
with special keys.

%files -n trinity-kmilo
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kded_kmilod.la
%{tde_prefix}/%{_lib}/trinity/kded_kmilod.so
%{tde_prefix}/%{_lib}/trinity/kmilo_generic.la
%{tde_prefix}/%{_lib}/trinity/kmilo_generic.so
%{tde_prefix}/%{_lib}/libkmilo.so.*
%{tde_prefix}/share/services/kded/kmilod.desktop
%dir %{tde_prefix}/share/services/kmilo
%{tde_prefix}/share/services/kmilo/kmilo_generic.desktop
%dir %{tde_prefix}/share/servicetypes/kmilo
%{tde_prefix}/share/servicetypes/kmilo/kmilopluginsvc.desktop

##########

%package -n trinity-kmilo-legacy
Summary:	Non-standard plugins for KMilo
Group:		Applications/Utilities
Requires:	trinity-kmilo = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-kcontrol

%description -n trinity-kmilo-legacy
KMilo lets you use the special keys on some keyboards and laptops.

Usually this includes volume keys and other features. Currently, KMilo
comes with plugins for Powerbooks, Thinkpads and Vaios.

The intention is that all laptops work with the generic kmilo
plugin, if you need this package please file a bug.

%files -n trinity-kmilo-legacy
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcm_kvaio.la
%{tde_prefix}/%{_lib}/trinity/kcm_kvaio.so
%{tde_prefix}/%{_lib}/trinity/kcm_thinkpad.la
%{tde_prefix}/%{_lib}/trinity/kcm_thinkpad.so
%{tde_prefix}/%{_lib}/trinity/kmilo_asus.la
%{tde_prefix}/%{_lib}/trinity/kmilo_asus.so
%{tde_prefix}/%{_lib}/trinity/kmilo_delli8k.la
%{tde_prefix}/%{_lib}/trinity/kmilo_delli8k.so
%{tde_prefix}/%{_lib}/trinity/kmilo_kvaio.la
%{tde_prefix}/%{_lib}/trinity/kmilo_kvaio.so
%{tde_prefix}/%{_lib}/trinity/kmilo_thinkpad.la
%{tde_prefix}/%{_lib}/trinity/kmilo_thinkpad.so
%{tde_prefix}/share/applications/tde/kvaio.desktop
%{tde_prefix}/share/applications/tde/thinkpad.desktop
%{tde_prefix}/share/services/kmilo/kmilo_asus.desktop
%{tde_prefix}/share/services/kmilo/kmilo_delli8k.desktop
%{tde_prefix}/share/services/kmilo/kmilo_kvaio.desktop
%{tde_prefix}/share/services/kmilo/kmilo_thinkpad.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kvaio/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/thinkpad/

##########

%package -n trinity-kregexpeditor
Summary:	Graphical regular expression editor plugin for Trinity
Group:		Applications/Utilities

%description -n trinity-kregexpeditor
This package contains a graphical regular expression editor plugin for use
with TDE. It let you draw your regular expression in an unambiguous way.

%files -n trinity-kregexpeditor
%defattr(-,root,root,-)
%{tde_prefix}/bin/kregexpeditor
%{tde_prefix}/%{_lib}/trinity/libkregexpeditorgui.la
%{tde_prefix}/%{_lib}/trinity/libkregexpeditorgui.so
%{tde_prefix}/%{_lib}/libkregexpeditorcommon.so.*
%{tde_prefix}/share/applications/tde/kregexpeditor.desktop
%{tde_prefix}/share/apps/kregexpeditor/
%{tde_prefix}/share/icons/hicolor/*/apps/kregexpeditor.png
%{tde_prefix}/share/services/kregexpeditorgui.desktop
%{tde_prefix}/share/doc/tde/HTML/en/KRegExpEditor/

##########

%package -n trinity-ksim
Summary:	System information monitor for Trinity
Group:		Applications/Utilities
Requires:	trinity-kicker

%description -n trinity-ksim
KSim is a system monitor app which has its own plugin system with support
for GKrellm skins. It allows users to follow uptime, memory usage, network
connections, power, etc.

%files -n trinity-ksim
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/trinity/ksim_panelextensionrc
%{tde_prefix}/%{_lib}/trinity/ksim_*.la
%{tde_prefix}/%{_lib}/trinity/ksim_*.so
%{tde_prefix}/%{_lib}/libksimcore.so.*
%{tde_prefix}/share/apps/kicker/extensions/ksim.desktop
%{tde_prefix}/share/apps/ksim/
%{tde_prefix}/share/doc/tde/HTML/en/ksim/
%{tde_prefix}/share/icons/crystalsvg/*/apps/ksim.png
%{tde_prefix}/share/icons/crystalsvg/*/devices/ksim_cpu.png

##########

%package -n trinity-ktimer
Summary:	Timer utility for Trinity
Group:		Applications/Utilities

%description -n trinity-ktimer
This is a timer application for TDE. It allows you to execute commands after
a certain amount of time. It supports looping commands as well as delayed
command execution.

%files -n trinity-ktimer
%defattr(-,root,root,-)
%{tde_prefix}/bin/ktimer
%{tde_prefix}/share/applications/tde/ktimer.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/ktimer.png
%{tde_prefix}/share/doc/tde/HTML/en/ktimer/

##########

%package -n trinity-tdewalletmanager
Summary:	Wallet manager for Trinity
Group:		Applications/Utilities

Obsoletes:	trinity-kwalletmanager < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kwalletmanager = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdewalletmanager
This program keeps various wallets for any kind of data that the user can
store encrypted with passwords and can also serve as a password manager that
keeps a master password to all wallets.

%files -n trinity-tdewalletmanager
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdewalletmanager
%{tde_prefix}/%{_lib}/trinity/kcm_tdewallet.la
%{tde_prefix}/%{_lib}/trinity/kcm_tdewallet.so
%{tde_prefix}/share/applications/tde/tdewalletconfig.desktop
%{tde_prefix}/share/applications/tde/tdewalletmanager.desktop
%{tde_prefix}/share/applications/tde/tdewalletmanager-tdewalletd.desktop
%{tde_prefix}/share/apps/tdewalletmanager/
%{tde_prefix}/share/icons/hicolor/*/apps/tdewalletmanager.png
%{tde_prefix}/share/services/tdewallet_config.desktop
%{tde_prefix}/share/services/tdewalletmanager_show.desktop
%{tde_prefix}/share/doc/tde/HTML/en/tdewallet/

##########

%if %{with superkaramba}

%package -n trinity-superkaramba
Summary:	A program based on karamba improving the eyecandy of TDE
Group:		Applications/Utilities

%description -n trinity-superkaramba
SuperKaramba is a tool based on karamba that allows anyone to easily create
and run little interactive widgets on a TDE desktop. Widgets are defined in a
simple text file and can be augmented with Python code to make them
interactive.

Here are just some examples of the things that can be done:
* Display system information such as CPU Usage, MP3 playing, etc.
* Create cool custom toolbars that work any way imaginable.
* Create little games or virtual pets that live on your desktop.
* Display information from the internet, such as weather and headlines.

%files -n trinity-superkaramba
%defattr(-,root,root,-)
%{tde_prefix}/bin/superkaramba
%{tde_prefix}/share/applications/tde/superkaramba.desktop
%{tde_prefix}/share/apps/superkaramba/
%{tde_prefix}/share/icons/crystalsvg/*/apps/superkaramba.png
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/superkaramba_theme.png
%{tde_prefix}/share/icons/crystalsvg/scalable/apps/superkaramba.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/mimetypes/superkaramba_theme.svgz
%{tde_prefix}/share/mimelnk/application/x-superkaramba.desktop
%{tde_prefix}/share/doc/tde/HTML/en/superkaramba/
%{tde_prefix}/share/man/man1/superkaramba.1*

%endif

##########

%if %{with tdefilereplace}

%package -n trinity-tdefilereplace
Summary:	Batch search-and-replace component for TDE
Group:		Applications/Utilities

Obsoletes:	trinity-kfilereplace < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kfilereplace = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdefilereplace
TDEFileReplace is an embedded component for TDE that acts as a batch
search-and-replace tool. It allows you to replace one expression with
another in many files at once.

Note that at the moment TDEFileReplace does not come as a standalone
application.

This package is part of Trinity, as a component of the TDE utilities module.

%files -n trinity-tdefilereplace
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdefilereplace
%{tde_prefix}/%{_lib}/trinity/libtdefilereplacepart.la
%{tde_prefix}/%{_lib}/trinity/libtdefilereplacepart.so
%{tde_prefix}/share/applications/tde/tdefilereplace.desktop
%{tde_prefix}/share/apps/tdefilereplace/
%{tde_prefix}/share/apps/tdefilereplacepart/
%{tde_prefix}/share/doc/tde/HTML/en/tdefilereplace/
%{tde_prefix}/share/icons/hicolor/*/apps/tdefilereplace.png
%{tde_prefix}/share/services/tdefilereplacepart.desktop
%{tde_prefix}/share/man/man1/tdefilereplace.1*

%endif

##########

# afaik, nobody BR's it, and it pulls kdeutils into multilib -- Rex
%package devel
Summary:	Development files for %{name} 
Group:		Development/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel

Obsoletes:	trinity-kdeutils-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeutils-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	tdeutils-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	tdeutils-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development files for tdeutils.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/*
%if %{with klaptopdaemon}
%{tde_prefix}/%{_lib}/libkcmlaptop.la
%{tde_prefix}/%{_lib}/libkcmlaptop.so
%endif
%{tde_prefix}/%{_lib}/libtdeinit_ark.la
%{tde_prefix}/%{_lib}/libtdeinit_irkick.la
%{tde_prefix}/%{_lib}/libtdeinit_kcalc.la
%{tde_prefix}/%{_lib}/libtdeinit_kedit.la
%{tde_prefix}/%{_lib}/libkmilo.la
%{tde_prefix}/%{_lib}/libkmilo.so
%{tde_prefix}/%{_lib}/libkregexpeditorcommon.la
%{tde_prefix}/%{_lib}/libkregexpeditorcommon.so
%{tde_prefix}/%{_lib}/libksimcore.la
%{tde_prefix}/%{_lib}/libksimcore.so
%{tde_prefix}/%{_lib}/libkhexeditcommon.la
%{tde_prefix}/%{_lib}/libkhexeditcommon.so
%{tde_prefix}/share/cmake/libksimcore.cmake

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

%install -a

%if %{?with_klaptopdaemon}
### Use consolehelper for 'klaptop_acpi_helper'
%if %{?with_consolehelper}
# Install configuration files
%__install -p -D -m 644 "%{SOURCE1}" "%{buildroot}%{_sysconfdir}/pam.d/klaptop_acpi_helper"
%__install -p -D -m 644 "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/security/console.apps/klaptop_acpi_helper"
# Moves the actual binary from 'bin' to 'sbin'
%__mkdir_p "%{buildroot}%{tde_prefix}/sbin" "%{buildroot}%{_sbindir}"
%__mv "%{buildroot}%{tde_prefix}/bin/klaptop_acpi_helper" "%{buildroot}%{tde_prefix}/sbin"
# Links to consolehelper
%__ln_s "%{_bindir}/consolehelper" "%{buildroot}%{tde_prefix}/bin/klaptop_acpi_helper"
# Put another symlink under '/usr', otherwise consolehelper does not work
%if "%{tde_prefix}" != "/usr"
%__ln_s "%{tde_prefix}/sbin/klaptop_acpi_helper" "%{?buildroot}%{_sbindir}/klaptop_acpi_helper"
%endif
%endif

# klaptop settings file
%__install -p -D -m 644 "%{SOURCE3}" "%{buildroot}%{_sysconfdir}/trinity/kcmlaptoprc"

%else

# Klaptop's documentation is installed even if we did not build the program ...
%__rm -fr %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmlowbatcrit/
%__rm -fr %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/kcmlowbatwarn/
%__rm -fr %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/laptop/
%__rm -fr %{?buildroot}%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/powerctrl/

%endif

# Fix desktop shortcut location
if [ -d "%{?buildroot}%{tde_prefix}/share/applnk" ]; then
  %__mkdir_p "%{?buildroot}%{tde_prefix}/share/applications/tde"
%if %{with_superkaramba}
  %__mv "%{?buildroot}%{tde_prefix}/share/applnk/Utilities/superkaramba.desktop" "%{?buildroot}%{tde_prefix}/share/applications/tde/superkaramba.desktop"
%endif
  %__rm -rf "%{?buildroot}%{tde_prefix}/share/applnk"
fi

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_prefix}/share/applications/tde/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Other TDE-only apps
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/thinkpad.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/kcmlirc.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/kvaio.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/kcmdf.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/tdewalletconfig.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/khexedit.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/kregexpeditor.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/kgpg.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/Kjots.desktop"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

