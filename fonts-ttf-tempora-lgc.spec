%define pkgname tempora-lgc

Summary:	times-like font with Latin, Greek and Cyrillic support
Name:		fonts-ttf-tempora-lgc
Version:	0.2
Release:	2
License:	GPLv2 with exception
Group:		System/Fonts/True type
URL:		http://www.thessalonica.org.ru/en/fonts.html
Source0:	http://www.thessalonica.org.ru/downloads/%{pkgname}.ttf.zip
BuildArch:	noarch
BuildRequires:	freetype-tools

%description
This font family is based on two well-known free typefaces similar to Adobe
Times: Nimbus Roman No 9 L by URW (russified by Valek Filippov), and the Omega
Serif family, developed by Yannis Haralambous. However, all basic components
of the font, and especially its Greek and Cyrillic parts, have suffered
serious modifications, so that currently Tempora LGC Unicode represents an
independent typeface, quite different from its predecessors.

%prep
%setup -q -c -n %{pkgname}-%{version}

%build

%install
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/tempora-lgc

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/tempora-lgc
ttmkfdir %{buildroot}%{_xfontdir}/TTF/tempora-lgc > %{buildroot}%{_xfontdir}/TTF/tempora-lgc/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/tempora-lgc/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/tempora-lgc \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-tempora-lgc:pri=50

%files
%doc COPYING HISTORY README
%dir %{_xfontdir}/TTF/tempora-lgc
%{_xfontdir}/TTF/tempora-lgc/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/tempora-lgc/fonts.dir
%{_xfontdir}/TTF/tempora-lgc/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-tempora-lgc:pri=50


%changelog
* Wed Dec 07 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2-1
+ Revision: 738637
- imported package fonts-ttf-tempora-lgc

