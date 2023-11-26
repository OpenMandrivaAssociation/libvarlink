%define major           0
%define libname         %mklibname varlink %{major}
%define develname       %mklibname varlink -d

Name:           libvarlink
Version:        23
Release:        %mkrel 1
Summary:        Varlink C Library
License:        ASL 2.0
Group:		Networking/Other
URL:            https://github.com/varlink/libvarlink
Source0:        https://github.com/varlink/libvarlink/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  gcc
# For tests
BuildRequires:  locales-de

%description
C implementation of the Varlink protocol and command line tool.

%package        -n %{libname}
Summary:        Development files for %{name}
Provides:       %{name} = %{version}-%{release}

%description    -n %{libname}
C implementation of the Varlink protocol.

%package        -n %{develname}
Summary:        Development files for %{name}
Provides:       %{name}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description    -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n varlink
Summary:        Varlink command line tool
Obsoletes:	%{name}-util < 23
Provides:	libvarlink-util = %{version}-%{release}

%description    -n varlink
Varlink command line tool.

%prep
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files -n %{libname}
%license LICENSE
%{_libdir}/libvarlink.so.%{major}{,.*}

%files -n varlink
%{_bindir}/varlink
%{_datadir}/bash-completion/completions/varlink
%{_datadir}/vim/vimfiles/after/*

%files -n %{develname}
%{_includedir}/varlink.h
%{_libdir}/libvarlink.so
%{_libdir}/pkgconfig/libvarlink.pc
