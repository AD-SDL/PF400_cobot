import os
from setuptools import setup, find_packages


install_requires = ["setuptools"]
# with open('requirements.txt') as reqs:
#     for line in reqs.readlines():
#         req = line.strip()
#         if not req or req.startswith('#'):
#             continue
#         install_requires.append(req)


package_name = 'camera_module_driver'

setup(
    name='camera_module_driver',
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
    url='https://github.com/AD-SDL/camera_module_driver.git', 
    license='MIT License',
    entry_points={ 
        'console_scripts': [
             'camera_module_driver = camera_module_driver.camera_module_driver:main_null',
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
