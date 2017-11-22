Summary: Gluster 3.13 (Short Term Stable) packages from the CentOS Storage SIG repository
Name: centos-release-gluster313
Version: 0.9
Release: 1%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Gluster-3.13.repo

BuildArch: noarch

# This provides the public key to verify the RPMs
Requires: centos-release-storage-common

# Users can install centos-release-gluster to get the latest, but we do not
# want to have 3.13 (Short Term Stable) to be selected when users do install
# the virtual centos-release-gluster package.
#
# If users want to test other projects with a centos-release-gluster
# dependency, they will need to install centos-release-gluster313 or similar in
# addition to centos-release-gluster313
#
#Provides: centos-release-gluster = 3.13
#Conflicts: centos-release-gluster < 3.13
#Obsoletes: centos-release-gluster < 3.13

%description
yum configuration for Gluster 3.13 packages from the CentOS Storage SIG.
Gluster 3.13 is a Short Term Stable release and will receive updates for only 3
months (until the next Gluster release is available). For more details about
the Long Term Stable and Short Term Stable release schedule, see
https://www.gluster.org/community/release-schedule

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.13.repo

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Gluster-3.13.repo

%changelog
* Wed Nov 22 2017 Niels de Vos <ndevos@redhat.com> - 0.9-1
- Initial version based on centos-release-gluster311
- Only the centos-gluster313-test repo is enabled during Beta
