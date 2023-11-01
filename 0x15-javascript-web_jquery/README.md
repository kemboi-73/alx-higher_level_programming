# Project: 0x15. JavaScript - Web jQuery

## Description
This project focuses on utilizing JavaScript and the jQuery library for front-end web development. You will complete various tasks to manipulate the Document Object Model (DOM), perform AJAX requests, and achieve specific learning objectives.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:

**General:**
- Understand why jQuery makes front-end programming easier.
- Select HTML elements in JavaScript.
- Select HTML elements with jQuery.
- Differentiate between ID, class, and tag name selectors.
- Modify an HTML element's style.
- Get and update HTML element content.
- Modify the DOM.
- Make a GET request with jQuery Ajax.
- Make a POST request with jQuery Ajax.
- Listen/bind to DOM events.
- Listen/bind to user events.

## Requirements
**General:**
- Allowed editors: vi, vim, emacs.
- All your files will be interpreted on Chrome (version 57.0).
- All your files should end with a new line.
- A README.md file at the root of the project folder is mandatory.
- Your code should be semistandard compliant with the flag `--global $: semistandard *.js --global $`.
- You must use jQuery version 3.x.
- You are not allowed to use `var`.
- HTML should not reload for each action, such as DOM manipulation, update values, and fetching data.

## Manual QA Review
It is your responsibility to request a review for this project from a peer before the project's deadline. If no peers have reviewed, you should request a review from a TA or staff member.

## Tasks
1. **No JQuery**
    - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000).
    - You must use `document.querySelector` to select the HTML tag.
    - You can't use the jQuery API.

2. **With JQuery**
    - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000).
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

3. **Click and Turn Red**
    - Write a JavaScript script that updates the text color of the `<header>` element to red (#FF0000) when the user clicks on the tag `DIV#red_header`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

4. **Add `.red` Class**
    - Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

5. **Toggle Classes**
    - Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`.
    - The `<header>` element must always have one class: `red` or `green`, never both at the same time and never empty.
    - If the current class is `red`, when the user clicks on `DIV#toggle_header`, the class must be updated to `green`, and vice versa.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

6. **List of Elements**
    - Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`.
    - The new element must be: `<li>Item</li>`.
    - The new element must be added to `UL.my_list`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

7. **Change the Text**
    - Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

8. **Star Wars Character**
    - Write a JavaScript script that fetches the character name from the URL: [https://swapi-api.alx-tools.com/api/people/5/?format=json](https://swapi-api.alx-tools.com/api/people/5/?format=json).
    - The name must be displayed in the HTML tag `DIV#character`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

9. **Star Wars Movies**
    - Write a JavaScript script that fetches and lists the titles for all movies using this URL: [https://swapi-api.alx-tools.com/api/films/?format=json](https://swapi-api.alx-tools.com/api/films/?format=json).
    - All movie titles must be listed in the HTML tag `UL#list_movies`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.

10. **Say Hello!**
    - Write a JavaScript script that fetches from [https://hellosalut.stefanbohacek.dev/?lang=fr](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays the value of "hello" from that fetch in the HTML tag `DIV#hello`.
    - The translation of "hello" must be displayed in the HTML tag `DIV#hello`.
    - You can't use `document.querySelector` to select the HTML tag.
    - You must use the jQuery API.
    - Your script must work when imported from the `<head>` tag.

**Note:** The HTML files and corresponding JavaScript files for each task are provided in the project repository.

## Copyright
© 2023 ALX. All rights reserved.

Please complete the tasks for each numbered item following the provided instructions and requirements. If you have any questions or need further assistance, feel free to ask.
