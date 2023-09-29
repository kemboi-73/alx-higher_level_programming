#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept it
curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
