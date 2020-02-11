Name:           calamares-settings-kamarada
Version:        15.1
Release:        0
Summary:        Kamarada theme and settings for the Calamares Installer
License:        GPL-2.0+
Group:          System/Management
Url:            https://github.com/kamarada/%{name}
Source:         https://github.com/kamarada/%{name}/archive/15.1-dev.tar.gz#/%{name}.tar.gz

BuildArch:      noarch
BuildRequires:  libqt5-linguist

Requires:       calamares
Requires:       calamares-branding-upstream


%description
Calamares is a generic installer framework for Linux distributions. By default,
it contains a set of boilerplate wording and images. This package provides the
Kamarada artwork and settings for Calamares.

It also serves as an example for how derivatives can create their own
calamares-settings packages.


%prep
%setup -q -n %{name}


%build
cd etc/calamares/branding/Kamarada/lang/
lrelease-qt5 *.ts
rm *.ts


%install
cp -r {etc,usr} %{buildroot}/


%files
/etc/calamares/
/usr/sbin/kamarada-postinstall.sh


%changelog

