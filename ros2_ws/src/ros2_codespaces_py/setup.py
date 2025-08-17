from setuptools import setup

package_name = 'ros2_codespaces_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='tuo_email@example.com',
    description='ROS2 codespaces cpp',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            #'example_exec = ' + package_name + '.example_file.example_exec:main',
        ],
    },
)