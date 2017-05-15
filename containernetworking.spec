%if 0%{?fedora}
%global with_debug   1
%global with_bundled 1
%else
%global with_debug   0
%global with_bundled 1
%endif

%if 0%{?with_debug}
# https://bugzilla.redhat.com/show_bug.cgi?id=995136#c12
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%global commit      0799f5732f2a11b329d9e3d51b9c8f2e3759f2ff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global shortname   cni
%global tag         0.5.1

# could also call this cni
Name:           containernetworking
Version:        %{tag}
Release:        1%{?dist}
Summary:        Libraries for writing plugins to configure network interfaces in Linux containers
License:        ASL 2.0 
URL:            https://github.com/containernetworking/cni
ExclusiveArch:  %{go_arches}

####################################
Source:     %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

####################################
BuildRequires: golang >= 1.7
BuildRequires: go-md2man
BuildRequires: go-bindata

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
%setup -q -n %{shortname}-%{commit}

%build 
./build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \n')" -v -x "$@"

%install 
mkdir -p %{buildroot}%{_libexecdir}/%{name} 
install -p -m 755 -t %{buildroot}%{_libexecdir}/%{name} bin/* 

##############################################
%files 
%license LICENSE
%doc *.md
%{_libexecdir}/%{name}/* 

%changelog 
* Sun May 07 2017 Timothy St. Clair <tstclair@heptio.com> - 0.5.2-1
- Initial release

