Name:           sealfail-scap-profile
Version:        1.1
Release:        1
Summary:        The SEALFAIL security profile for OpenSCAP.
License:        GPLv3

Source0: 	%{name}.tar.xz

BuildArch:      noarch

%description
The SEALFAIL security profile for OpenSCAP.

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}/usr/share/xml/scap/sealfail/
install -m 0644 sealfail.xml %{buildroot}/usr/share/xml/scap/sealfail/sealfail.xml

%files
%attr(0644,root,root) /usr/share/xml/scap/sealfail/sealfail.xml


%changelog
* Sat Jul 30 2022 Sasha Emily Chelsea Murgia - 1.1-1
- Removed unused rules
- Changed profile description
* Sat Jul 23 2022 Sasha Emily Chelsea Murgia - 1-1
- Initial release
