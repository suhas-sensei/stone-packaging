Name:           stone-prover
Version:        %{?version}  # The version, automatically pulled from the Git tag in your workflow
Release:        1%{?dist}
Summary:        The prover tool for the Stone project

License:        MIT
URL:            https://github.com/baking-bad/stone-prover
Source0:        %{name}-%{version}.tar.gz  # Placeholder, replace with the actual source tarball or GitHub URL

BuildRequires:  gcc, make, bazel  # Add any other dependencies required for building the project
Requires:       gcc, make, bazel  # Add runtime dependencies

%description
The stone-prover is a prover tool used in conjunction with the Stone project.

%prep
# This section prepares the software for building
%setup -q  # Assumes you are unpacking a tarball, replace if necessary

%build
# The actual build commands, modify as needed
make  # If there's a specific build process, use it here

%install
# Install the binaries and other files into the RPM build root
make install DESTDIR=%{buildroot}

%files
# List the files to be included in the RPM
/usr/bin/stone-prover  # Path to the binary, adjust as per your project structure

%changelog
* Tue Oct 01 2024 Your Name <suhas.ghosal2002@gmail.com> - 1.0-1
- Initial package
