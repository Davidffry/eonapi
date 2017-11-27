Summary:        API for the EON suite.
Name:           eonapi
Version:        1.0
Release:        2.eon
Source:         https://github.com/EyesOfNetworkCommunity/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}-%{release}.tar.gz
Group:          Applications/System
License:        GPL
Vendor:         EyesOfNetwork Community
URL:            https://github.com/EyesOfNetworkCommunity/eonapi
Requires:	eonweb

BuildRoot:      %{_tmppath}/%{name}-%{version}-root

%define eondir          /srv/eyesofnetwork
%define	datadir		%{eondir}/%{name}

%description
Eyes Of Network includes a web-based "RESTful" API (Application Programming Interface) called EONAPI that enables external programs to access information from the monitoring database and to manipulate objects inside the databases of EON suite.

%prep
%setup -q

%build

%install
install -d -m0755 %{buildroot}%{datadir}
install -d -m0755 %{buildroot}%{_sysconfdir}/httpd/conf.d
cp -afv ./* %{buildroot}%{datadir}
install -m 640 eonapi.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

%post
systemctl restart httpd

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,eyesofnetwork)
%{eondir}
%defattr(-,root,root)
%{_sysconfdir}/httpd/conf.d/eonapi.conf

%changelog
* Mon Nov 27 2017 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.0-2
- Fix installation for EyesOfNetwork 5.2.

* Thu Oct 26 2017 Michael Aubertin <michael.aubertin@gmail.com> - 1.0-1
- Fix permission issue.

* Wed Oct 25 2017 Lucas Salinas - 1.0-0
-Package for EyesOfNetwork API.
