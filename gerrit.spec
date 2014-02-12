Summary: Web based code review and project management for Git based projects. 
Name: gerrit
Version: 2.8.1
Release: 1
License: Apache License 2.0
Group: Applications/Codereview
Source: http://gerrit-releases.storage.googleapis.com/gerrit-%{version}.war
URL: https://code.google.com/p/gerrit
Vendor: Gerrit Contributors
Packager: Julien Pivotto <roidelapluie@inuits.eu>
Requires: java-1.7.0 git

%description
Gerrit is a web based code review system, facilitating online code reviews for projects using the Git version control system.

Gerrit makes reviews easier by showing changes in a side-by-side display, and allowing inline comments to be added by any reviewer.

Gerrit simplifies Git based project maintainership by permitting any authorized user to submit changes to the master Git repository, rather than requiring all approved changes to be merged in by hand by the project maintainer. This functionality enables a more centralized usage of Git.

%prep -T

java -jar %{_sourcedir}/gerrit-%{version}.war init -d ${RPM_BUILD_ROOT}/opt/gerrit
${RPM_BUILD_ROOT}/opt/gerrit/bin/gerrit.sh stop
rm ${RPM_BUILD_ROOT}/opt/gerrit/etc/secure.config
rm ${RPM_BUILD_ROOT}/opt/gerrit/etc/ssh_host_key
rm -rf ${RPM_BUILD_ROOT}/opt/gerrit/cache/*

%post
ssh-keygen -N '' -f /opt/gerrit/etc/host_key
mv /opt/gerrit/etc/host_key /opt/gerrit/etc/ssh_host_key

%files
/opt/gerrit/lib
/opt/gerrit/bin
%dir /opt/gerrit/data
%ghost /opt/gerrit/git
%dir /opt/gerrit/cache
/opt/gerrit/plugins
%config /opt/gerrit/etc
%dir /opt/gerrit/tmp
%ghost /opt/gerrit/logs
%ghost /opt/gerrit/db
/opt/gerrit/static

