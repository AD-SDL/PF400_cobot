import os
from setuptools import setup, find_packages
import glob

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


##this is weird. 
package_name = 'pf400_client'

setup(
    name = package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=install_requires,
    zip_safe=True,
    python_requires=">=3.8",
    maintainer='Doga Ozgulbas',
    maintainer_email='dozgulbas@anl.gov',
    description='Driver for the PF400 robot arm',
    url='https://github.com/AD-SDL/PF400_driver.git', 
    license='MIT License',
    entry_points={ 
        'console_scripts': [
             'pf400_client = pf400_client.pf400_client:main',
        ]
    },
)
