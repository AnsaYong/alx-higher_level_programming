#!/bin/bash
# Uses curl to display all HTTP methods that that will be accepted by the server of a given URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
