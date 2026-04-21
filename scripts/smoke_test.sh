#!/bin/bash

set -eou pipefail

URL="http://127.0.0.1:5000"

docker build -t flask-app .
docker run --rm -p 5000:5000 flask-app &

echo "Waiting for the Flask app to start..."
sleep 5

echo "Performing smoke test by sending a request to $URL"

HTTP_RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$HTTP_RESPONSE" -eq 200 ]; then
    echo "Flask app is up and running! HTTP Status Code: $HTTP_RESPONSE"
else
    echo "Flask app is not responding correctly. HTTP Status Code: $HTTP_RESPONSE"
    exit 1
fi

exit 0
