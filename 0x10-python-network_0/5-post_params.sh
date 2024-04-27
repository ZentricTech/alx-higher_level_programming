#!/bin/bash
# URL, sends a POST request to the passed URL & displays body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
