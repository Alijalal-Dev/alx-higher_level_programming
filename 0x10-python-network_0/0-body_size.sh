#!/bin/bash
# dispaly the size of the response
curl -s "$1" | wc -c
