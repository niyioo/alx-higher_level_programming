#!/bin/bash
# This script displays all HTTP methods the server will accept for a URL
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
