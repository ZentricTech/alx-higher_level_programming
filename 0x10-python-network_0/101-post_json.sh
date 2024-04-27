#!/bin/bash
# sends JSON POST req to URL passed as first arg, & displays body of response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
