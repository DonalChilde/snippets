"""
Source: __about__template.py
Template Version: 1.1.0
Template Rev. Date: 2019.02.07
"""


__all__ = [
    "__PYPI_NAME__",
    "__NAME__",
    "__SHORT_DESCRIPTION__",
    "__URL__",
    "__EMAIL__",
    "__AUTHOR__",
    "__PYTHON_REQUIRES__",
    "__KEYWORDS__",
    "__VERSION__",
    "__INSTALL_REQUIRES__",
    "__EXTRAS_REQUIRE__",
    "__PACKAGE_DATA__",
    "__ENTRY_POINTS__",
    "__PROJECT_URLS__",
    "__LICENSE__",
    "__CLASSIFIERS__",
]

# Package meta-data.
__PYPI_NAME__ = "mypackage"
__NAME__ = ""
__SHORT_DESCRIPTION__ = "My short description for my project."
__URL__ = "https://github.com/me/myproject"
__EMAIL__ = "me@example.com"
__AUTHOR__ = "Awesome Soul"
__PYTHON_REQUIRES__ = ">=3.7.0"
__KEYWORDS__ = "sample setuptools development"
__VERSION__ = "0.0.0.dev0"
# What packages are required for this module to be executed?
__INSTALL_REQUIRES__: list = [
    # 'requests', 'maya', 'records',
]
# What packages are optional?
__EXTRAS_REQUIRE__: dict = {
    # "dev": ["check-manifest"], "test": ["coverage"]
}
# Prefer include_package_data, with a good MANIFEST.in file
# To use PACKAGE_DATA, uncomment in setup()
# https://setuptools.readthedocs.io/en/latest/setuptools.html#including-data-files
__PACKAGE_DATA__: dict = {
    # # If any package contains *.txt files, include them:
    # "": ["*.txt"],
    # # And include any *.dat files found in the 'data' subdirectory
    # # of the 'mypkg' package, also:
    # "mypkg": ["data/*.dat"],
}
__ENTRY_POINTS__: dict = {
    # "console_scripts": ["sample=sample:main"]
}
__PROJECT_URLS__: dict = {  # Optional
    # "Bug Reports": "https://github.com/pypa/sampleproject/issues",
    # "Funding": "https://donate.pypi.org",
    # "Say Thanks!": "http://saythanks.io/to/example",
    # "Source": "https://github.com/pypa/sampleproject/",
}
__LICENSE__ = "MIT"
__CLASSIFIERS__: list = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.7",
]
