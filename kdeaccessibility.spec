
%define		_ver	3.1.92
%define		_snap	031024

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	%{_ver}.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	a57750979f966fe77570b8948b226e29
Patch0:		%{name}-vcategories.patch
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         no_install_post_chrpath         1

%description
Accessibility support for KDE.

%description -l pl
U³atwienia dostêpu dla KDE.

%package kmag
Summary:        A KDE magnifying tool
Summary(pl):    Lupa dla ¶rodowiska KDE
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmag
A KDE magnifying tool.

%description kmag -l pl
Lupa dla ¶rodowiska KDE.

%package kmousetool
Summary:        MouseTool - a program that clicks the mouse for you
Summary(pl):    MouseTool - narzêdzie do klikania myszk± bez naciskania jej przycisków
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmousetool
MouseTool is a program that clicks the mouse for you.

%description kmousetool -l pl
MouseTool to narzêdzie do klikania myszk± bez naciskania jej
przycisków.

%package kmouth
Summary:        A frontend for speech synthesizers
Summary(pl):    Frontend do syntezatorów mowy
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmouth
A frontend for speech synthesizers.

%description kmouth -l pl
Frontend do syntezatorów mowy.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_docdir}/kde/HTML

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_applnkdir}/Applications/* \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde

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
