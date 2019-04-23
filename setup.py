from setuptools import setup

setup(name='platwilio',
      version='0.1',
      description='PLA Twilio',
      url='http://github.com/philalegal/platwilio',
      author='Jonathan Pyle',
      author_email='jpyle@philalegal.org',
      license='MIT',
      install_requires=['blinker', 'coverage', 'Flask', 'Flask-Script', 'Flask-Testing', 'funcsigs', 'httplib2', 'itsdangerous', 'Jinja2', 'linecache2', 'MarkupSafe', 'mock', 'nose', 'pbr', 'pycparser', 'pytz', 'requests', 'selenium', 'six', 'traceback2', 'twilio', 'unittest2', 'Werkzeug'],
      packages=['platwilio'],
      package_data={'platwilio': ['templates/*.*', 'static/*.*']},
      include_package_data=True,
      zip_safe=False)
