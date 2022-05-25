import os
from setuptools import setup, find_packages


install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


##this is weird. 
package_name = 'PF400_driver'

setup(
    name='PF400_driver',
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=install_requires,
    zip_safe=True,
    python_requires=">=3.8",
    maintainer='Doga Ozgulbas and Alan Wang',
    maintainer_email='dozgulbas@anl.gov',
    description='Driver for the PF400 robot arm',
    url='https://github.com/AD-SDL/PF400_driver.git', 
    license='MIT License',
    entry_points={ 
        'console_scripts': [
             'arm_driver = arm_driver_pkg.arm_driver:main_null',
            #  'arm_listener = pf400_client.arm_listener:main_null',
            #  'rpl_pf400 = pf400_client.rpl_pf400:main_null',
            #  'pf400_client = pf400_client.pf400_client:main_null',
            #  'dummy_server = pf400_client.dummy_server:main_null',

        ]
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
