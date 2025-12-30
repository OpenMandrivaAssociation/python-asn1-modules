%define	oname	pyasn1_modules
%define	module	asn1-modules

Name:		python-%{module}
Version:	0.4.2
Release:	2
Summary:	A collection of ASN.1-based protocols modules
Source0:	https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/etingof/pyasn1-modules
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
A collection of ASN.1 modules expressed 
in form of pyasn1 classes. 
Includes protocols PDUs definition 
(SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

%files
%{py_puresitedir}/pyasn1_modules/__pycache__
%{py_puresitedir}/pyasn1_modules/*.py*
%{py_puresitedir}/pyasn1_modules-%{version}.dist-info
