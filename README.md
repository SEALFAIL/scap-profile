![SEALFAIL logo](logo-transparent.png) 

# SEALFAIL SCAP PROFILE

This repository contains the OpenSCAP security profile used by SEALFAIL.

The profile is based on the STIG GUI draft profile for Enterprise Linux 9.

## Usage

The RPM build process requires `rpm-build`. The script has only been tested on **AlmaLinux 9.**

Build the RPM with the following command:

`# ./build.sh`

Install the RPM with the following command:

`# rpm -i ~/rpmbuild/RPMS/noarch/sealfail-scap-profile-*.rpm`

Use the profile with the following command:

`# oscap xccdf eval --profile xccdf_org.sealfail_profile_workstation /usr/share/xml/scap/sealfail/sealfail.xml`

## Contributing

Refer to the SEALFAIL project [documentation repository](https://github.com/SEALFAIL/Documentation) for information regarding contributions.

## Code of conduct (COC)

Contributors are to follow the code of conduct (COC) located at the SEALFAIL project [documentation repository](https://github.com/SEALFAIL/Documentation).
