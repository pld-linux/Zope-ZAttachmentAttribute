%define		zope_subname	ZAttachmentAttribute
Summary:	A system to manage attachments within Zope objects
Summary(pl):	Produkt dla Zope do zarz±dzania za³±cznikami
Name:		Zope-%{zope_subname}
Version:	2.3
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/ingeniweb/%{zope_subname}-%{version}.tar.gz
# Source0-md5:	1a88288063cbd373e38470f4618ab7b0
URL:		http://sourceforge.net/projects/ingeniweb/
%pyrequires_eq	python-modules
Requires:	Zope
Requires(post,postun):	/usr/sbin/installzopeproduct
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A system to manage attachments within Zope objects.

%description -l pl
Produkt dla Zope do zarz±dzania za³±cznikami.

%prep
%setup -q -n %{zope_subname}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af *.py *.txt dtml $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope restart >&2
	fi
fi

%files
%defattr(644,root,root,755)
%doc doc/* CHANGES ChangeLog README
%{_datadir}/%{name}
