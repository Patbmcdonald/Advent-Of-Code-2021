import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aoc",
    version="0.0.1",
    author="Patrick McDonald",
    author_email="pat.b.mcdonald@gmail.com",
    description="Solving advent of code!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
