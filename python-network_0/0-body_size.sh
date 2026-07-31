#!/bin/bash
# Displays size of response body in bytes
curl -s -o /dev/null -w "%{size_download}" "$1"
