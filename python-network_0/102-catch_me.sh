#!/bin/bash
# Sends a crafted request to trigger the hidden catch_me response
curl -s -L -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
