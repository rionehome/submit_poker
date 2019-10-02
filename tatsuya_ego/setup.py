from setuptools import setup

package_name = 'ros2_poker'

setup(
    name='ros2_poker',

    version='0.0.1',
    packages=[],
    py_modules=[
        "poker"
    ],
    data_files=[
        ('share/' + package_name ,['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Tatsuyaego',
    author_email='is0506he@ed.ritsumei.jp',
    maintainer='Tatsuyaego',
    maintainer_email='is0506he@ed.ritsumei.jp',
    keywords=['ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'poker=poker:main',
        ],
    },
)