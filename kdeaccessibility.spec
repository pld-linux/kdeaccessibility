#
# Conditional build:
%bcond_without	i18n	# don't build i18n subpackage
#
%define		_state		stable
%define		_ver		3.2.0

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	%{_ver}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	97466b78dcee2d29505937c79919713d
%if %{with i18n}
Source1:        http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	cb5057c35fc76fa96057e166fa62226b
%endif
URL:		http://www.kde.org/
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accessibility support for KDE.

%description -l pl
U³atwienia dostêpu dla KDE.

%package kmag
Summary:	A KDE magnifying tool
Summary(pl):	Lupa dla ¶rodowiska KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmag
A KDE magnifying tool.

%description kmag -l pl
Lupa dla ¶rodowiska KDE.

%package kmousetool
Summary:	MouseTool - a program that clicks the mouse for you
Summary(pl):	MouseTool - narzêdzie do klikania myszk± bez naciskania jej przycisków
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmousetool
MouseTool is a program that clicks the mouse for you.

%description kmousetool -l pl
MouseTool to narzêdzie do klikania myszk± bez naciskania jej
przycisków.

%package kmouth
Summary:	A frontend for speech synthesizers
Summary(pl):	Frontend do syntezatorów mowy
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmouth
A frontend for speech synthesizers.

%description kmouth -l pl
Frontend do syntezatorów mowy.

%package i18n
Summary:	Common internationalization and localization files for kdeaccessibility
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeaccessibility
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdeaccessibility.

%description i18n -l pl
Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdeaccessibility.


%package kmag-i18n
Summary:	Internationalization and localization files for kmag
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmag
Group:		X11/Applications
Requires:	%{name}-kmag = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kmag-i18n
Internationalization and localization files for kmag.

%description kmag-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmag.

%package kmousetool-i18n
Summary:	Internationalization and localization files for kmousetool
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmousetool
Group:		X11/Applications
Requires:	%{name}-kmousetool = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kmousetool-i18n
Internationalization and localization files for kmousetool.

%description kmousetool-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmousetool.

%package kmouth-i18n
Summary:	Internationalization and localization files for kmouth
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmouth
Group:		X11/Applications
Requires:	%{name}-kmouth = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kmouth-i18n
Internationalization and localization files for kmouth.

%description kmouth-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmouth.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/* \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde

%if %{with i18n}
%find_lang desktop_kdeaccessibility	--with-kde
%endif

files="kmag \
kmousetool \
kmouth"

for i in $files; do
	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with i18n}
%files i18n -f desktop_kdeaccessibility.lang
%files kmag-i18n -f kmag.lang
%files kmousetool-i18n -f kmousetool.lang
%files kmouth-i18n -f kmouth.lang
%endif

%files kmag -f kmag_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_datadir}/apps/kmag
%{_desktopdir}/kde/kmag.desktop
%{_iconsdir}/[!l]*/*/apps/kmag.png

%files kmousetool -f kmousetool_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_datadir}/apps/kmousetool
%{_desktopdir}/kde/kmousetool.desktop
%{_iconsdir}/[!l]*/*/apps/kmousetool.png

%files kmouth -f kmouth_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_datadir}/apps/kmouth
%{_datadir}/config/kmouthrc
%{_desktopdir}/kde/kmouth.desktop
%{_iconsdir}/[!l]*/*/apps/kmouth.png
