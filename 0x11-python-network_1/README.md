# Project Title

## Project Description

This repository contains a collection of Python scripts for the "0x11. Python - Network #1" project at Holberton School. These scripts are designed to perform various network-related tasks using Python, including fetching internet resources, sending HTTP requests, and handling HTTP errors. They are part of the learning objectives for this project, which include understanding how to use libraries such as urllib and requests, working with HTTP GET and POST requests, handling HTTP errors, and more.

## Project Tasks

### Task 0: What's my status?

- **Script:** [0-hbtn_status.py](0x11-python-network_1/0-hbtn_status.py)
- **Description:** This Python script fetches the status of a specific URL (`https://alx-intranet.hbtn.io/status`) using the urllib package. It then displays information about the response body, including its type, content in bytes, and content in UTF-8.

### Task 1: Response header value

- **Script:** [1-hbtn_header.py](0x11-python-network_1/1-hbtn_header.py)
- **Description:** This Python script takes a URL as input, sends an HTTP request to that URL using urllib, and displays the value of the `X-Request-Id` variable found in the response header.

### Task 2: POST an email

- **Script:** [2-post_email.py](0x11-python-network_1/2-post_email.py)
- **Description:** This Python script takes a URL and an email as input, sends a POST request to the specified URL with the email as a parameter, and displays the body of the response after decoding it in UTF-8.

### Task 3: Error code

- **Script:** [3-error_code.py](0x11-python-network_1/3-error_code.py)
- **Description:** This Python script takes a URL as input, sends an HTTP request to that URL using urllib, and displays the body of the response after decoding it in UTF-8. It also handles urllib.error.HTTPError exceptions and prints the HTTP status code if it's greater than or equal to 400.

### Task 4: What's my status? #1

- **Script:** [4-hbtn_status.py](0x11-python-network_1/4-hbtn_status.py)
- **Description:** This Python script fetches the status of a specific URL (`https://alx-intranet.hbtn.io/status`) using the requests package. It then displays information about the response body, including its type and content.

### Task 5: Response header value #1

- **Script:** [5-hbtn_header.py](0x11-python-network_1/5-hbtn_header.py)
- **Description:** This Python script takes a URL as input, sends an HTTP request to that URL using requests, and displays the value of the `X-Request-Id` variable in the response header.

### Task 6: POST an email #1

- **Script:** [6-post_email.py](0x11-python-network_1/6-post_email.py)
- **Description:** This Python script takes a URL and an email as input, sends a POST request to the specified URL with the email as a parameter using requests, and displays the body of the response.

### Task 7: Error code #1

- **Script:** [7-error_code.py](0x11-python-network_1/7-error_code.py)
- **Description:** This Python script takes a URL as input, sends an HTTP request to that URL using requests, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it also prints an error message with the HTTP status code.

### Task 8: Search API

- **Script:** [8-json_api.py](0x11-python-network_1/8-json_api.py)
- **Description:** This Python script takes a letter as input and sends a POST request to `http://0.0.0.0:5000/search_user` with the letter as a parameter. It handles different cases such as empty response, valid JSON, and invalid JSON, displaying results accordingly.

### Task 9: My GitHub!

- **Script:** [10-my_github.py](0x11-python-network_1/10-my_github.py)
- **Description:** This Python script takes GitHub credentials (username and personal access token) as input and uses the GitHub API to display the user's ID. It uses Basic Authentication with the personal access token as the password.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- Your code should use the pycodestyle (version 2.8.*) for style checking
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'` to check)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)
- Follow specific requirements for each script as mentioned in the project instructions.

## Usage

Each script can be executed individually by running the corresponding Python file. For example, to run Task 0, use the following command:

```bash
./0-hbtn_status.py
```

Make sure to follow the specific usage instructions for each script as mentioned in the project requirements.

## Author

- [Guillaume](https://github.com/Guillaume-R)
- CTO at Holberton School

## License

Copyright © 2023 ALX, All rights reserved.
