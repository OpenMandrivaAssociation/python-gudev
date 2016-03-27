Summary:        Python (PyGObject) bindings to the GUDev library
Name:           python2-gudev
URL:            http://github.com/nzjrs/
Version:        147
Release:        4
Source0:	http://github.com/nzjrs/python-gudev/tarball/%{version}/nzjrs-python-gudev-%{version}.2-1-g780b007.tar.gz
Group:          Development/Python
License:        LGPLv3+
%if %_arch == i386
Requires:       libgudev1.0_0 >= 147
%endif
%if %_arch == X86_64
Requires:       lib64gudev1.0_0 >= 147
%endif
Requires:       python2-gobject
BuildRequires:  python2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%if %_arch == i386
BuildRequires:  libgudev1.0-devel >= 147
%endif 
%if  %_arch == x86_64
BuildRequires:  lib64gudev1.0-devel >= 147
%endif
BuildRequires:  python2-gobject-devel

%rename python-gudev

%description
python-gudev is a Python (PyGObject) binding to the GUDev UDEV library.

%prep
%setup -q -n nzjrs-python-gudev-780b007

%build
export PYTHON=python2

sh autogen.sh --prefix=%{_prefix} --disable-static

%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README NEWS
%doc test.py
%{py2_platsitedir}/*
%{_datadir}/pygobject/2.0/defs/gudev.defs




%changelog
* Sat Feb 11 2012 Oden Eriksson <oeriksson@mandriva.com> 147-3mdv2012.0
+ Revision: 773026
- relink against libpcre.so.1

* Thu Aug 11 2011 Leonardo Coelho <leonardoc@mandriva.org> 147-2
+ Revision: 694053
- change on spec file to add a dependency pkg

* Wed Aug 10 2011 Leonardo Coelho <leonardoc@mandriva.org> 147-1
+ Revision: 693872
- import spec file from fedora frist mandriva version
- Created package structure for python-gudev.

