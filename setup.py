"Setup class"

from distutils.core import setup

setup(
    name='backuPi',
    version='1.0.0',
    packages=['backuPi'],
    url='https://github.com/develohpanda/backuPi',
    description='Backup tool for Raspberry Pi',
    install_requires=[
        'mount'
    ],
    dependency_links=[
        'https://github.com/develohpanda/mount.py/tarball/master#egg=mount.py'
    ]
)
