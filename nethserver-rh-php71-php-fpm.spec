Name: nethserver-rh-php71-php-fpm
Version: 1.1.2
Release: 1%{?dist}
Summary: NethServer rh-php71-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php71, rh-php71-php-fpm
Requires: rh-php71-php-bcmath, rh-php71-php-gd
Requires: rh-php71-php-ldap, rh-php71-php-enchant, rh-php71-php-mbstring
Requires: rh-php71-php-pdo, rh-php71-php-mysqlnd
Requires: rh-php71-php-soap, rh-php71-php-pgsql
Requires: rh-php71-php-pecl-apcu, rh-php71-php-intl
Requires: rh-php71-php-opcache

%description
Basic support for PHP 7.1 using SCL

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Fri Apr 03 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Remove dismissed dependencies: imap and tidy (#7) 

* Wed Dec 18 2019 Davide Principi <davide.principi@nethesis.it> - 1.1.1-1
- Rh-php7x: opcache dependency - NethServer/dev#5986

* Tue Dec 17 2019 Davide Principi <davide.principi@nethesis.it> - 1.1.0-1
- Rh-php7x: add Intl and apcu - NethServer/dev#5987
- Rh-PHP7x: RunTime Directory Creation - NethServer/dev#5992

* Wed Dec 11 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1
- Change PHP-FPM version in Web server app - NethServer/dev#5912

* Tue Mar 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Nextcloud: upgrade to v13 & optimizations - NethServer/dev#5427

* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- First release
- Nextcloud 11 - NethServer/dev#5242

