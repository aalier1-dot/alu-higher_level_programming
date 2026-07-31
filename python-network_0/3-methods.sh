#!/bin/bash
# Displays all HTTP methods the server accepts
curl -s -X OPTIONS -i "$1" | grep Allow | cut -d" " -f2-
