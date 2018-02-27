%define	oname	pyasn1-modules
%define	module	asn1-modules

Name:		python-%{module}
Version:	0.2.1
Release:	1
Summary:	A collection of ASN.1-based protocols modules
Source0:	http://pypi.python.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://sourceforge.net/projects/pyasn1/
BuildArch:	noarch
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools

%description
A collection of ASN.1 modules expressed 
in form of pyasn1 classes. 
Includes protocols PDUs definition 
(SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

%package -n python2-%{module}
Summary:        Python 2.x library for asn1-modules
Group:          Development/Python

%prep
%setup -q -n %{oname}-%{version}
mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
pushd python2
python2 setup.py build
popd
pushd python3
python3 setup.py build
popd

%install
pushd python2
python2 setup.py install --root=%{buildroot}
popd

pushd python3
python3 setup.py install --root=%{buildroot}
popd

%files
%doc python3/CHANGES.txt
%doc python3/LICENSE.txt
%doc python3/README.md
%{py3_puresitedir}/pyasn1_modules/*.py*
%{py3_puresitedir}/pyasn1_modules*.egg-info

%files -n python2-%{module}
%doc python2/CHANGES.txt
%doc python2/LICENSE.txt
%doc python2/README.md
%{py2_puresitedir}/pyasn1_modules/*.py*
%{py2_puresitedir}/pyasn1_modules*.egg-info


