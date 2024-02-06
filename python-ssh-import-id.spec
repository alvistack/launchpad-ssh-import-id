# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-ssh-import-id
Epoch: 100
Version: 5.11
Release: 1%{?dist}
BuildArch: noarch
Summary: Securely retrieve an SSH public key and install it locally
License: GPL-3.0
URL: https://git.launchpad.net/ssh-import-id/
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-distro
BuildRequires: python3-setuptools

%description
This utility will securely contact a public keyserver (Launchpad.net by
default, but Github.com is also supported), retrieve one or more user's
public keys, and append these to the current user's
~/.ssh/authorized_keys file.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%package -n ssh-import-id
Summary: Securely retrieve an SSH public key and install it locally
Requires: ca-certificates
Requires: openssh-clients
Requires: python3
Requires: python3-distro
Requires: wget
Provides: ssh-import-id = %{epoch}:%{version}-%{release}
Provides: python3dist(ssh-import-id) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ssh-import-id = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ssh-import-id) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ssh-import-id = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ssh-import-id) = %{epoch}:%{version}-%{release}

%description -n ssh-import-id
This utility will securely contact a public keyserver (Launchpad.net by
default, but Github.com is also supported), retrieve one or more user's
public keys, and append these to the current user's
~/.ssh/authorized_keys file.

%files -n ssh-import-id
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*

%changelog
