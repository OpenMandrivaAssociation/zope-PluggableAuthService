%define Product PluggableAuthService
%define product pluggableauthservice
%define name    zope-%{Product}
%define version 1.5.2
%define release %mkrel 7

%define zope_minver	2.7
%define plone_minver	2.0
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	This product defines a fully-pluggable user folder, intended for use in all Zope sites
License:	GPL
Group:		System/Servers
URL:		https://www.zope.org/Products/%{Product}
Source:		http://zope.org/Products/%{Product}/%{Product}-%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope-Plone >= %{plone_minver}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This product defines a fully-pluggable user folder, intended for use in all
Zope sites

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a %{Product}-%{version} %{buildroot}%{software_home}/Products/
%{__mv} %{buildroot}%{software_home}/Products/%{Product}-%{version} \
	%{buildroot}%{software_home}/Products/%{Product}

%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
