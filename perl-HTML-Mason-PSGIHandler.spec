#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	Mason-PSGIHandler
Summary:	HTML::Mason::PSGIHandler - PSGI handler for HTML::Mason
Name:		perl-HTML-Mason-PSGIHandler
Version:	0.53
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
URL:		http://search.cpan.org/dist/HTML-Mason-PSGIHandler/
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f5982567c24f86b41c4cad43fd07c16c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CGI-PSGI
BuildRequires:	perl-HTML-Mason >= 1.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# provided indirectly by perl(HTML::Mason::CGIHandler)
%define		_noautoreq_perl	HTML::Mason::Request::CGI HTML::Mason::Request::PSGI

%description
HTML::Mason::PSGIHandler is a PSGI handler for HTML::Mason. It's based
on HTML::Mason::CGIHandler and allows you to process Mason templates
on any web servers that support PSGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/HTML/Mason/PSGIHandler.pm
%dir %{perl_vendorlib}/HTML/Mason/PSGIHandler
%{perl_vendorlib}/HTML/Mason/PSGIHandler/Streamy.pm
%{_mandir}/man3/*
