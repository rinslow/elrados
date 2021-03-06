"""Setup file for handling packaging and distribution."""
import sys

from setuptools import setup, find_packages

__version__ = "0.5.3"

requirements = [
    'django>=1.7,<1.8',
    'twisted',
    'crochet',
    'autobahn',
    'rotest'
    ]

if not sys.platform.startswith("win32"):
    requirements.append('python-daemon')

setup(
    name='elrados',
    version=__version__,
    description="Frontend for django models and Rotest Testing Framework",
    license="MIT",
    author="Elran Shefer",
    author_email="elran777@gmail.com",
    url="https://github.com/IamShobe/elrados",
    keywords="rotest frontend",
    install_requires=requirements,
    python_requires="~=2.7.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"elrados": ["frontend/static/*",
                              "frontend/static/img/*",
                              "frontend/static/font/*",
                              "frontend/templates/*"]},
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        ],
    )
