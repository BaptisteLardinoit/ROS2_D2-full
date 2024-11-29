from setuptools import find_packages, setup

package_name = 'quartermaster'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kenobi',
    maintainer_email='matis.viozelange@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pid_controler  = quartermaster.pid_controler:main',
            'MPC            = quartermaster.MPC:main',
            'USV_MPC        = quartermaster.USV_MPC:main',
            'Cam_controler = quartermaster.cam_controler:main',
        ],
    },
)