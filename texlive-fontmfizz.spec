Name:		texlive-fontmfizz
Version:	43546
Release:	1
Summary:	Font Mfizz icons for use in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fontmfizz
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontmfizz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontmfizz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The MFizz font provides scalable vector icons representing
programming languages, operating systems, software engineering,
and technology. It can be seen as an extension to FontAwesome.
This package requires the fontspec package and either the
Xe(La)TeX or Lua(La)TeX engine to load the included ttf font.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/fontmfizz
%{_texmfdistdir}/fonts/truetype/public/fontmfizz
%doc %{_texmfdistdir}/doc/fonts/fontmfizz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
