from setuptools import setup

setup(
   name='myutil',
   version='1.0',
   description='reoccuring stuff',
   author='Dennis Reimann',
   author_email='d.reimann@nexperia.com',
   packages=['myutil'],  #same as name
   install_requires=['wheel'], #external packages as dependencies
)
