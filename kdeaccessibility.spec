
%define		_snap	030918
%define		_ver	3.1.91

Summary:	TODO
Summary(pl):	TODO
Name:		kdeaccessibility
Version:	%{_ver}.%{_snap}
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	7590003d7dae018265e963e1c25213a4
Patch0:		%{name}-vcategories.patch
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         no_install_post_chrpath         1

%description
TODO

%description -l pl
TODO

%package kmag
Summary:        TODO                                                            
Summary(pl):    TODO
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmag
TODO.

%description kmag -l pl
TODO.

%package kmousetool
Summary:        TODO                                                            
Summary(pl):    TODO
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmousetool
TODO.

%description kmousetool -l pl
TODO.

%package kmouth
Summary:        TODO                                                            
Summary(pl):    TODO
Group:          X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kmouth
TODO.

%description kmouth -l pl
TODO.

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
