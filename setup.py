from setuptools import setup, find_packages
setup(
    name = "docker-autocompose",
    version = "1.2.0",
    description = "Generate a docker-compose yaml definition from a running container",
    url = "https://github.com/zbgn/docker-autocompose",
    author = "zbgn",
    license = "GPLv2",
    keywords = "docker yaml container",
    packages = find_packages(),
    install_requires = ['pyaml>=17.12.1', 'docker>=3.4.1','six>=1.16.0'],
    scripts = ['autocompose.py'],
    entry_points={
        'console_scripts': [
            'autocompose = autocompose:main',
        ]
    }
)
