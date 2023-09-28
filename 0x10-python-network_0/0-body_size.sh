#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
