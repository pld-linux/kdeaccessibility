#
%define		_state		stable
%define		_ver		3.2.3

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	%{_ver}
Release:	0.1
License:	GPL
Group:		X11/Applications
#Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	18a949124ff7f5ba8c7e7d107d8ec794
Icon:		kde-access.xpm
# Patch100:		%{name}-branch.diff
URL:		http://www.kde.org/
BuildRequires:  autoconf
BuildRequires:  unsermake >= 040511
BuildRequires:  automake
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
MouseTool is a program that clicks the mouse for you. KMouseTool clicks the mouse whenever the mouse cursor pauses briefly. It was designed to help those with repetitive strain injuries, for whom pressing buttons hurts. It can also drag the mouse, although this takes a bit more practice. 

%description kmousetool -l pl
MouseTool to narzêdzie do klikania myszk± bez naciskania jej
przycisków.

%package kmouth
Summary:	A frontend for speech synthesizers
Summary(pl):	Frontend do syntezatorów mowy
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmouth
A frontend for speech synthesizers. It is a program that enables persons that cannot speak to let their computers speak. It includes a history of spoken sentences from which the user can select sentences to be re-spoken. 

Note that KMouth does not include speech synthesizer. Instead it requires a speech synthesizer installed in the system. 

%description kmouth -l pl
Frontend do syntezatorów mowy.

%prep
%setup -q
#%%patch100 -p1

%build
cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/* \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT


%files kmag 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_datadir}/apps/kmag
%{_desktopdir}/kde/kmag.desktop
%{_iconsdir}/[!l]*/*/apps/kmag.png
%{_kdedocdir}/en/kmag

%files kmousetool
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_datadir}/apps/kmousetool
%{_desktopdir}/kde/kmousetool.desktop
%{_iconsdir}/[!l]*/*/apps/kmousetool.png
%{_kdedocdir}/en/kmousetool

%files kmouth 
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_datadir}/apps/kmouth
%{_datadir}/config/kmouthrc
%{_desktopdir}/kde/kmouth.desktop
%{_iconsdir}/[!l]*/*/apps/kmouth.png
%{_kdedocdir}/en/kmouth
