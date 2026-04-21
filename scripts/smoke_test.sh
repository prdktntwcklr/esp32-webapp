#!/bin/bash

set -eou pipefail

PORT=5000
URL="http://127.0.0.1:$PORT"
HEALTH_URL="$URL/health"

# First, check if the Flask app is responding
echo "Performing smoke test by sending a request to $URL"

HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$HTTP_RESPONSE" -eq 200 ]; then
    echo "Flask app is up and running! HTTP Status Code: $HTTP_RESPONSE"
else
    echo "Flask app is not responding correctly. HTTP Status Code: $HTTP_RESPONSE"
    exit 1
fi

# Then, check the health check endpoint
echo "Checking health check endpoint at $HEALTH_URL"

HEALTH_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $HEALTH_URL)

if [ "$HEALTH_RESPONSE" -eq 200 ]; then
    echo "Health check passed! HTTP Status Code: $HEALTH_RESPONSE"
else
    echo "Health check failed. HTTP Status Code: $HEALTH_RESPONSE"
    exit 1
fi

exit 0
