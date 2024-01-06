#!/bin/bash
# Uses curl to send a DELETE request to a URL and then displays the body of the response
curl -sX DELETE "$1"
