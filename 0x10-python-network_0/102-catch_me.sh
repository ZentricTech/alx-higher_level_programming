#!/bin/bash
#  request to 0.0.0.0:5000/catch_me; server respond - You got me!
curl -sLX PUT 0.0.0.0:5000/catch_me -o /dev/null -w 'HTTP/1.1 %{http_code}\\nYou got me!\\n'|
