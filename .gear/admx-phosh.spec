%define _destdir %_datadir/PolicyDefinitions

Name: admx-phosh
Version: 0.1
Release: alt1

Summary: Phosh-specific ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

BuildRequires: admx-lint admx-basealt

Source0: %name-%version.tar

%description
ALTMobile-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -r ru-RU/ en-US/ Phosh.admx %buildroot%_destdir/

%check
for file in *.admx *-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%_destdir

%changelog
* Tue Sep 10 2024 Valentin Sokolov <sova@altlinux.org> 0.1-alt1
- Initial build for Sisyphus