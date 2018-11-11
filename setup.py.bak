from __future__ import print_function
import sys
import io
import os
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from ABtests import stats

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst', 'CHANGES.txt')


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


setup(
    name='ABtests',
    version=stats.__version__,
    license='Apache Software License',
    author='Leonardo De Marchi',
    tests_require=['ABtests'],
    install_requires=['matplotlib>=1.5.3'
                      'numpy>=1.11.2'
                      'pandas>=0.19.0'
                      'scipy>=0.18.1'
                      'seaborn>=0.7.1'
                      'setuptools>=28.3.0'
                      'pytest>=3.0.3'
                      'statsmodels>=0.8.0rc1'
                      ],
    cmdclass={'test': PyTest},
    description='Automated AB tests',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/leodema/ABtests',
    maintainer_email='leodema@users.noreply.github.com',
    platforms='any',
    test_suite='ABtests.tests',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    extras_require={
        'testing': ['stats'],
    }
)
