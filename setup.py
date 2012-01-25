from distutils import setup

import stats


setup(
    name='stats',
    description='TODO',
    long_description=open('README.md').read(),
    version=stats.__version__,
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    license='Apache',
    py_modules=['stats']
)
