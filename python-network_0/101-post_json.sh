#!/bin/bash
# Sends a JSON POST request using the content of a file passed as $2
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
