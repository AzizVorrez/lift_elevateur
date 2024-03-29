from setuptools import setup, find_packages

setup(
    name="lift_elevateur",
    version="1.0",
    author="Aziz Vorrez",
    description="Lift project",
    packages=find_packages(),
    install_requires=[
        "asgiref==3.6.0"
        "Django==4.2"
        "mysqlclient==2.1.1"
        "sqlparse==0.4.4"
        "tzdata==2023.3"
    ],
)
