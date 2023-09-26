%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20230925

Name: plasma6-ocean-sounds
Version: 5.240.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/ocean-sound-theme/-/archive/
%else
#Source0: https://download.kde.org/%{stable}/plasma/%(echo %{version}|cut -d. -f1-3)/ocean-sounds-%{version}.tar.xz
%endif
Summary: Ocean Sound Theme for Plasma
URL: https://invent.kde.org/plasma/ocean-sound-theme
License: CC-BY-SA-4.0
Group: Graphical desktop/KDE
BuildArch: noarch
BuildRequires: cmake ninja extra-cmake-modules
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)

%description
Ocean Sound Theme for Plasma

%prep
%autosetup -p1 -n ocean-sounds-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/sounds/ocean/*
