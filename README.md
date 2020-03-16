# Tdd-Assigment-2-SCE

Testing project (in TDD metology) of 2 features in a NBA database API, it’s a colleague project and is made purely for learning purposes.
Here’s the link to the API used in this project: https://www.balldontlie.io/ .
The 2 features we tested is the game data and player data.
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
# Prerequisites
Python 3.6 and up (probably works in most Python 3.X, but tested for 3.6)
Pip 10.0.1 and up for package manager.
Request 2.23.
# Installing
Download the folders, run the testing files in a machine that can run python and has the appropriate libraries.
#Running the tests
You need to run the test files while the source files are at the same directory as they are in the project.
# Brief explanition about the tests
The tests in the project test the 2 features of the API we choose for this project they test mainly simple functionality of getting the right data from the API.
For example one of the tests is testing a function that translate imperial units of the NBA player measurements to metric, the test checks if the conversion is right.
#Testing Technique:
Since the API response can change in any given time, we used Mocking to substitutes and imitates the real object to eliminate any failures within our test suite.
Furthermore,  we used patch() as a decorator to provide a scope in which we will mock our target object.

# Coding style tests
We used Flake8 because is easy to setup.
One of the useful features we found is the flag to run Flake8 only for the specific type of warnings, errors, etc.
After trying flake8 multiple times you’re realizing that some set of commands with Flake8 are the same. Good thing Flake8 supports creating and storing configuration file. You can change the Flake8 settings globally by editing its config file.

# Built With
•	Pycharm – The IDE used to manage the tests and runs.
# Versioning
The Versioning management is delegated to Github the numbering is mainly a progress check for how big are the changes.
# Authors
•	Sharon Yaroshetsky 
•	Ilan Kroter 
•	Noy Nir 
Students of Sami Shamoon Collegue of Engineering in Ashdod.
# License
This project is open source, you might freely use anything on it if you see fit.
# Acknowledgments
•	CoronaVirus for fucking us up with the team meeting.
•	Danny Park(ynnadkrap)- for using his NBA API.
•	Yaniv Ben Zvi- the project mentor.

