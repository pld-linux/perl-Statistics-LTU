%define	pdir	Statistics
%define	pnam	LTU
%include	/usr/lib/rpm/macros.perl
Summary:	Statistics-LTU perl module
Summary(pl):	Modu³ perla Statistics-LTU
Name:		perl-Statistics-LTU
Version:	2.8
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
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

gzip -9nf README.LTU ltu.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Statistics/LTU.pm
%{perl_sitelib}/Statistics/weather.pl
%{_mandir}/man3/*
