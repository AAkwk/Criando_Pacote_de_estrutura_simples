from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="my_info_package",
    version="0.0.1",
    author="Alexandre Kawakita",
    author_email="aakawakitas12@gmail.com",
    description="Pacote simples que retorna minha informações.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="github.com/AAkwk/Criando_Pacote_de_estrutura_simples/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.13.7',
)
