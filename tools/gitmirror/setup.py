from setuptools import setup

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='gitmirror',
    version='0.0.1',
    long_description=readme(),
    description='A tools to setup mirror for all openstack git projects',
    url='http://github.com/jiangyh/worktree',
    scripts=['bin/openstack-mirror'],
    author='Yunhong Jiang',
    author_email="yunhong.jiang@intel.com",
    license='MIT',
    install_requires=[
        'gerritlib',
        ],
    packages=['gitmirror'],
    include_package_data=True,
    zip_safe=False)
