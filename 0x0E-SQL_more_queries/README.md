**Project- SQL Queries and Privileges**

This repository contains a set of SQL scripts and queries that are part of a school project for Holberton School. These scripts are designed to interact with a MySQL database and perform various tasks, including creating tables, populating data, and executing SQL queries.

### Contents

- `0-privileges.sql`: This script demonstrates how to manage user privileges in a MySQL database. It creates and grants privileges to `user_0d_1` and `user_0d_2`.

- `1-create_user.sql`: This script creates a MySQL user named `user_0d_1` with all privileges on the server.

- `2-create_read_user.sql`: This script creates a MySQL user named `user_0d_2` with only SELECT privileges on the `hbtn_0d_2` database.

- `3-force_name.sql`: This script creates a table named `force_name` in the specified database with certain constraints on column values.

- `4-never_empty.sql`: This script creates a table named `id_not_null` in the specified database with the default value and constraint for the `id` column.

- `5-unique_id.sql`: This script creates a table named `unique_id` in the specified database with a unique constraint on the `id` column.

- `6-states.sql`: This script creates a table named `states` in the specified database.

- `7-cities.sql`: This script creates a table named `cities` in the specified database with a foreign key relationship to the `states` table.

- `8-cities_of_california_subquery.sql`: This script retrieves a list of cities from the `cities` table that are associated with the state of California.

- `9-cities_by_state_join.sql`: This script retrieves a list of cities from the `cities` table along with their corresponding state names using a JOIN operation.

- `10-genre_id_by_show.sql`: This script retrieves a list of genres linked to the show "Dexter" from the `tv_shows` and `tv_show_genres` tables.

- `11-genre_id_all_shows.sql`: This script retrieves a list of all shows from the `tv_shows` table along with their corresponding genre IDs from the `tv_show_genres` table.

- `12-no_genre.sql`: This script retrieves a list of shows from the `tv_shows` table that do not have a genre linked.

- `13-count_shows_by_genre.sql`: This script retrieves a count of shows for each genre from the `tv_shows` and `tv_genres` tables.

- `14-my_genres.sql`: This script retrieves a list of genres linked to the show "Dexter" from the `tv_genres` table.

- `15-comedy_only.sql`: This script retrieves a list of shows from the `tv_shows` table that belong to the "Comedy" genre.

- `16-shows_by_genre.sql`: This script retrieves a list of shows from the `tv_shows` table along with the genres linked to each show.

### Instructions

1. Clone the repository to your local machine.
2. Import the provided SQL dump file (`hbtn_0d_tvshows.sql`) into your MySQL server.
3. Execute the SQL scripts using the following command:
   ```
   cat script_name.sql | mysql -hlocalhost -uroot -p database_name
   ```
   Replace `script_name.sql` with the name of the script you want to run, and replace `database_name` with the name of the target database.
4. Follow the output to see the results of each script's execution.

Please note that these scripts are designed for educational purposes and may require adjustments to work in different environments or with different databases. Always exercise caution when running SQL scripts, especially on production databases.
