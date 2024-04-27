#!/bin/bash
#  URL arg, sends GET request to URL, and display  body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
