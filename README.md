# UD_FSND_Tournament_Results

## Project Overview

The "Tournament Results" project is part of the Udacity Full Stack Nanodegree program. This repository showcases a website that is backed by a PostgreSQL database, designed to manage and display results for a tournament. The project implements a database schema that is well-normalized and adheres to best practices in database design. It includes a series of unit tests to ensure the application functions correctly under various scenarios.

### Project Structure

- `tournament.sql` - This file contains all PostgreSQL database schema definitions for the tables and views used in the project.
- `tournament.py` - This Python script includes all the functions required to interact with the database, such as connecting to the PostgreSQL server, registering players, recording matches, and fetching standings.
- `tournament_test.py` - A set of unit tests provided to validate the functions in the `tournament.py` script.

## Setup and Installation

### Prerequisites

- Python 2.7 or higher
- PostgreSQL
- psycopg2 Python library

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/UD_FSND_Tournament_Results.git
   cd UD_FSND_Tournament_Results
   ```

2. **Set up the PostgreSQL database**
   - Log in to your PostgreSQL console. Depending on your installation, you might do this with:
     ```bash
     psql -U postgres
     ```
   - Create the database:
     ```sql
     CREATE DATABASE tournament;
     ```
   - Connect to the database:
     ```sql
     \c tournament
     ```
   - Import the schema:
     ```bash
     \i tournament.sql
     ```

3. **Install Python dependencies (if not already installed)**
   ```bash
   pip install psycopg2
   ```

## Usage

To run the application, you need to execute the Python scripts provided. Here's how you can run the tests to make sure everything is set up correctly:

```bash
python tournament_test.py
```

This script will test several functionalities such as:
- Registering players
- Recording matches
- Checking player standings
- Ensuring that players are matched for games correctly

## Contributing

Contributions to the UD_FSND_Tournament_Results project are welcome! Here are a few ways you can contribute:
- Reporting bugs
- Suggesting enhancements
- Submitting pull requests for open issues

If you are submitting a pull request, please ensure your changes pass all tests. New features should also be accompanied by additional tests where feasible.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

This README provides a basic guide to getting started with the UD_FSND_Tournament_Results project. For more detailed information, please refer to the specific files and code within the repository.