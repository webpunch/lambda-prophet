[Original story](https://medium.com/@marc.a.metz/docker-run-rm-it-v-pwd-var-task-lambci-lambda-build-python3-7-bash-c7d53f3b7eb2).
[Original repo](https://github.com/marcmetz/How-To-Deploy-Facebook-Prophet-on-AWS-Lambda)

# Instructions

Build package:

```
docker build -t prophet .
```

Test function:

```
docker run prophet python3 local.py
```

Run a server:

```
docker run -p 4128:4128 prophet python3 server.py
```

Deploy:

```
docker save prophet | ssh -C ubuntu@3.239.164.172 sudo docker load
ssh ubuntu@3.239.164.172
docker run serve
```
