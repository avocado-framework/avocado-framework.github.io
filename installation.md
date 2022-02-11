---
layout: default
---

# Downloading and installing Avocado

## Python package on PyPI
You can install the package from PyPI:

```bash
 pip3 install --user avocado-framework
```

A system-wide installation is also possible, dropping the `--user` option.

Also, check out for the [avocado plugins distributed on PyPI](https://pypi.org/search/?q=avocado-framework-plugin)


## Installing from packages in Fedora

The Avocado Framework is available as a standard distribution package. Enable the latest stream and install it to use the latest version:

```bash
 dnf module enable avocado:latest
 dnf module install avocado
```

If you keep your system updated, you'll get automatically the avocado updates.

### Latest Development RPM Packages from COPR

Installing the latest Avocado code from the master branch is as easy as installing a package. Enable the COPR repository and install the package using the package manager:

```bash
dnf copr enable @avocado/avocado-latest
dnf install python3-avocado*
```

## Installing from the source code

Install the dependencies:

```bash
 dnf install -y python3 git gcc python3-pip
```

Clone and install from the main repository:

```bash
git clone git://github.com/avocado-framework/avocado.git
cd avocado
python3 setup.py install --user
```

If you need more detailed instructions and how to install from source, please check our [documentation](https://avocado-framework.readthedocs.io/en/latest/guides/user/chapters/installing.html).
