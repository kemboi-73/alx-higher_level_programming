# 0x14. JavaScript - Web scraping

## Description

This project consists of several JavaScript scripts for web scraping and data manipulation. It covers a range of tasks to help you learn and practice JavaScript programming while working with web data.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the significance of JavaScript programming.
- Manipulate JSON data effectively.
- Utilize the request and fetch API for making web requests.
- Read and write files using the fs module.

## Copyright and Plagiarism

Remember that plagiarism is strictly forbidden. You are required to come up with your own solutions to the tasks in this project. Copying and pasting someone else's work or publishing the project content is not allowed and may result in removal from the program.

## Requirements

- Editors allowed: vi, vim, emacs
- All files will be interpreted on Ubuntu 20.04 LTS using Node.js (version 14.x)
- All files must end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/node`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should follow the semi-standard coding style (StandardJS with semicolons).
- All your files must be executable.
- Do not use the `var` keyword.

## Project Tasks

### Task 0: Readme

Write a script that reads and prints the content of a file.

- The first argument is the file path.
- The content of the file must be read in utf-8.
- If an error occurs during the reading, print the error object.

Example:
```bash
$ cat cisfun
C is super fun!
$ ./0-readme.js cisfun
C is super fun!

$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### Task 1: Write me

Write a script that writes a string to a file.

- The first argument is the file path.
- The second argument is the string to write.
- The content of the file must be written in utf-8.
- If an error occurs while writing, print the error object.

Example:
```bash
$ ./1-writeme.js my_file.txt "Python is cool"
$ cat my_file.txt ; echo ""
Python is cool
```

### Task 2: Status code

Write a script that displays the status code of a GET request.

- The first argument is the URL to request (GET).
- The status code must be printed like this: `code: <status code>`.
- You must use the `request` module.

Example:
```bash
$ ./2-statuscode.js https://alx-intranet.hbtn.io/status
code: 200

$ ./2-statuscode.js https://alx-intranet.hbtn.io/doesnt_exist
code: 404
```

### Task 3: Star Wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

- The first argument is the movie ID.
- Use the Star Wars API with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`.
- You must use the `request` module.

Example:
```bash
$ ./3-starwars_title.js 1
A New Hope

$ ./3-starwars_title.js 5
Attack of the Clones
```

### Task 4: Star Wars Wedge Antilles

Write a script that prints the number of movies where the character "Wedge Antilles" is present.

- The first argument is the API URL of the Star Wars API: `https://swapi-api.alx-tools.com/api/films/`.
- Wedge Antilles is character ID 18; your script must use this ID for filtering the result of the API.
- You must use the `request` module.

Example:
```bash
$ ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films
3
```

### Task 5: Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

- The first argument is the URL to request.
- The second argument is the file path to store the body response.
- The file must be UTF-8 encoded.
- You must use the `request` module.

Example:
```bash
$ ./5-request_store.js http://loripsum.net/api loripsum
$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. ...
```

### Task 6: How many completed?

Write a script that computes the number of tasks completed by user id.

- The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`.
- Only print users with completed tasks.
- You must use the `request` module.

Example:
```bash
$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

## Resources

To successfully complete these tasks, you may need to refer to the following resources:

- Working with JSON data
- The workflow of accessing the attributes of a simply-created JSON object
- `request` module
- Modern JavaScript

## Author

- Guillaume, CTO at Holberton School

If you have any questions or need further clarification on any of the tasks, feel free to ask for assistance. Happy coding!
