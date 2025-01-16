#!/bin/bash
# Send a JSON POST request and display the response
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
