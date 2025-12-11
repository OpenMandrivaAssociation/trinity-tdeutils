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
%define pkg_rel 2

%define tde_pkg tdeutils
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_confdir %{_sysconfdir}/trinity
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_sbindir %{tde_prefix}/sbin
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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

#Vendor:		Trinity Project
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:		%{tde_prefix}

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	klaptop_acpi_helper.pam
Source2:	klaptop_acpi_helper.console
Source3:	kcmlaptoprc
Source4:	%{name}-rpmlintrc

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DBIN_INSTALL_DIR="%{tde_bindir}"
BuildOption:    -DCONFIG_INSTALL_DIR="%{tde_confdir}"
BuildOption:    -DDOC_INSTALL_DIR="%{tde_docdir}"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_tdeincludedir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DPKGCONFIG_INSTALL_DIR="%{tde_libdir}/pkgconfig"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DWITH_DPMS=ON -DWITH_ASUS=ON -DWITH_POWERBOOK=OFF
BuildOption:    -DWITH_POWERBOOK2=OFF -DWITH_VAIO=ON
BuildOption:    -DWITH_THINKPAD=ON -DWITH_I8K=ON
BuildOption:    -DWITH_SNMP=ON -DWITH_SENSORS=ON -DWITH_XMMS=ON
BuildOption:    -DWITH_TDENEWSTUFF=ON -DBUILD_ALL=ON
%{?with_xscreensaver:BuildOption:    -DWITH_XSCREENSAVER=ON}
%{?!with_klaptopdaemon:BuildOption:    -DBUILD_KLAPTOPDAEMON=OFF}
%{?!with_superkaramba:BuildOption:    -DBUILD_SUPERKARAMBA=OFF}
%{?!with_tdefilereplace:BuildOption:    -DBUILD_TDEFILEREPLACE=OFF}

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
%{tde_bindir}/ark
%{tde_tdelibdir}/ark.la
%{tde_tdelibdir}/ark.so
%{tde_tdelibdir}/libarkpart.la
%{tde_tdelibdir}/libarkpart.so
%{tde_libdir}/libtdeinit_ark.so
%{tde_tdeappdir}/ark.desktop
%{tde_datadir}/apps/ark/
%{tde_datadir}/config.kcfg/ark.kcfg
%{tde_datadir}/icons/hicolor/*/apps/ark.png
%{tde_datadir}/icons/hicolor/scalable/apps/ark.svgz
%{tde_datadir}/services/ark_part.desktop
%{tde_tdedocdir}/HTML/en/ark/
%{tde_mandir}/man1/ark.1*

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
%{tde_bindir}/kcalc
%{tde_tdelibdir}/kcalc.la
%{tde_tdelibdir}/kcalc.so
%{tde_libdir}/libtdeinit_kcalc.so
%{tde_tdeappdir}/kcalc.desktop
%{tde_datadir}/apps/kcalc/
%{tde_datadir}/apps/tdeconf_update/kcalcrc.upd
%{tde_datadir}/config.kcfg/kcalc.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kcalc.png
%{tde_datadir}/icons/hicolor/scalable/apps/kcalc.svgz
%{tde_tdedocdir}/HTML/en/kcalc/
%{tde_mandir}/man1/kcalc.1*

##########

%package -n trinity-kcharselect
Summary:	Character selector for Trinity
Group:		Applications/Utilities
Requires:	trinity-kicker

%description -n trinity-kcharselect
This package contains kcharselect, a character set selector for TDE.

%files -n trinity-kcharselect
%defattr(-,root,root,-)
%{tde_bindir}/kcharselect
%{tde_tdelibdir}/kcharselect_panelapplet.la
%{tde_tdelibdir}/kcharselect_panelapplet.so
%{tde_tdeappdir}/KCharSelect.desktop
%{tde_datadir}/apps/kcharselect/
%{tde_datadir}/apps/tdeconf_update/kcharselect.upd
%{tde_datadir}/apps/kicker/applets/kcharselectapplet.desktop
%{tde_datadir}/icons/hicolor/*/apps/kcharselect.png
%{tde_tdedocdir}/HTML/en/kcharselect/
%{tde_mandir}/man1/kcharselect.1*

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
%{tde_bindir}/irkick
%{tde_tdelibdir}/irkick.la
%{tde_tdelibdir}/irkick.so
%{tde_tdelibdir}/kcm_kcmlirc.la
%{tde_tdelibdir}/kcm_kcmlirc.so
%{tde_libdir}/libtdeinit_irkick.so
%{tde_tdeappdir}/irkick.desktop
%{tde_tdeappdir}/kcmlirc.desktop
%{tde_datadir}/apps/irkick/
%{tde_datadir}/apps/profiles/tdelauncher.profile.xml
%{tde_datadir}/apps/profiles/konqueror.profile.xml
%{tde_datadir}/apps/profiles/noatun.profile.xml
%{tde_datadir}/apps/profiles/profile.dtd
%dir %{tde_datadir}/apps/remotes
%{tde_datadir}/apps/remotes/RM-0010.remote.xml
%{tde_datadir}/apps/remotes/cimr100.remote.xml
%{tde_datadir}/apps/remotes/hauppauge.remote.xml
%{tde_datadir}/apps/remotes/remote.dtd
%{tde_datadir}/apps/remotes/sherwood.remote.xml
%{tde_datadir}/apps/remotes/sonytv.remote.xml
%{tde_datadir}/autostart/irkick.desktop
%{tde_datadir}/icons/hicolor/*/apps/irkick.png
%{tde_datadir}/icons/locolor/*/apps/irkick.png
%{tde_tdedocdir}/HTML/en/irkick/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmlirc/

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
%{tde_bindir}/tdessh

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
%{tde_bindir}/kdf
%{tde_bindir}/kwikdisk
%{tde_tdelibdir}/kcm_kdf.la
%{tde_tdelibdir}/kcm_kdf.so
%{tde_tdeappdir}/kcmdf.desktop
%{tde_tdeappdir}/kdf.desktop
%{tde_tdeappdir}/kwikdisk.desktop
%{tde_datadir}/apps/kdf/
%{tde_datadir}/icons/hicolor/*/apps/kdf.png
%{tde_datadir}/icons/hicolor/*/apps/kwikdisk.png
%{tde_tdedocdir}/HTML/en/kdf/
%{tde_tdedocdir}/HTML/en/kcontrol/storagedevices/
%{tde_mandir}/man1/kdf.1*
%{tde_mandir}/man1/kwikdisk.1*

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
%{tde_bindir}/kedit
%{tde_tdelibdir}/kedit.la
%{tde_tdelibdir}/kedit.so
%{tde_libdir}/libtdeinit_kedit.so
%{tde_tdeappdir}/KEdit.desktop
%{tde_datadir}/apps/kedit/
%{tde_datadir}/config.kcfg/kedit.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kedit.png
%{tde_tdedocdir}/HTML/en/kedit/
%{tde_mandir}/man1/kedit.1*

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
%{tde_bindir}/kfloppy
%{tde_tdeappdir}/KFloppy.desktop
%{tde_datadir}/apps/konqueror/servicemenus/floppy_format.desktop
%{tde_datadir}/icons/hicolor/*/apps/kfloppy.png
%{tde_tdedocdir}/HTML/en/kfloppy/
%{tde_mandir}/man1/kfloppy.1*

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
%{tde_bindir}/kgpg
%{tde_tdeappdir}/kgpg.desktop
%{tde_datadir}/apps/kgpg/
%{tde_datadir}/apps/konqueror/servicemenus/encryptfile.desktop
%{tde_datadir}/apps/konqueror/servicemenus/encryptfolder.desktop
%{tde_datadir}/autostart/kgpg.desktop
%{tde_datadir}/config.kcfg/kgpg.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kgpg.png
%{tde_tdedocdir}/HTML/en/kgpg/
%{tde_mandir}/man1/kgpg.1*

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
%{tde_bindir}/khexedit
%{tde_tdelibdir}/libkbyteseditwidget.la
%{tde_tdelibdir}/libkbyteseditwidget.so
%{tde_tdelibdir}/libkhexedit2part.la
%{tde_tdelibdir}/libkhexedit2part.so
%{tde_libdir}/libkhexeditcommon.so.*
%{tde_tdeappdir}/khexedit.desktop
%{tde_datadir}/apps/khexedit/
%{tde_datadir}/apps/khexedit2part/
%{tde_datadir}/icons/hicolor/*/apps/khexedit.png
%{tde_datadir}/services/kbyteseditwidget.desktop
%{tde_datadir}/services/khexedit2part.desktop
%{tde_tdedocdir}/HTML/en/khexedit/
%{tde_mandir}/man1/khexedit.1*

##########

%package -n trinity-kjots
Summary:	Note taking utility for Trinity
Group:		Applications/Utilities

%description -n trinity-kjots
Kjots is a small note taker program. Name and idea are taken from the jots
program included in the tkgoodstuff package.

%files -n trinity-kjots
%defattr(-,root,root,-)
%{tde_bindir}/kjots
%{tde_tdeappdir}/Kjots.desktop
%{tde_datadir}/apps/kjots/
%{tde_datadir}/config.kcfg/kjots.kcfg
%{tde_datadir}/icons/hicolor/*/apps/kjots.png
%{tde_tdedocdir}/HTML/en/kjots/

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
%{tde_bindir}/klaptop_acpi_helper
%{tde_bindir}/klaptop_check
%{tde_tdelibdir}/kcm_laptop.la
%{tde_tdelibdir}/kcm_laptop.so
%{tde_tdelibdir}/kded_klaptopdaemon.la
%{tde_tdelibdir}/kded_klaptopdaemon.so
%{tde_libdir}/libkcmlaptop.so.*
%{tde_tdeappdir}/laptop.desktop
%{tde_tdeappdir}/pcmcia.desktop
%{tde_datadir}/apps/klaptopdaemon/
%{tde_datadir}/icons/crystalsvg/*/apps/laptop_battery.png
%{tde_datadir}/icons/crystalsvg/*/apps/laptop_pcmcia.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/laptop_battery.svgz
%{tde_datadir}/services/kded/klaptopdaemon.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatcrit/
%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatwarn/
%{tde_tdedocdir}/HTML/en/kcontrol/laptop/
%{tde_tdedocdir}/HTML/en/kcontrol/powerctrl/

# ConsoleHelper support
%if %{with consolehelper}
%{_sysconfdir}/pam.d/klaptop_acpi_helper
%attr(644,root,root) %{_sysconfdir}/security/console.apps/klaptop_acpi_helper
%{tde_sbindir}/klaptop_acpi_helper
%{_sbindir}/klaptop_acpi_helper
%endif

%config(noreplace) %{tde_confdir}/kcmlaptoprc

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
%{tde_tdelibdir}/kded_kmilod.la
%{tde_tdelibdir}/kded_kmilod.so
%{tde_tdelibdir}/kmilo_generic.la
%{tde_tdelibdir}/kmilo_generic.so
%{tde_libdir}/libkmilo.so.*
%{tde_datadir}/services/kded/kmilod.desktop
%dir %{tde_datadir}/services/kmilo
%{tde_datadir}/services/kmilo/kmilo_generic.desktop
%dir %{tde_datadir}/servicetypes/kmilo
%{tde_datadir}/servicetypes/kmilo/kmilopluginsvc.desktop

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
%{tde_tdelibdir}/kcm_kvaio.la
%{tde_tdelibdir}/kcm_kvaio.so
%{tde_tdelibdir}/kcm_thinkpad.la
%{tde_tdelibdir}/kcm_thinkpad.so
%{tde_tdelibdir}/kmilo_asus.la
%{tde_tdelibdir}/kmilo_asus.so
%{tde_tdelibdir}/kmilo_delli8k.la
%{tde_tdelibdir}/kmilo_delli8k.so
%{tde_tdelibdir}/kmilo_kvaio.la
%{tde_tdelibdir}/kmilo_kvaio.so
%{tde_tdelibdir}/kmilo_thinkpad.la
%{tde_tdelibdir}/kmilo_thinkpad.so
%{tde_tdeappdir}/kvaio.desktop
%{tde_tdeappdir}/thinkpad.desktop
%{tde_datadir}/services/kmilo/kmilo_asus.desktop
%{tde_datadir}/services/kmilo/kmilo_delli8k.desktop
%{tde_datadir}/services/kmilo/kmilo_kvaio.desktop
%{tde_datadir}/services/kmilo/kmilo_thinkpad.desktop
%{tde_tdedocdir}/HTML/en/kcontrol/kvaio/
%{tde_tdedocdir}/HTML/en/kcontrol/thinkpad/

##########

%package -n trinity-kregexpeditor
Summary:	Graphical regular expression editor plugin for Trinity
Group:		Applications/Utilities

%description -n trinity-kregexpeditor
This package contains a graphical regular expression editor plugin for use
with TDE. It let you draw your regular expression in an unambiguous way.

%files -n trinity-kregexpeditor
%defattr(-,root,root,-)
%{tde_bindir}/kregexpeditor
%{tde_tdelibdir}/libkregexpeditorgui.la
%{tde_tdelibdir}/libkregexpeditorgui.so
%{tde_libdir}/libkregexpeditorcommon.so.*
%{tde_tdeappdir}/kregexpeditor.desktop
%{tde_datadir}/apps/kregexpeditor/
%{tde_datadir}/icons/hicolor/*/apps/kregexpeditor.png
%{tde_datadir}/services/kregexpeditorgui.desktop
%{tde_tdedocdir}/HTML/en/KRegExpEditor/

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
%config(noreplace) %{tde_confdir}/ksim_panelextensionrc
%{tde_tdelibdir}/ksim_*.la
%{tde_tdelibdir}/ksim_*.so
%{tde_libdir}/libksimcore.so.*
%{tde_datadir}/apps/kicker/extensions/ksim.desktop
%{tde_datadir}/apps/ksim/
%{tde_tdedocdir}/HTML/en/ksim/
%{tde_datadir}/icons/crystalsvg/*/apps/ksim.png
%{tde_datadir}/icons/crystalsvg/*/devices/ksim_cpu.png

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
%{tde_bindir}/ktimer
%{tde_tdeappdir}/ktimer.desktop
%{tde_datadir}/icons/hicolor/*/apps/ktimer.png
%{tde_tdedocdir}/HTML/en/ktimer/

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
%{tde_bindir}/tdewalletmanager
%{tde_tdelibdir}/kcm_tdewallet.la
%{tde_tdelibdir}/kcm_tdewallet.so
%{tde_tdeappdir}/tdewalletconfig.desktop
%{tde_tdeappdir}/tdewalletmanager.desktop
%{tde_tdeappdir}/tdewalletmanager-tdewalletd.desktop
%{tde_datadir}/apps/tdewalletmanager/
%{tde_datadir}/icons/hicolor/*/apps/tdewalletmanager.png
%{tde_datadir}/services/tdewallet_config.desktop
%{tde_datadir}/services/tdewalletmanager_show.desktop
%{tde_tdedocdir}/HTML/en/tdewallet/

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
%{tde_bindir}/superkaramba
%{tde_tdeappdir}/superkaramba.desktop
%{tde_datadir}/apps/superkaramba/
%{tde_datadir}/icons/crystalsvg/*/apps/superkaramba.png
%{tde_datadir}/icons/crystalsvg/*/mimetypes/superkaramba_theme.png
%{tde_datadir}/icons/crystalsvg/scalable/apps/superkaramba.svgz
%{tde_datadir}/icons/crystalsvg/scalable/mimetypes/superkaramba_theme.svgz
%{tde_datadir}/mimelnk/application/x-superkaramba.desktop
%{tde_tdedocdir}/HTML/en/superkaramba/
%{tde_mandir}/man1/superkaramba.1*

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
%{tde_bindir}/tdefilereplace
%{tde_tdelibdir}/libtdefilereplacepart.la
%{tde_tdelibdir}/libtdefilereplacepart.so
%{tde_tdeappdir}/tdefilereplace.desktop
%{tde_datadir}/apps/tdefilereplace/
%{tde_datadir}/apps/tdefilereplacepart/
%{tde_tdedocdir}/HTML/en/tdefilereplace/
%{tde_datadir}/icons/hicolor/*/apps/tdefilereplace.png
%{tde_datadir}/services/tdefilereplacepart.desktop
%{tde_mandir}/man1/tdefilereplace.1*

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
%{tde_tdeincludedir}/*
%if %{with klaptopdaemon}
%{tde_libdir}/libkcmlaptop.la
%{tde_libdir}/libkcmlaptop.so
%endif
%{tde_libdir}/libtdeinit_ark.la
%{tde_libdir}/libtdeinit_irkick.la
%{tde_libdir}/libtdeinit_kcalc.la
%{tde_libdir}/libtdeinit_kedit.la
%{tde_libdir}/libkmilo.la
%{tde_libdir}/libkmilo.so
%{tde_libdir}/libkregexpeditorcommon.la
%{tde_libdir}/libkregexpeditorcommon.so
%{tde_libdir}/libksimcore.la
%{tde_libdir}/libksimcore.so
%{tde_libdir}/libkhexeditcommon.la
%{tde_libdir}/libkhexeditcommon.so
%{tde_datadir}/cmake/libksimcore.cmake

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

%install -a

%if %{?with_klaptopdaemon}
### Use consolehelper for 'klaptop_acpi_helper'
%if %{?with_consolehelper}
# Install configuration files
%__install -p -D -m 644 "%{SOURCE1}" "%{buildroot}%{_sysconfdir}/pam.d/klaptop_acpi_helper"
%__install -p -D -m 644 "%{SOURCE2}" "%{buildroot}%{_sysconfdir}/security/console.apps/klaptop_acpi_helper"
# Moves the actual binary from 'bin' to 'sbin'
%__mkdir_p "%{buildroot}%{tde_sbindir}" "%{buildroot}%{_sbindir}"
%__mv "%{buildroot}%{tde_bindir}/klaptop_acpi_helper" "%{buildroot}%{tde_sbindir}"
# Links to consolehelper
%__ln_s "%{_bindir}/consolehelper" "%{buildroot}%{tde_bindir}/klaptop_acpi_helper"
# Put another symlink under '/usr', otherwise consolehelper does not work
%if "%{tde_prefix}" != "/usr"
%__ln_s "%{tde_sbindir}/klaptop_acpi_helper" "%{?buildroot}%{_sbindir}/klaptop_acpi_helper"
%endif
%endif

# klaptop settings file
%__install -p -D -m 644 "%{SOURCE3}" "%{buildroot}%{tde_confdir}/kcmlaptoprc"

%else

# Klaptop's documentation is installed even if we did not build the program ...
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatcrit/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/kcmlowbatwarn/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/laptop/
%__rm -fr %{?buildroot}%{tde_tdedocdir}/HTML/en/kcontrol/powerctrl/

%endif

# Fix desktop shortcut location
if [ -d "%{?buildroot}%{tde_datadir}/applnk" ]; then
  %__mkdir_p "%{?buildroot}%{tde_tdeappdir}"
%if %{with_superkaramba}
  %__mv "%{?buildroot}%{tde_datadir}/applnk/Utilities/superkaramba.desktop" "%{?buildroot}%{tde_tdeappdir}/superkaramba.desktop"
%endif
  %__rm -rf "%{?buildroot}%{tde_datadir}/applnk"
fi

# Icons from TDE Control Center should only be displayed in TDE
for i in %{?buildroot}%{tde_tdeappdir}/*.desktop ; do
  if grep -q "^Categories=.*X-TDE-settings" "${i}"; then
    if ! grep -q "OnlyShowIn=TDE" "${i}" ; then
      echo "OnlyShowIn=TDE;" >>"${i}"
    fi
  fi
done

# Other TDE-only apps
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/thinkpad.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kcmlirc.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kvaio.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kcmdf.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/tdewalletconfig.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/khexedit.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kregexpeditor.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/kgpg.desktop"
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_tdeappdir}/Kjots.desktop"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_datadir}"

