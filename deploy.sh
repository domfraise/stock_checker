docker build -t stock-checker .
aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 739866317750.dkr.ecr.us-east-2.amazonaws.com
docker tag  stock-checker:latest 739866317750.dkr.ecr.us-east-2.amazonaws.com/stock-checker:latest
docker push 739866317750.dkr.ecr.us-east-2.amazonaws.com/stock-checker:latest