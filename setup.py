from setuptools import setup, find_packages

setup(
    name='todo_app',
    version='0.0.1',
    description='ToDo App',
    author='deepraj',
    author_email='deepraj@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
