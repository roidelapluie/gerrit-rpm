#!/bin/bash

spec=/vagrant/gerrit.spec
yum install -y rpm-build java-1.7.0 spectool git

(
mkdir -p /root/rpmbuild/SOURCES
cd /root/rpmbuild/SOURCES
spectool -g $spec

)
rpmbuild -v -bb $spec

