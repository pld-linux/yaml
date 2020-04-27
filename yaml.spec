Summary:	A C library for parsing and emitting YAML
Summary(pl.UTF-8):	Biblioteka C do analizy i wytwarzania YAML-a
Name:		yaml
Version:	0.2.4
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/yaml/libyaml/releases
Source0:	https://github.com/yaml/libyaml/archive/%{version}/libyaml-%{version}.tar.gz
# Source0-md5:	64219701e897efb467d95123a165ca01
URL:		https://pyyaml.org/wiki/LibYAML
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML 1.1 parser and emitter written in C.

%description -l pl.UTF-8
Napisana w C biblioteka analizująca i wytwarzająca dane w formacie
YAML 1.1.

%package devel
Summary:	Header files for yaml library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki yaml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for yaml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yaml.

%package static
Summary:	Static yaml library
Summary(pl.UTF-8):	Statyczna biblioteka yaml
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static yaml library.

%description static -l pl.UTF-8
Statyczna biblioteka yaml.

%prep
%setup -q -n libyaml-%{version}

%build
%{__libtoolize}
%{__aclocal} -I config
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libyaml.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes License ReadMe.md announcement.msg
%attr(755,root,root) %{_libdir}/libyaml-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaml-0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyaml.so
%{_includedir}/yaml.h
%{_pkgconfigdir}/yaml-0.1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libyaml.a
