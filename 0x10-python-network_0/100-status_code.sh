#!/usr/bin/bash
# Displays the status code of the response of a request sent to a provided URL
curl -s -o /dev/null -w "%{http_code}" "$1"
