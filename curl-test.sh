#!/bin/bash

NAME="User$(shuf -i 1000-9999 -n 1)"
EMAIL="user$(shuf -i 1000-9999 -n 1)@example.com"
CONTENT="This is a test post with random content $(shuf -i 1000-9999 -n 1)"

POST_RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post -d "name=${NAME}&email=${EMAIL}&content=${CONTENT}")
POST_ID=$(echo $POST_RESPONSE | jq -r '.id')

if [ "$POST_ID" != "null" ]; then
    echo "POST request successful: Created timeline post with ID ${POST_ID}"
else
    echo "POST request failed"
    exit 1
fi

GET_RESPONSE=$(curl -s http://localhost:5000/api/timeline_post)
echo $GET_RESPONSE | jq -e ".timeline_posts[] | select(.id == ${POST_ID})" > /dev/null

if [ $? -eq 0 ]; then
    echo "GET request successful: Verified timeline post with ID ${POST_ID} exists"
else
    echo "GET request failed: Timeline post with ID ${POST_ID} not found"
    exit 1
fi
