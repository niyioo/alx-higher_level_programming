#!/bin/bash
# This script makes a request and displays the response
curl -s -L -X PUT 0.0.0.0:5000/catch_me -d "user_id=98"
