Name:		texlive-babel-basque
Version:	30256
Release:	1
Summary:	TeXLive babel-basque package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-basque.r30256.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-basque.doc.r30256.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-basque.source.r30256.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-basque package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-basque
%doc %{_texmfdistdir}/doc/generic/babel-basque
#- source
%doc %{_texmfdistdir}/source/generic/babel-basque

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
