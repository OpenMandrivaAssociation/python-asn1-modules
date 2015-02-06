%define	oname	pyasn1-modules
%define	module	asn1-modules

Name:		python2-%{module}
Version:	0.0.5
Release:	2
Summary:	A collection of ASN.1-based protocols modules
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sourceforge.net/projects/pyasn1/
BuildArch:	noarch
BuildRequires:	python2-setuptools

%description
A collection of ASN.1 modules expressed 
in form of pyasn1 classes. 
Includes protocols PDUs definition 
(SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

%prep
%setup -q -n %{oname}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot}

%files
%doc CHANGES
%doc LICENSE
%doc README
%{py2_puresitedir}/pyasn1_modules/*.py*
%{py2_puresitedir}/pyasn1_modules*.egg-info
