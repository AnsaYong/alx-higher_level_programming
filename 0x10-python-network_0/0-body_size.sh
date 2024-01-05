#!/bin/bash
# Uses curl to send a request to a URL and then displays
# the size of the body of the response

# Check if a URL is provided as an argument
if [ $# -eq 0 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and measure the size of the response body
response_body_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n')

# Check if Content-Length header is present in the response
if [ -n "$response_body_size" ]; then
	echo "${response_body_size}"
fi
