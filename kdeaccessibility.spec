
%define		_state		snapshots
%define		_ver		3.2.90
%define		_snap		040511
%define		_packager	adgor

%define		_minlibsevr	9:3.2.90.040508
%define		_minbaseevr	9:3.2.90.040508

Summary:	Accessibility support for KDE
Summary(pl):	U³atwienia dostêpu dla KDE
Name:		kdeaccessibility
Version:	%{_ver}.%{_snap}
Release:	2
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	97466b78dcee2d29505937c79919713d
URL:		http://www.kde.org/
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
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
Summary:	MouseTool - a program that clicks the mouse for you
Summary(pl):	MouseTool - narzêdzie do klikania myszk± bez naciskania jej przycisków
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmousetool
MouseTool is a program that clicks the mouse for you.

%description kmousetool -l pl
MouseTool to narzêdzie do klikania myszk± bez naciskania jej
przycisków.

%package kmouth
Summary:	A frontend for speech synthesizers
Summary(pl):	Frontend do syntezatorów mowy
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kmouth
A frontend for speech synthesizers.

%description kmouth -l pl
Frontend do syntezatorów mowy.

%prep
%setup -q -n %{name}-%{_snap}

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

# Workaround for doc caches (unsermake bug?)
cd doc
for i in `find . -name index.cache.bz2`; do
	install -c -p -m 644 $i $RPM_BUILD_ROOT%{_kdedocdir}/en/$i
done
cd -	 

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

mv $RPM_BUILD_ROOT%{_datadir}/applnk/Applications/* \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde

files="\
	kmag \
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
