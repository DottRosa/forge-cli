from setuptools import setup, find_packages

setup(
    name="forge-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "forge = forge.main:main",
        ],
    },
    author="Marco Rosa",
    author_email="marco1rosa@gmail.com",
    description="Forge CLI is a command-line tool designed to streamline and automate project management tasks. With Forge CLI, users can easily configure, build, and manage their software projects through a simple and intuitive interface. This tool reads from a .forge.json configuration file to provide customizable options that cater to various development needs. Whether you are compiling projects, running tests, or cleaning up, Forge CLI enhances productivity and reduces setup complexity for developers of all skill levels.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DottRosa/forge-cli",
)
