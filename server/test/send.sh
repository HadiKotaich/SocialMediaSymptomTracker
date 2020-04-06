
sed -e "s/XXXX/$1/g;s/YYYY/$2/g" template_x_y.json > result.json

curl --header "Content-Type: application/json"   \
  --request POST   --data \
  "`cat result.json`" \
  https://gw.cmtelecom.com/v1.0/message
