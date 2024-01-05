#!/bin/bash
# Uses curl to send a request to a URL and then displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
