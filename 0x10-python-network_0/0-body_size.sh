#!/bin/bash
# Uses curl to send a request to a URL and then displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | tr -d '\r\n'
