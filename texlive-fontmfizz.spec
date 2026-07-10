%global tl_name fontmfizz
%global tl_revision 43546

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Font Mfizz icons for use in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fontmfizz
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontmfizz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fontmfizz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The MFizz font provides scalable vector icons representing programming
languages, operating systems, software engineering, and technology. It
can be seen as an extension to FontAwesome. This package requires the
fontspec package and either the Xe(La)TeX or Lua(La)TeX engine to load
the included ttf font.

