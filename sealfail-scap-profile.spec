Name:           sealfail-scap-profile
Version:        1
Release:        1
Summary:        The SEALFAIL security profile for OpenSCAP.
License:        GPLv3

Source0: 	%{name}.tar.xz

BuildArch:      noarch

%description
The SEALFAIL security profile for OpenSCAP.

%prep
cp %SOURCE0 .
cp %SOURCE1 .


%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xml/scap/%{name}
cp ssg-sealfail9-ds.xml $RPM_BUILD_ROOT/%{_datadir}/xml/scap/%{name}/
cp tailoring-xccdf.xml $RPM_BUILD_ROOT/%{_datadir}/xml/scap/%{name}/


%files
%{_datadir}/xml/scap/%{name}/ssg-sealfail9-ds.xml
%{_datadir}/xml/scap/%{name}/tailoring-xccdf.xml


%changelog
* Sat Jul 23 2022 Sasha Emily Chelsea Murgia - 1-1
- Initial release
