#!/bin/bash
# sends request to URL passed as arg & displays status code of the response
curl -o /dev/null -w '%{http_code}' -sLI "$1"
