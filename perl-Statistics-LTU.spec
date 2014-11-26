%define		pdir	Statistics
%define		pnam	LTU
%include	/usr/lib/rpm/macros.perl
Summary:	Statistics::LTU perl module
Summary(pl.UTF-8):	Moduł perla Statistics::LTU
Name:		perl-Statistics-LTU
Version:	2.8
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22d194baec8ef7696b57a4a365a0850d
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Statistics-LTU/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics::LTU defines methods for creating, destroying, training and
testing Linear Threshold Units.

%description -l pl.UTF-8
Statistics::LTU definiuje metody tworzenia, niszczenia i testowania
LTU (Linear Treshold Units).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.LTU ltu.doc
%{perl_vendorlib}/Statistics/LTU.pm
%{perl_vendorlib}/Statistics/weather.pl
%{_mandir}/man3/*
