# UD_FSND_Tournament_Results

## Project Overview

The "Tournament Results" is a project from the Udacity Full Stack Nanodegree program. This project showcases a website backed by a PostgreSQL database, with unit tests, meaningful table and column design, and adherence to best practices in database normalization. The purpose of this project is to create a database schema to store the game matches between players and to code a Python module to rank the players and pair them up in matches in a tournament.

## Setup and Installation

To set up and run this project, you need to have Python and PostgreSQL installed on your machine. If you don't have these installed, you can download and install them from their official websites.

Once you have Python and PostgreSQL installed, follow the steps below:

1. Clone this repository to your local machine using `git clone https://github.com/<your-github-username>/UD_FSND_Tournament_Results.git`
2. Navigate to the project directory `cd UD_FSND_Tournament_Results`
3. Run the command `pip install -r requirements.txt` to install the required dependencies.
4. Open PostgreSQL and create a new database named 'tournament'.
5. Import the `tournament.sql` file into your newly created database.
6. Run `python tournament_test.py` to run the unit tests.

## Usage

After setting up the project, you can use it by running the `tournament_test.py` script. This script will run a series of tests to ensure that the functions in the `tournament.py` module are working correctly. If all tests pass, you can be confident that the tournament database and functions are set up correctly.

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute. Also, please make sure to update tests as appropriate before making a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.