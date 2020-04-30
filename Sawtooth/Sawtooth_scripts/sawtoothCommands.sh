curl --request POST \
     --header "Content-Type: application/octet-stream" \
     --data-binary @intkey.batches \
     "http://localhost:8008/batches"