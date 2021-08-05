from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in contoh/__init__.py
from contoh import __version__ as version

setup(
	name="contoh",
	version=version,
	description="apa",
	author="apa",
	author_email="apa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
