from setuptools import setup, find_packages
from modelmetry.version import SDK_VERSION

long_description = """
The Modelmetry SDK provides a Python interface to interact with the Modelmetry API, 
allowing developers to easily integrate Modelmetry's capabilities into their applications.
"""

setup(
    name="modelmetry-python-sdk",
    version=SDK_VERSION,
    description="Official Python library for Modelmetry",
    long_description=long_description,
    url="https://modelmetry.com",
    author="test",
    author_email="support@modelmetry.com",
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