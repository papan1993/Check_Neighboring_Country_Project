from setuptools import find_packages, setup

setup(
    name = 'Check_Neighboring_Country_Library',
    packages = find_packages(include=['Check_Neighboring_Country_Library']),
    version = '1.0.0',
    description = 'Detects whether two countries are neighbors or not using wiki urls ',
    author = 'Soumyadeep Choudhury',
    email = 'papan1993@gmail.com',
    license = 'Test Project',
    install_requires = [],
    setup_requires = ['pytest-runner'],
    tests_require = ['more-itertools', 'pytest'],
    test_suite = 'tests'
)