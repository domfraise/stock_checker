# stock_checker

## Local Dev
`pip install requests`
`pip install beautifulsoup4`
`pip install html5lib`

## AWS Deploy
`docker build -t stock-checker .`
`docker tag  stock-checker:latest 739866317750.dkr.ecr.us-east-2.amazonaws.com/stock-checker:latest`
`docker push 739866317750.dkr.ecr.us-east-2.amazonaws.com/stock-checker:latest`