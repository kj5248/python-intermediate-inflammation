# Inflam

![Continuous Integration build in GitHub Actions](https://github.com/kj5248/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation

- Clone the repository using command ''git clone repo'' where [repo](https://github.com/kj5248/python-intermediate-inflammation)
- Change directory into the repository folder
- Create a virtual environment here with ''python3 -m venv venv''
- Activate the environment with ''source venv/bin/activate''
- Install the repository requirements with ''pip3 install -r requirements.txt''
- Install local repository to environment using ''pip install -e .''
- Use ''pytest'' to check everything was correctly installed

## Usage

- Different parts of the system can be run using the ''python'' command alongside the desired file
- Some of the files have additional arguments which can be checked using --h to bring up a list of possible arguments

## Contribution

- Create an issue and assign to yourself and add corresponding tag
- After editing and improving can then submit a pull request

## Contact

- If it is in relation to a bug in the code an issue can be created detailing the problem and assigned the author or other administrator
- Alternatively running ''git show v1.0.0'' will provide the authors name and email for contact purposes

## Citations

- The online course that led to the creation of this work can be found at:
        - https://ukaea-rse-training.github.io/python-intermediate-development/00-setting-the-scene/index.html

## Credits

- Credit goes to the initial creators the UKAEA RSE team and The Carpentries Incubator for the setup of this repository and the lessons
- Credit to repository owner: kj5248
- Credit to collaborators: agwhittle, dsimfukwe and Fitz1309.