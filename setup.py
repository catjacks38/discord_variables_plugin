import setuptools

with open("README.md", "r") as file:
    longDesc = file.read()

setuptools.setup(
    name="discord_variables_plugin",
    version="1.2",
    author="catjacks38",
    description="A plugin to help with saving variables for Discord bots",
    long_description=longDesc,
    long_description_content_type="text/markdown",
    url="https://github.com/catjacks38/discord_variables_plugin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    python_requires=">=3.5.3"
)
