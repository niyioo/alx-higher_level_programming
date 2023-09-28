#!/bin/bash
# This script sends a JSON POST request with file contents and displays the response body
curl -s -X POST -H "Content-Type: application/json" --data @"$2" "$1"
