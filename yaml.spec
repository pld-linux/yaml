Summary:	A C library for parsing and emitting YAML
Summary(pl.UTF-8):	Biblioteka C do analizy i wytwarzania YAML-a
Name:		yaml
Version:	0.1.6
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://pyyaml.org/download/libyaml/%{name}-%{version}.tar.gz
# Source0-md5:	5fe00cda18ca5daeb43762b80c38e06e
URL:		http://pyyaml.org/wiki/LibYAML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML 1.1 parser and emitter written in C.

%description -l pl.UTF-8
Napisana w C biblioteka analizująca i wytwarzająca danych w formacie
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
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libyaml-0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libyaml-0.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libyaml.so
%{_libdir}/libyaml.la
%{_includedir}/yaml.h
%{_pkgconfigdir}/yaml-0.1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libyaml.a
