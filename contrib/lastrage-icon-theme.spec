%global         tname LaStrange
# https://github.com/zibonbadi/lastrange-icons/commit/edfca5fbd7fd96b61dee1f25e9db7ac91b61ec41
%global commitdate 20210113
%global commit0 edfca5fbd7fd96b61dee1f25e9db7ac91b61ec41
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           lastrange-icon-theme
Version:        %{commitdate}
Release:        0.1.git%{shortcommit0}%{?dist}
Summary:        A clean, simple icon theme for easy and focused computing

License:        GPLv3+
URL:            https://github.com/zibonbadi/lastrange-icons
Source0:        https://github.com/zibonbadi/lastrange-icons/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Source1:        https://ftp.gnu.org/gnu/Licenses/lgpl-3.0.txt
BuildArch:      noarch

BuildRequires:  coreutils

Requires:       hicolor-icon-theme

%description
A clean, simple icon theme for easy and focused computing. Originally
developed for dogfooding, the theme aims to be simple in both design
and implementation while keeping a distinctly Unix-like aesthetic
...with some modern quality-of-life considerations.

The name is a reference to Tom LaStrange, the inventor of the TWM
window manager, which served as the main inspiration for the desktop
theme. Other influences include printed paper, the Athena widget
library and the Amiga Workbench

%prep
%autosetup -p1 -n lastrange-icons-%{commit0}
find . -executable -type f -exec chmod --verbose a-x '{}' ';'
cp -a %{SOURCE1} LICENSE

%build

%install
mkdir -p %{buildroot}%{_datadir}/icons/%{tname}
cp -a index.theme scalable %{buildroot}%{_datadir}/icons/%{tname}

%if 0%{?fedora} < 28 || 0%{?rhel} < 8
%post
touch --no-create %{_datadir}/icons/%{tname} &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/%{tname} &>/dev/null ||:
    gtk-update-icon-cache %{_datadir}/icons/%{tname} &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/%{tname} &>/dev/null || :
%endif

%files
%license LICENSE
%doc README.md banner.png
%dir %{_datadir}/icons/%{tname}
%{_datadir}/icons/%{tname}/scalable
%{_datadir}/icons/%{tname}/index.theme
%ghost %{_datadir}/icons/%{tname}/icon-theme.cache

%changelog
* Fri Apr 02 2021 Joel Barrios <http://www.alcancelibre.org/> - 20210113-0.1.gitedfca5f
- Initial spec file.
