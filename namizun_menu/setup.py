from setuptools import setup, find_packages

setup(name='namizun_menu',
      version='1.1.0',
      description='namizun menu',
      author='MalKeMit',
      author_email='khodemalkemit@gmail.com',
      py_modules=['main_menu', 'network_submenu', 'monitor', 'udp_submenu', 'display'],
      setup_requires=['wheel'],
      install_requires=['colored~=1.4.4',
                        'pyfiglet~=0.8.post1',
                        'prettytable~=3.5.0']
      )
