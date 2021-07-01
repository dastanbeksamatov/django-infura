"""Setup script for django-infura"""

import os.path
from setuptools import setup
# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="django-infura",
    version="1.0.0",
    description="Send tx from Django with infura",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dastanbeksamatov/django-infura",
    author="Dastan Samatov",
    author_email="dastanbeksamatov@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["tx"],
    include_package_data=True,
    install_requires=[
        "requests"
    ],
    entry_points={"console_scripts": ["django-infura=tx.__main__:main"]},
)
