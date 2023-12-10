import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open ("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="tracc",
    version="0.0.1",
    author="Kelly McCuddy",
    author_email="kelly@graewolf.com",
    description="Traveller character creator",
    long_description=long_description,
    long_description_content_type="text/md",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Creative Commons",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    install_requires=requirements,
)
