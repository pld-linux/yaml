Summary:	A C library for parsing and emitting YAML
Summary(pl.UTF-8):	Biblioteka C do analizy i wytwarzania YAML-a
Name:		yaml
Version:	0.1.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://pyyaml.org/download/libyaml/%{name}-%{version}.tar.gz
# Source0-md5:	f6c9b5c2b0f6919abd79f5fd059b01dc
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
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for yaml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki yaml.

%package static
Summary:	Static yaml library
Summary(pl.UTF-8):	Statyczna biblioteka yaml
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
