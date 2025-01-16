#!/bin/bash
# All the allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
