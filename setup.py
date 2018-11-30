from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cash-converter-cli',
    version='0.1.1',
    author="Tuan Nguyen",
    author_email="tuan.nguyenviet271@gmail.com",
    description="Currency converter using lastest data from fixer.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daenylio/cash-converter-cli",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        cashconverter=scripts.main:cli
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)