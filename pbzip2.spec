Summary:	Parallel implementation of bzip2
Summary(pl.UTF-8):	Zrównoleglona implementacja bzip2
Name:		pbzip2
Version:	1.0.2
Release:	0.9
License:	BSD
Group:		Applications/Archiving
URL:		http://www.compression.ca/pbzip2/
BuildRequires:	bzip2-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	http://www.compression.ca/pbzip2/%{name}-%{version}.tar.gz
# Source0-md5:	2f58b4e844c74d0c98b98326c6a3945f
Patch0:		%{name}-optflags.patch

%description
PBZIP2 is a parallel implementation of the bzip2 block-sorting file
compressor that uses pthreads and achieves near-linear speedup on SMP
machines. The output of this version is fully compatible with bzip2
v1.0.2 or newer (ie: anything compressed with pbzip2 can be
decompressed with bzip2).

%description -l pl.UTF-8
PBZIP2 to zrównoleglona implementacja algorytmu kompresji plików
metodą sortowania bloków sobzip2, wykorzystująca mechanizm wątków
pthread i osiągająca prawie liniowe przyspieszenie na maszynach
wieloprocesorowych. Wyjście z tego programu jest w pełni
kompatybilne z formatem bzip2 w wersji 1.0.2 lub nowszej (tzn.
wszystko skompresowane programem pbzip2 może być rozpakowane przy
pomocy bzip2).

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC=%{__cxx} \
	OPTFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
ln -sf %{name} $RPM_BUILD_ROOT%{_bindir}/pbunzip2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/pbunzip2
%{_mandir}/man1/*
