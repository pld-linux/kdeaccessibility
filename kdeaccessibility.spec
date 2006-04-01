#
# TODO:
# - fix festival and speech_tools

%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	3.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	bcfd51875aa2a168fbc97055a576a33c
URL:		http://www.kde.org/
BuildRequires:	akode-devel
BuildRequires:	festival-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	speech_tools-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accessibility support for KDE.

%description -l pl
U³atwienia dostêpu dla KDE.

%package devel
Summary:	Accessibility support for KDE - header files
Summary(pl):	U³atwienia dostêpu dla KDE - pliki nag³ówkowe
Group:		X11/Applications
Requires:	kdelibs-devel = %{_minlibsevr}

%description devel
Accessibility support for KDE - header files.

%description devel -l pl
U³atwienia dostêpu dla KDE - pliki nag³ówkowe.

%package -n kde-icons-mono
Summary:	KDE Icons Theme - mono
Summary(pl):	Motyw ikon dla KDE - mono
Group:		X11/Amusements
Requires:	kdelibs >= %{_minlibsevr}

%description -n kde-icons-mono
KDE Icons Theme - mono.

%description -n kde-icons-mono -l pl
Motyw ikon dla KDE - mono.

%package kbstateapplet
Summary:	Keyboard Status Applet
Summary(pl):	Aplet stanu klawiatury
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description kbstateapplet
Keyboard Status Applet.

%description kbstateapplet -l pl
Aplet stanu klawiatury.

%package kmag
Summary:	A KDE magnifying tool
Summary(pl):	Lupa dla ¶rodowiska KDE
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmag
A KDE magnifying tool.

%description kmag -l pl
Lupa dla ¶rodowiska KDE.

%package kmousetool
Summary:	KMouseTool - a program that clicks the mouse for you
Summary(pl):	KMouseTool - narzêdzie do klikania myszk± bez naciskania jej przycisków
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmousetool
KMouseTool is a program that clicks the mouse for you. KMouseTool
clicks the mouse whenever the mouse cursor pauses briefly. It was
designed to help those with repetitive strain injuries, for whom
pressing buttons hurts. It can also drag the mouse, although this
takes a bit more practice.

%description kmousetool -l pl
KMouseTool jest narzêdziem do klikania myszk± bez naciskania jej
przycisków. KMouseTool klika myszk± za ka¿dym razem gdy kursor
zatrzymuje siê na krótko. Narzêdzie to zosta³o zaprojektowane by pomóc
osobom z uszkodzeniami miê¶ni, dla których naciskanie przycisków jest
bolesne. Ponadto mo¿e ono przeci±gaæ mysz±, aczkolwiek wymaga to
pewnej praktyki.

%package kmouth
Summary:	A frontend for speech synthesizers
Summary(pl):	Frontend do syntezatorów mowy
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmouth
KMouth is a frontend for speech synthesizers. It is a program that
enables persons that cannot speak to let their computers speak. It
includes a history of spoken sentences from which the user can select
sentences to be re-spoken.

Note that KMouth does not include speech synthesizer. Instead it
requires a speech synthesizer installed in the system.

%description kmouth -l pl
KMouth jest frontendem do syntezatorów mowy. Jest to narzêdzie dziêki
któremu osoby nieme mog± pozwoliæ komputerowi mówiæ za nie. Zawiera on
historiê wypowiedzianych zdañ, z której to u¿ytkownik mo¿e wybraæ
zdanie do ponownego wypowiedzenia.

UWAGA! KMouth nie zawiera syntezatora mowy. Zamiast tego wykorzystuje
syntezator zainstalowany w systemie.

%package ksayit
Summary:	KSayIt - A Text To Speech frontend for KDE
Summary(pl):	KSayIt - Frontend systemu Tekst-w-Mowê KDE
Group:		X11/Applications
Requires:	%{name}-kttsd = %{epoch}:%{version}-%{release}

%description ksayit
A Text To Speech frontend for KDE.

%description ksayit -l pl
Frontend systemu Tekst-w-Mowê KDE.

%package kttsd
Summary:	KDE Text-to-Speech
Summary(pl):	KDE Tekst-w-Mowê
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kttsd

%description kttsd
KTTS -- KDE Text-to-Speech -- is a subsystem within the KDE desktop
for conversion of text to audible speech. KTTS is currently under
development and aims to become the standard subsystem for all KDE
applications to provide speech output.

%description kttsd -l pl
KTTS -- KDE Tekst-w-Mowê -- jest podsystemem ¶rodowiska KDE s³u¿±cym
do konwersji tekstu w s³yszaln± mowê. KTTS jest ca³y czas rozwijany,
jego celem jest zostanie standardowym podsystemem dostarczaj±cym
wyj¶cie mowy dla wszystkich aplikacji KDE.

%package kttsd-akode
Summary:	KTTS AKODE plugin
Summary(pl):	Wtyczka AKODE dla KTTS
Group:		X11/Applications
Requires:	%{name}-kttsd = %{epoch}:%{version}-%{release}

%description kttsd-akode
KTTS AKODE plugin.

%description kttsd-akode -l pl
Wtyczka AKODE dla KTTS.

%package kttsd-gstreamer
Summary:	KTTS GStreamer plugin
Summary(pl):	Wtyczka Gstreamer dla KTTS
Group:		X11/Applications
Requires:	%{name}-kttsd = %{epoch}:%{version}-%{release}

%description kttsd-gstreamer
KTTS GStreamer plugin.

%description kttsd-gstreamer -l pl
Wtyczka Gstreamer dla KTTS.

%prep
%setup -q
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Accessibility;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kmouth/kmouth.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Accessibility;/' \
	-e 's/Terminal=0/Terminal=false/' -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	kmag/kmag.desktop \
	kmousetool/kmousetool/kmousetool.desktop

%build
cp /usr/share/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--disable-final \
	--with-gstreamer \
	--with-alsa \
	--with-akode \
	--enable-kttsd-festival \
	--enable-kttsd-festivalcs \
	--enable-kttsd-gstreamer \
	--with-qt-libraries=%{_libdir} \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/* \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde
%find_lang kttsd	--with-kde

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post	kttsd	-p /sbin/ldconfig
%postun	kttsd	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/ksayit_fxplugin.h

%files -n kde-icons-mono
%defattr(644,root,root,755)
%{_iconsdir}/mono
%exclude %{_iconsdir}/mono/*/apps/kmag.*
%exclude %{_iconsdir}/mono/*/apps/kmousetool.*
%exclude %{_iconsdir}/mono/*/apps/kmouth.*

%files kbstateapplet
%defattr(644,root,root,755)
%{_libdir}/kde3/kbstate_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kbstate_panelapplet.so
%{_datadir}/apps/kbstateapplet
%{_datadir}/apps/kicker/applets/kbstateapplet.desktop

%files kmag -f kmag.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_datadir}/apps/kmag
%{_desktopdir}/kde/kmag.desktop
%{_iconsdir}/[!l]*/*/apps/kmag.*

%files kmousetool -f kmousetool.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_datadir}/apps/kmousetool
%{_desktopdir}/kde/kmousetool.desktop
%{_iconsdir}/[!l]*/*/apps/kmousetool.*

%files kmouth -f kmouth.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_datadir}/apps/kmouth
%{_datadir}/config/kmouthrc
%{_desktopdir}/kde/kmouth.desktop
%{_iconsdir}/[!l]*/*/apps/kmouth.*

%files ksayit
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksayit
%{_desktopdir}/kde/ksayit.desktop
%{_datadir}/apps/ksayit
%{_iconsdir}/*/*/*/ksayit*

%files kttsd -f kttsd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kttsd
%attr(755,root,root) %{_bindir}/kttsmgr
%{_libdir}/kde3/kcm_kttsd.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kttsd.so
%{_libdir}/kde3/ktexteditor_kttsd.la
%attr(755,root,root) %{_libdir}/kde3/ktexteditor_kttsd.so
%{_libdir}/kde3/libkttsd_alsaplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_alsaplugin.so
%{_libdir}/kde3/libkttsd_artsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_artsplugin.so
%{_libdir}/kde3/libkttsd_commandplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_commandplugin.so
%{_libdir}/kde3/libkttsd_eposplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_eposplugin.so
%{_libdir}/kde3/libkttsd_festivalintplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_festivalintplugin.so
%{_libdir}/kde3/libkttsd_fliteplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_fliteplugin.so
%{_libdir}/kde3/libkttsd_freettsplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_freettsplugin.so
%{_libdir}/kde3/libkttsd_hadifixplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_hadifixplugin.so
%{_libdir}/kde3/libkttsd_sbdplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_sbdplugin.so
%{_libdir}/kde3/libkttsd_stringreplacerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_stringreplacerplugin.so
%{_libdir}/kde3/libkttsd_talkerchooserplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_talkerchooserplugin.so
%{_libdir}/kde3/libkttsd_xmltransformerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_xmltransformerplugin.so
%{_libdir}/kde3/libkttsjobmgrpart.la
%attr(755,root,root) %{_libdir}/kde3/libkttsjobmgrpart.so
%{_libdir}/libKTTSD_Lib.la
%attr(755,root,root) %{_libdir}/libKTTSD_Lib.so.*.*.*
%{_libdir}/libkttsd.la
%attr(755,root,root) %{_libdir}/libkttsd.so.*.*.*
%{_desktopdir}/kde/kcmkttsd.desktop
%{_desktopdir}/kde/kttsmgr.desktop
%{_datadir}/apps/ktexteditor_kttsd
%{_datadir}/apps/kttsd
%{_datadir}/services/*ktts*.desktop
%{_datadir}/servicetypes/*ktts*.desktop
%{_iconsdir}/*/*/*/kttsd.*
%{_iconsdir}/*/*/*/female.*
%{_iconsdir}/*/*/*/male.*
%{_iconsdir}/*/*/*/*speak.png

%files kttsd-akode
%defattr(644,root,root,755)
%{_libdir}/kde3/libkttsd_akodeplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_akodeplugin.so

%files kttsd-gstreamer
%defattr(644,root,root,755)
%{_libdir}/kde3/libkttsd_gstplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkttsd_gstplugin.so
