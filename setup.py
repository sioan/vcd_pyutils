import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


REQUIREMENTS = []

setuptools.setup(
    name="vcd_pyutils",
    version="0.0.1",
    author="Sioan Zohar",
    author_email="zohar.sioan@gmail.com",
    description="utilities for generic vcd applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sioan/vcd_pyutils",
    project_urls={
        "Bug Tracker": "https://github.com/sioan/vcd_pyutils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=REQUIREMENTS,
    python_requires=">=3.6",


)