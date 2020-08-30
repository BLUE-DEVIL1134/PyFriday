
from setuptools import setup

README = open("README.md","r").read()
setup(
    name="PyFriday",
    version="1.0",
    description="A Virtual Assistant In Pure Python..",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BLUE-DEVIL1134/PyFriday",
    author="Akash Pattnaik",
    author_email="akashpattnaik.github@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=["PyFriday"],
    install_requires=['pyttsx3', 'speech_recognition', 'wikipedia', 'webbrowser', 'pipwin'],
    entry_points={
        "console_scripts": [
            "PyFriday=PyFriday.__init__:loop",
            "Friday=PyFriday.__init__:loop",
            "Jarvis=PyFriday.__init__:loop",
            "jarvis=PyFriday.__init__:loop",
            "friday=PyFriday.__init__:loop",
            "pyfriday=PyFriday.__init__:loop",
        ]
    },
)
