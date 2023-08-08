# data2bots_test
# JSON Schema Generation

This Python script generates JSON schema files based on input data files. It provides a structured way to define the schema structure, types, and properties of your JSON data.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Introduction

The JSON Schema Generation script processes input JSON data files, analyzes the structure and types of the data, and generates corresponding JSON schema files. This can be useful for ensuring data consistency and providing a clear representation of the expected data format.
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file 
- Dumps the output in (./schema/)

## Installation

1. Clone the repository to your local machine:
<pre>

'git clone https://github.com/adekingsley/data2bots_test.git'

</pre>

2. cd data2botss_test to enter the directory
<pre>

'cd data2bots_test'

</pre>
4. Install dependencies using `pip`: 
<pre>

'pip install requirements.txt'

</pre>

## Usage

1. Place your input JSON data files in the `work/data` folder.

2. Run the script to generate JSON schema files:
<pre>

'python main.py'

</pre>

3. The generated schema files will be saved in the `work/schema` folder.

## Project Structure

The project is structured as follows:

data2bots_test/
├── main.py
├── assignment.py
├── requirements.txt
└── tests/
├── test_assignment.py
.
- `main.py`: Orchestrates the schema generation process.
- `assignment.py`: Contains the utility functions for determining types and processing dictionaries.
- `requirements.txt`: Lists project dependencies.
- `tests/test_assignment.py`: Contains unit tests for the utility functions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

When contributing, please follow the existing code style and ensure that your changes are well-documented.

