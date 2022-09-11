%define	oname	pyasn1-modules
%define	module	asn1-modules

Name:		python-%{module}
Version:	0.2.8
Release:	1
Summary:	A collection of ASN.1-based protocols modules
Source0:	https://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://github.com/etingof/pyasn1-modules
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
A collection of ASN.1 modules expressed 
in form of pyasn1 classes. 
Includes protocols PDUs definition 
(SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

%prep
%setup -q -n %{oname}-%{version}
%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%files
%doc python3/CHANGES.txt
%doc python3/LICENSE.txt
%doc python3/README.md
%{py3_puresitedir}/pyasn1_modules/*.py*
%{py3_puresitedir}/pyasn1_modules*.egg-info
