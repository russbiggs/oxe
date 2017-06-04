from setuptools import setup

setup(name='oxe',
      version='1.0',
      description='parses ODK xml file to find a desired value',
      classifiers=[
          'Programming Language :: Python :: 2.7',
          'Topic :: XML Processing :: ODK',
      ],
      keywords='odk xml opendatakit',
      url='http://github.com/russbiggs/oxe',
      author='Russ Biggs',
      author_email='russbiggs@gmail.com',
      license='MIT',
      packages=['oxe'],
      entry_points={
          'console_scripts': ['oxe=oxe.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)
