from setuptools import setup, find_packages
from modelmetry.version import SDK_VERSION

long_description = """
Test description
"""

setup(
    name="modelmetry0-sdk",
    version=SDK_VERSION,
    description="Official Python library for Modelmetry",
    long_description=long_description,
    url="https://github.com/modelmetry/modelmetry-sdk-python",
    author="Modelmetry",
    author_email="support@modelmetry.io",
    license="Apache License 2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'urllib3>=1.25.3',
        'python-dateutil>=2.9.0',
        'pydantic>=2',
        'typing-extensions>=4.12.2',
        'devtools>=0.12.2',
        'python-dotenv>=1.0.1',
        'pytest>=8.2.2',
    ],
    zip_safe=False,
)