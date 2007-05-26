Summary:	A C library for parsing and emitting YAML
Name:		yaml
Version:	0.0.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://pyyaml.org/download/libyaml/%{name}-%{version}.tar.gz
# Source0-md5:	8affdebeb0da9ed6a4cefba210b432d4
URL:		http://pyyaml.org/wiki/LibYAML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
YAML 1.1 parser and emitter written in C.

%package devel
Summary:	Header files and develpment documentation for yaml
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and develpment documentation for yaml.

%package static
Summary:	Static yaml library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static yaml library.

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
