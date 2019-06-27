from setuptools import setup, find_packages

install_requires = [
    'click==7.0',
    'requests==2.22.0'
]

setup(
    name='ipfinder',
    version='0.0.1',
    author='Joshua Groeschl',
    author_email='joshua.groeschl@tutanota.com',
    description='A utility tool for determining a users Public IPv4 WAN address.',
    license='MIT',
    py_modules=['externip'],
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'ipfinder = externip:ipfinder',
        ]
    },
    package_dir={'': 'src'},
    packages=find_packages('src')
)