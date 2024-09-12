from setuptools import setup

setup(name='namizun_core',
      version='1.4.0',
      description='namizun main functions',
      author='SinaEs',
      author_email='sina.eskandari0937@gmail.com',
      url='https://github.com/sinaes21/namizun',
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6']
      )
