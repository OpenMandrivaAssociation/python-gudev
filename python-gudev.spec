Summary:        Python (PyGObject) bindings to the GUDev library
Name:           python-gudev
URL:            http://github.com/nzjrs/
Version:        147
Release:        %mkrel 3
Source0: 	http://github.com/nzjrs/python-gudev/tarball/%{version}/nzjrs-python-gudev-%{version}.2-1-g780b007.tar.gz
Group:          Development/Python
License:        LGPLv3+
%if %_arch == i386
Requires:       libgudev1.0_0 >= 147
%endif
%if %_arch == X86_64
Requires:       lib64gudev1.0_0 >= 147
%endif
Requires:       python-gobject
BuildRequires:  python-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%if %_arch == i386
BuildRequires:  libgudev1.0-devel >= 147
%endif 
%if  %_arch == x86_64
BuildRequires:  lib64gudev1.0-devel >= 147
%endif
BuildRequires:  python-gobject-devel

%description
python-gudev is a Python (PyGObject) binding to the GUDev UDEV library.

%prep
%setup -q -n nzjrs-python-gudev-780b007

%build
sh autogen.sh --prefix=%{_prefix} --disable-static
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING README NEWS
%doc test.py
%{py_platsitedir}/*
%{_datadir}/pygobject/2.0/defs/gudev.defs


%changelog
* Thu Jul 21 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 147.2-1
- Update to latest upstream

* Thu Jul 21 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 147.1-7
- Added upstream patch
- Resolves: rhbz#637084,rhbz#723795
- Related: rhbz#631789

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 147.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 147.1-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar 15 2010 Miroslav Suchý <msuchy@redhat.com> 147.1-4
- 572609 - do not strip all debuginfo

* Mon Feb  8 2010 Miroslav Suchý <msuchy@redhat.com> 147.1-3
- initial release
