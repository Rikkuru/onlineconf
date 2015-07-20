Name:           onlineconf-admin
Version:        %{__version}
Release:        %{__release}%{?dist}

Summary:        onlineconf-admin application server
License:        BSD
Group:          MAILRU

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
AutoReq:        0
BuildRequires:  mr-rpm-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl-List-MoreUtils
Requires:       perl-Log-Dispatch
Requires:       perl-Mojolicious
Requires:       perl-Mojolicious-Plugin-MysqlBasicAuth
Requires:       perl-Starman
Requires:       perl-YAML
Requires:       perl-Mouse
Requires:       perl-JSON
Requires:       perl-JSON-XS
Requires:       perl-MR-ChangeBot-Database
Requires:       perl-MR-DBI >= 20120606.1301
Requires:       mailru-initd-functions >= 1.11
Requires:       onlineconf-updater
Conflicts:      perl-MR-Onlineconf < 20120319.1930

%description
onlineconf-admin application server. Built from revision %{__revision}.

%prep
%setup -n onlineconf/admin

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%__make %{?_smp_mflags}

%install
[ "%{buildroot}" != "/" ] && rm -fr %{buildroot}
%__make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%__chmod -R u+w $RPM_BUILD_ROOT/*
%{__rm} %{buildroot}/%{_bindir}/onlineconf-migration
%{__mkdir} -p %{buildroot}/%{_initrddir} %{buildroot}/%{_localetcdir} %{buildroot}/%{_sysconfdir}/{cron.d,nginx} %{buildroot}/usr/local/www/onlineconf/static
%{__install} -m 644 etc/%{name}.yaml %{buildroot}/%{_localetcdir}/%{name}.yaml
%{__install} -m 755 init.d/%{name} %{buildroot}/%{_initrddir}/%{name}
%{__mv} %{buildroot}/%{_bindir} %{buildroot}/%{_localbindir}
%{__cp} -r static/* $RPM_BUILD_ROOT/usr/local/www/onlineconf/static/
%{__cp} -f etc/nginx.conf $RPM_BUILD_ROOT/etc/nginx/onlineconf.conf
echo "@daily root %{_initrddir}/%{name} remove-old-logs" > %{buildroot}/%{_sysconfdir}/cron.d/%{name}
%_fixperms %{buildroot}/*

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/MR/OnlineConf/Admin
%{_localbindir}/onlineconf-admin
%{_localbindir}/onlineconf-import
%{_initrddir}/%{name}
%config(noreplace) %{_localetcdir}/%{name}.yaml
%config(noreplace) %{_sysconfdir}/nginx/*
/usr/local/www/onlineconf/static/*
%{_sysconfdir}/cron.d/%{name}
%{_mandir}/*/*

%post
chkconfig --add %{name}
chkconfig %{name} on

%preun
if [ $1 -eq 0 ]; then
    service %{name} stop > /dev/null
    chkconfig --del %{name}
fi

%package -n onlineconf-selftest
Summary:    onlineconf monitoring support script
Group:      MAILRU
Requires:   perl-Log-Dispatch
Requires:   onlineconf-admin >= %{__version}
Requires:   perl-YAML

%description -n onlineconf-selftest
onlineconf-selftest - onlineconf monitoring support script.

%files -n onlineconf-selftest
%defattr(-,root,root,-)
%{_localbindir}/onlineconf-selftest

%changelog
* Mon Mar 19 2012 Aleksey Mashanov <a.mashanov@corp.mail.ru>
- initial version
