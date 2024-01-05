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
response_body_size=$(			# Store the result in this variable
	curl -sI "$url" |			# Sends a HEAD request (`-I` option) to the specified url (`$url`) using `curl`
	grep -i Content-Length |	# Filters headers to include only lnes containing "Content-Length," case-insensitive (`-i`)
	awk '{print $2}' |		# Extracts the second field (column) from the filtered line (the actual size of the response body in this case)
	tr -d '\r\n'				# Removes any carriage return (\r) or newline (\n) characters from the extracted value
)

# Check if Content-Length header is present in the response
if [ -n "$response_body_size" ]; then
	echo "${response_body_size}"
fi
