Name: nethserver-rh-php71-php-fpm
Version: 1.0.0
Release: 1%{?dist}
Summary: NethServer rh-php71-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: rh-php71, rh-php71-php-fpm
Requires: rh-php71-php-bcmath, rh-php71-php-gd, sclo-php71-php-imap
Requires: rh-php71-php-ldap, rh-php71-php-enchant, rh-php71-php-mbstring
Requires: rh-php71-php-pdo, sclo-php71-php-tidy, rh-php71-php-mysqlnd
Requires: rh-php71-php-soap, rh-php71-php-pgsql

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
* Tue Mar 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Nextcloud: upgrade to v13 & optimizations - NethServer/dev#5427

* Tue Apr 04 2017 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- First release
- Nextcloud 11 - NethServer/dev#5242

