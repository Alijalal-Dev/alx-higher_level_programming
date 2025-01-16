#!/bin/bash
# Display the status code
curl -so /dev/null -w "%{http_code}" "$1"
