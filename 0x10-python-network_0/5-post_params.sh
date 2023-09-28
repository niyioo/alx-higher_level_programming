#!/bin/bash
# This script sends a POST request to a URL with custom variables and displays the response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
