import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
install_requires = [
    "cffi==1.15.1",
    "mnemonic==0.20",
    "pycparser==2.21",
    "PyNaCl==1.5.0",
]

about = {}
with open(
        os.path.join(here, "stellar_sdk", "__version__.py"), mode="r", encoding="utf-8"
) as f:
    exec(f.read(), about)

with open("README.rst", mode="r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    license=about["__license__"],
    keywords=[
        "stellar-sdk",
        "stellar.org",
        "lumens",
        "xlm",
        "blockchain",
        "distributed exchange",
        "cryptocurrency",
        "dex",
        "stellar-core",
        "horizon",
        "sdex",
        "trading",
    ],
    project_urls={
        "Documentation": "https://stellar-sdk.readthedocs.org",
        "Code": "https://github.com/StellarCN/py-stellar-base",
        "Issue tracker": "https://github.com/StellarCN/py-stellar-base/issues",
    },
    include_package_data=True,
    install_requires=install_requires,
    packages=find_packages(exclude=["tests", "tests.*"]),
    python_requires=">=3.7.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
)
