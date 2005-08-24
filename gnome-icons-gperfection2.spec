#
%define		realname	gperfection2
#
Summary:	Gperfection2 GNOME Icons
Summary(pl):	Zestaw ikonek Gperfection2 dla GNOME
Name:		gnome-icons-gperfection2
Version:	2.3
Release:	1
License:	GPL
Group:		X11/Amusements
Source0:	http://members.shaw.ca/titancreations/gnome/%{realname}-%{version}.tar.bz2
# Source0-md5:	d986acad9835c14e5c6bcbd4e1119f62
URL:		http://gnome-look.org/content/show.php?content=22989
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The set is an extensive expansion on the default icon theme designed
by Jakub Steiner.

%description -l pl
Zestaw jest obszernym rozszerzeniem standardowego motywu stworzonego
przez Jakuba Streinera.

%prep
%setup -q -n %{realname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

cp -af . $RPM_BUILD_ROOT%{_iconsdir}/%{realname}

# remove gentoo icons
rm -f $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/{24x24,48x48,72x72}/apps/gnome-main-menu.png
rm -f $RPM_BUILD_ROOT%{_iconsdir}/%{realname}/{12x12,20x20,24x24,32x32,36x36,48x48}/emblems/emblem-gentoo.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_iconsdir}/%{realname}
%dir %{_iconsdir}/%{realname}/12x12
%dir %{_iconsdir}/%{realname}/16x16
%dir %{_iconsdir}/%{realname}/20x20
%dir %{_iconsdir}/%{realname}/24x24
%dir %{_iconsdir}/%{realname}/32x32
%dir %{_iconsdir}/%{realname}/36x36
%dir %{_iconsdir}/%{realname}/48x48
%dir %{_iconsdir}/%{realname}/72x72
%dir %{_iconsdir}/%{realname}/scalable
%{_iconsdir}/%{realname}/index.theme
%{_iconsdir}/%{realname}/12x12/devices
%{_iconsdir}/%{realname}/12x12/emblems
%{_iconsdir}/%{realname}/12x12/filesystems
%{_iconsdir}/%{realname}/12x12/mimetypes
%{_iconsdir}/%{realname}/16x16/apps
%{_iconsdir}/%{realname}/16x16/devices
%{_iconsdir}/%{realname}/16x16/filesystems
%{_iconsdir}/%{realname}/16x16/gtk
%{_iconsdir}/%{realname}/16x16/mimetypes
%{_iconsdir}/%{realname}/16x16/stock
%{_iconsdir}/%{realname}/20x20/apps
%{_iconsdir}/%{realname}/20x20/devices
%{_iconsdir}/%{realname}/20x20/emblems
%{_iconsdir}/%{realname}/20x20/filesystems
%{_iconsdir}/%{realname}/20x20/gtk
%{_iconsdir}/%{realname}/20x20/stock
%{_iconsdir}/%{realname}/24x24/apps
%{_iconsdir}/%{realname}/24x24/devices
%{_iconsdir}/%{realname}/24x24/emblems
%{_iconsdir}/%{realname}/24x24/filesystems
%{_iconsdir}/%{realname}/24x24/gtk
%{_iconsdir}/%{realname}/24x24/mimetypes
%{_iconsdir}/%{realname}/24x24/stock
%{_iconsdir}/%{realname}/32x32/apps
%{_iconsdir}/%{realname}/32x32/emblems
%{_iconsdir}/%{realname}/32x32/filesystems
%{_iconsdir}/%{realname}/32x32/gtk
%{_iconsdir}/%{realname}/32x32/stock
%{_iconsdir}/%{realname}/36x36/apps
%{_iconsdir}/%{realname}/36x36/devices
%{_iconsdir}/%{realname}/36x36/emblems
%{_iconsdir}/%{realname}/36x36/filesystems
%{_iconsdir}/%{realname}/36x36/mimetypes
%{_iconsdir}/%{realname}/36x36/stock
%{_iconsdir}/%{realname}/48x48/apps
%{_iconsdir}/%{realname}/48x48/devices
%{_iconsdir}/%{realname}/48x48/emblems
%{_iconsdir}/%{realname}/48x48/filesystems
%{_iconsdir}/%{realname}/48x48/gtk
%{_iconsdir}/%{realname}/48x48/mimetypes
%{_iconsdir}/%{realname}/48x48/stock
%{_iconsdir}/%{realname}/72x72/apps
%{_iconsdir}/%{realname}/72x72/filesystems
%{_iconsdir}/%{realname}/72x72/gtk
%{_iconsdir}/%{realname}/scalable/filesystems
