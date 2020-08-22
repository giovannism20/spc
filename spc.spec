# Generated by go2rpm 1
%bcond_without check

# https://github.com/dvdmuckle/spc

%global goipath         github.com/dvdmuckle/spc
%global tag             v0.4.1
%gometa
Version:                %{tag}


%global common_description %{expand:
A lightweight multiplatform CLI for Spotify.}

%global godocs          README.md

Name:           spc
Release:        1%{?dist}
Summary:        A lightweight multiplatform CLI for Spotify

# Upstream license specification: Apache-2.0
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

# Using go mod vendor to get the build requirements, since
# we would have to anyways for all the packages that don't
# have Fedora packages
# BuildRequires:  golang(github.com/golang/glog)
# Package does not exist: BuildRequires:  golang(github.com/ktr0731/go-fuzzyfinder)
# Package does not exist: BuildRequires:  golang(github.com/markbates/goth/providers/spotify)
# BuildRequires:  golang(github.com/mitchellh/go-homedir)
# BuildRequires:  golang(github.com/spf13/cobra)
# BuildRequires:  golang(github.com/spf13/viper)
# Package does not exist: BuildRequires:  golang(github.com/zmb3/spotify)
# BuildRequires:  golang(golang.org/x/oauth2)
BuildRequires:  git

%description
%{common_description}

%gopkg

%prep
%goprep

%build
go mod vendor
%gobuild -o %{gobuilddir}/bin/spc %{goipath}

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%gopkgfiles

%changelog
* Sat Aug 22 13:36:00 EDT 2020 David Muckle <dvdmuckle@dvdmuckle.xyz> - 0.4-1
- Initial package

