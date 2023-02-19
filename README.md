# hello
A simple and little image that can be used to test simple API.
It's based on nginx open source.

# Build
If you want to rebuild it locally:
```
IMG="rmarcello/hello"
VER="1.0"
docker build --no-cache -t $IMG:$VER .
```

# Test
## Run
```
docker run --name hello -p 8080:80 -d $IMG:$VER
```

URL that can be called with 200 status:
```
curl http://localhost:8080/
curl http://localhost:8080/hello
curl http://localhost:8080/time
```

and URL that can be called for error:
```
curl http://localhost:8080/error
curl http://localhost:8080/error401
curl http://localhost:8080/error403
```


## Stop
```
docker container stop hello
docker container rm hello
```

# Push
```
docker push $IMG:$VER
```

