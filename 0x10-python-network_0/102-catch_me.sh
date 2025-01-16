#!/bin/bash
# get the response from 0.0.0.0:5000/catch_me
curl -sL -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me_2
