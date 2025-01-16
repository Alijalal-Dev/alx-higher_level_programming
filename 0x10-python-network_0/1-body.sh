#!/bin/bash
# respons for 200 status code
curl -sL -o /dev/null -w "%{http_code}" "$1" | grep -q "200" && curl -sL "$1"
