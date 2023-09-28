#!/bin/bash
# This script sends a GET request to a URL and displays the body of a 200 status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | [ "$(cat)" -eq 200 ] && curl -s "$1"
