
%define		_state		stable
%define		_ver		3.3.0

%define		_minlibsevr	9:3.3.0
%define		_minbaseevr	9:3.3.0

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	%{_ver}
Release:	3
License:	GPL
Group:		X11/Applications
Icon:		kde-access.xpm
Source0:        ftp://ftp.kde.org/pub/kde/%{_state}/3.3/src/%{name}-%{version}.tar.bz2
# Source0-md5:	17dc4ae94d0307a00e2b676818f49d63
#Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_ver}-%{_snap}.tar.bz2
URL:		http://www.kde.org/
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accessibility support for KDE.

%description -l pl
U³atwienia dostêpu dla KDE.

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

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

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

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files kmag -f kmag.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_datadir}/apps/kmag
%{_desktopdir}/kde/kmag.desktop
%{_iconsdir}/[!l]*/*/apps/kmag.png

%files kmousetool -f kmousetool.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_datadir}/apps/kmousetool
%{_desktopdir}/kde/kmousetool.desktop
%{_iconsdir}/[!l]*/*/apps/kmousetool.png

%files kmouth -f kmouth.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_datadir}/apps/kmouth
%{_datadir}/config/kmouthrc
%{_desktopdir}/kde/kmouth.desktop
%{_iconsdir}/[!l]*/*/apps/kmouth.png
