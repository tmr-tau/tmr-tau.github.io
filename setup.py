import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tau-docs",
    version="0.0.1",
    author="Department of Transport and Main Roads",
    author_email="transport_analysis_requests@tmr.qld.gov.au",
    description="TAUDocs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.taugit.com/taugit",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
