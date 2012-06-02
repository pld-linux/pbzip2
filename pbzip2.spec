# TODO
# - check minimum gcc ver:
#   on ac gcc 3.3.6: - BZ2StreamScanner.cpp:(.text+0x219): undefined reference to `std::char_traits<unsigned char>::length(unsigned char const*)'
Summary:	Parallel implementation of bzip2
Summary(pl.UTF-8):	Zrównoleglona implementacja bzip2
Name:		pbzip2
Version:	1.1.6
Release:	1
License:	BSD
Group:		Applications/Archiving
Source0:	http://www.compression.ca/pbzip2/%{name}-%{version}.tar.gz
# Source0-md5:	26cc5a0d882198f106e75101ff0544a3
URL:		http://www.compression.ca/pbzip2/
BuildRequires:	bzip2-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
wieloprocesorowych. Wyjście z tego programu jest w pełni kompatybilne
z formatem bzip2 w wersji 1.0.2 lub nowszej (tzn. wszystko
skompresowane programem pbzip2 może być rozpakowane przy pomocy
bzip2).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p %{name} $RPM_BUILD_ROOT%{_bindir}
ln -sf %{name} $RPM_BUILD_ROOT%{_bindir}/pbunzip2
cp -a %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/pbzip2
%attr(755,root,root) %{_bindir}/pbunzip2
%{_mandir}/man1/pbzip2.1*
