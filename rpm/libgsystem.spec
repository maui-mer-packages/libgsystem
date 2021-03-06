# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       libgsystem

# >> macros
# << macros

Summary:    GIO-based library with Unix/Linux specific API
Version:    2014.2
Release:    1
Group:      System/GUI/Other
License:    LGPLv2+
URL:        https://wiki.gnome.org/Projects/LibGSystem
Source0:    %{name}-%{version}.tar.xz
Source100:  libgsystem.yaml
Source101:  libgsystem-rpmlintrc
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libattr-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  systemd-devel

%description
LibGSystem is a GIO-based library targeted primarily
for use by operating system components.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   gobject-introspection-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
mkdir m4
# << build pre

%reconfigure --disable-static
make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_libdir}/%{name}.so.*
%{_libdir}/girepository-*/*.typelib
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-*/*.gir
# >> files devel
# << files devel
