
# 0x0D. SQL - Introduction

![SQL Logo](https://upload.wikimedia.org/wikipedia/en/thumb/6/68/MySQL.svg/1200px-MySQL.svg.png)

## Description

This repository contains a series of SQL scripts that cover the fundamental concepts of databases and SQL. Each script performs a specific task related to databases using MySQL as the chosen database management system.

The tasks in this project are designed to help you grasp the basic concepts of databases, SQL statements, and database manipulation. By completing these tasks, you will gain practical experience with creating databases, tables, and performing various operations on them.

## Learning Objectives

Upon completing this project, you will have acquired the following skills:

- Understanding of databases and relational databases.
- Knowledge of SQL and its role in database manipulation.
- Familiarity with MySQL as a database management system.
- Creating databases and tables using Data Definition Language (DDL).
- Executing queries to retrieve, insert, update, and delete data.
- Exploring advanced SQL techniques, such as functions and subqueries.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts should be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All script files must end with a newline character
- All SQL queries should be commented just before the query
- All script files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`)
- A `README.md` file at the root of the project folder is mandatory
- The length of your files will be tested using `wc`

## Installation

To run the scripts in this project, you'll need to have MySQL 8.0 installed on your Ubuntu 20.04 LTS system. If you don't have it installed, you can follow these steps to install it:

```bash
$ sudo apt update
$ sudo apt install mysql-server
```

You can verify the installation by checking the version:

```bash
$ mysql --version
```

## Usage

To execute the SQL scripts in this project, you can use the following command structure:

```bash
$ cat script_file.sql | mysql -hlocalhost -uroot -p
Enter password:
```

Replace `script_file.sql` with the name of the script file you want to execute. The command will prompt you for your MySQL root password.

## Project Structure

- `0-list_databases.sql`: Script to list all databases on the MySQL server.
- `1-create_database_if_missing.sql`: Script to create a database (`hbtn_0c_0`) if it doesn't exist.
- `2-remove_database.sql`: Script to delete the `hbtn_0c_0` database if it exists.
- `3-list_tables.sql`: Script to list all tables in a specified database.
- `4-first_table.sql`: Script to create a table called `first_table` in the current database.
- `5-full_table.sql`: Script to print the full description of the `first_table` in the `hbtn_0c_0` database.
- `6-list_values.sql`: Script to list all records in the `first_table`.

## Acknowledgments

- Resources and tutorials on databases and SQL concepts.
- [MySQL Documentation](https://dev.mysql.com/doc/): For detailed information about MySQL.
- [ALX - Higher Level Programming](https://github.com/username/repo): The original repository for this project.

## Authors

- Guillaume

---

**Project Deadline: August 16, 2023, 6:00 AM (UTC)**
