# Project README

## Table of Contents
1. [Project Description](#project-description)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Files](#files)
5. [Contributing](#contributing)
6. [License](#license)

---

### 1. Project Description

This project consists of a set of Python scripts that interact with a MySQL database named `hbtn_0e_0_usa` and `hbtn_0e_4_usa`. The scripts are designed to perform various tasks related to querying and manipulating data in the database. Each script is explained in detail below:

#### 0-select_states.py

This script lists all states from the database `hbtn_0e_0_usa`. It takes three arguments: MySQL username, MySQL password, and the database name. The results are sorted in ascending order by `states.id` and displayed as follows:

```
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
```

#### 1-filter_states.py

This script lists all states with a name starting with 'N' (uppercase) from the database `hbtn_0e_0_usa`. It also takes three arguments: MySQL username, MySQL password, and the database name. The results are sorted in ascending order by `states.id` and displayed similarly to the previous script.

#### 2-my_filter_states.py

Similar to the previous script, this one takes four arguments: MySQL username, MySQL password, database name, and a state name to search for. It displays the state that matches the provided name, and the results are sorted by `states.id`.

#### 3-my_safe_filter_states.py

This script is an improved version of `2-my_filter_states.py`, designed to be safe from SQL injection attacks. It takes the same four arguments and displays the state that matches the provided name, with the results sorted by `states.id`.

#### 4-cities_by_state.py

This script lists all cities from the database `hbtn_0e_4_usa`. It takes three arguments: MySQL username, MySQL password, and the database name. The results are sorted in ascending order by `cities.id` and include the associated state as well.

#### 5-filter_cities.py

This script takes four arguments: MySQL username, MySQL password, database name, and a state name to search for. It lists all cities of the specified state from the database `hbtn_0e_4_usa`, with the results sorted by `cities.id`.

#### 6-model_state.py

This script defines a Python class named `State` and an instance of `Base` using SQLAlchemy. The `State` class represents a table in the database, with attributes `id` and `name`.

#### 7-model_state_fetch_all.py

This script lists all `State` objects from the database `hbtn_0e_6_usa`. It takes three arguments: MySQL username, MySQL password, and the database name. The results are sorted in ascending order by `states.id`.

#### 8-model_state_fetch_first.py

This script prints the first `State` object from the database `hbtn_0e_6_usa`. It takes three arguments: MySQL username, MySQL password, and the database name. If no states are found in the database, it prints "Nothing."

#### 9-model_state_filter_a.py

This script lists all `State` objects from the database `hbtn_0e_6_usa` that contain the letter 'a' in their names. It takes three arguments: MySQL username, MySQL password, and the database name. The results are sorted in ascending order by `states.id`.

#### 10-model_state_my_get.py

This script prints the `states.id` of a `State` object with the name provided as an argument. It takes four arguments: MySQL username, MySQL password, database name, and the state name to search for. If no state with the provided name is found, it prints "Not found."

#### 11-model_state_insert.py

This script adds a new `State` object with the name "Louisiana" to the database `hbtn_0e_6_usa`. It takes three arguments: MySQL username, MySQL password, and the database name. It also prints the `states.id` of the newly added state.

---

### 2. Requirements 

To run these scripts, you need the following:

- Python 3.x
- MySQL server
- MySQLdb module for Python
- SQLAlchemy module for Python

Ensure that you have the necessary MySQL database (`hbtn_0e_0_usa` and `hbtn_0e_4_usa`) set up with the provided schema.

---

### 3. Usage 

To use these scripts, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/alx-higher_level_programming.git`
2. Navigate to the project directory: `cd alx-higher_level_programming/0x0F-python-object_relational_mapping`
3. Run the desired script with the required arguments. For example:

```bash
./0-select_states.py mysql_username mysql_password hbtn_0e_0_usa
```

Replace `mysql_username` and `mysql_password` with your MySQL credentials.

---

### 4. Files 

Here is a list of the script files included in this project:

- `0-select_states.py`
- `1-filter_states.py`
- `2-my_filter_states.py`
- `3-my_safe_filter_states.py`
- `4-cities_by_state.py`
- `5-filter_cities.py`
- `6-model_state.py`
- `7-model_state_fetch_all.py`
- `8-model_state_fetch_first.py`
- `9-model_state_filter_a.py`
- `10-model_state_my_get.py`
- `11-model_state_insert.py`

---

### 5. Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your changes: `git checkout -b feature/your-feature-name`
4. Make your changes and commit them with descriptive commit messages.
5. Push your changes to your forked repository.
6. Create a pull request on the original repository.

---

### 6. License 

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
