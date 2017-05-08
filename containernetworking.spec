%global commit      137b4975ecab6e1f0c24c1e3c228a50a3cfba75e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global tag         0.5.2

# could also call this cni
Name:       containernetworking
Version:    %{tag}
Release:    1%{?dist}
Summary:    Libraries for writing plugins to configure network interfaces in Linux containers
License:    ASL 2.0 
URL:        https://github.com/containernetworking/cni

# ExclusiveArch: x86_64

####################################
Source:     %{url}/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

####################################
# Patch0: 

####################################
# BuildRequires
# Requires


%description 
The CNI (Container Network Interface) project consists of a specification 
and libraries for writing plugins to configure network interfaces in Linux 
containers, along with a number of supported plugins. CNI concerns itself 
only with network connectivity of containers and removing allocated resources 
when the container is deleted.

##############################################
%package devel 
Summary: %{summary}
BuildArch: noarch       

Provides: golang(%{import_path}/libcni) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/invoke) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ip) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ipam) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/ns) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/skel) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/testutils) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/types) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/utils) = %{version}-%{release}
Provides: golang(%{import_path}/pkg/version) = %{version}-%{release}

%description devel
Libraries for building packages importing containernetworking/cni.
Currently, the devel is not suitable for development.
It is meant only as a buildtime dependency for other projects.

##############################################
%prep 
%setup -q -n %{name}-%{commit}
./build.sh
outpath = "bin" 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/bridge 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/cnitool 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/dhcp
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/flannel 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/host-local
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/ipvlan 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/loopback 
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/macvlan
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/noop
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/ptp
install -p -m 755 -t %{buildroot}%{_bindir} ${outpath}/tuning

##############################################
%files 
%license LICENSE
%doc *.md
%{_bindir}/bridge 
%{_bindir}/cnitool 
%{_bindir}/dhcp
%{_bindir}/flannel 
%{_bindir}/host-local
%{_bindir}/ipvlan 
%{_bindir}/loopback 
%{_bindir}/macvlan
%{_bindir}/noop
%{_bindir}/ptp
%{_bindir}/tuning

%pre 
%post 
%preun 
%postun 

%changelog 
* Sun May 07 2017 Timothy St. Clair <tstclair@heptio.com> - 0.5.2-1
- Initial release

