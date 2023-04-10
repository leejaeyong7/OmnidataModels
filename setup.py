from pkg_resources import parse_version, parse_requirements
import setuptools
assert parse_version(setuptools.__version__)>=parse_version('36.2')
with open('LICENSE', encoding='utf-8') as f:
    license = f.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name='OmnidataModels',
    license=license,
    url='https://github.com/leejaeyong7/OmnidataModels',
    packages = setuptools.find_packages(),
    install_requires = required,
    python_requires='>=3.6',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    zip_safe = False,
    version='0.0.1',
)