%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-LTU perl module
Summary(pl):	Modu� perla Statistics-LTU
Name:		perl-Statistics-LTU
Version:	2.8
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Statistics/Statistics-LTU-%{version}.tar.gz
Patch0:		perl-Statistics-LTU-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Statistics-LTU defines methods for creating, destroying, training and
testing Linear Threshold Units.

%description -l pl
Statistics-LTU definiuje metody tworzenia, niszczenia i testowania LTU
(Linear Treshold Units).

%prep
%setup -q -n Statistics-LTU-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Statistics/LTU
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README.LTU ltu.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README.LTU,ltu.doc}.gz

%{perl_sitelib}/Statistics/LTU.pm
%{perl_sitelib}/Statistics/weather.pl
%{perl_sitearch}/auto/Statistics/LTU

%{_mandir}/man3/*
