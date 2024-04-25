#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -X OPTIONS -s -i "$1" | grep -i "Allow" | cut -d " " -f 2