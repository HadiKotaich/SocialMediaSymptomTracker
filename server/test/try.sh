curl --header "Content-Type: application/json"   \
  --request POST   --data \
  "`cat $1`" \
  http://server.withapi.com/try
