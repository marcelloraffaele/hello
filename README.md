# hello
A simple and little image that can be used to test simple API.
It's based on Python.

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
docker run --name hello -p 8080:8080 -e "MY_ENV_VAR=my_value" -d $IMG:$VER
```

URL that can be called with 200 status:
```
curl http://localhost:8080/
curl http://localhost:8080/api/hello
curl http://localhost:8080/api/time
curl http://localhost:8080/api/all-env
curl http://localhost:8080/api/env
curl http://localhost:8080/api/headers
```

and URL that can be called for error:
```
curl http://localhost:8080/api/error
curl http://localhost:8080/api/error401
curl http://localhost:8080/api/error403
```


## Stop
```
docker container stop hello
docker container rm hello
```

# Install on kubernetes using Helm
The project have a helm folder that can be used to release the `hello`.


## Dry run:
```
cd helm
helm install --generate-name --dry-run --debug hello > dry-run.yaml
```

## Install:
```
kubectl create ns test
helm install hello-test ./hello -n test
```

## Uninstall
```
helm uninstall hello-test -n test
kubectl delete ns test
```

# Path documentation
Here is a Markdown table describing each API path and what to expect from each:

| Path               | Method | Response Code | Content-Type         | Response Body                                      | Description                        |
|--------------------|--------|--------------|----------------------|----------------------------------------------------|------------------------------------|
| /                  | GET    | 200          | text/html (default)  | index.html                                         | Serves the main HTML page          |
| /api/hello         | GET    | 200          | application/json     | { message: "hello world" }                         | Returns a hello world message      |
| /api/test          | GET    | 200          | application/json     | { message: "this is a test" }                      | Returns a test message             |
| /api/version       | GET    | 200          | application/json     | { version: "1.0", date: "20250528" }               | Returns version and date info      |
| /api/time          | GET    | 200          | application/json     | {"status":"success","time":"$time_local","msec":"$msec"} | Returns server time and msec       |
| /api/error         | GET    | 500          | text/html            | (empty)                                            | Returns a 500 Internal Server Error|
| /api/error401      | GET    | 401          | text/html            | (empty)                                            | Returns a 401 Unauthorized error   |
| /api/error403      | GET    | 403          | text/html            | (empty)                                            | Returns a 403 Forbidden error      |
| /api/all-env        | GET    | 200          | application/json     | { ...all environment variables... }                 | Returns all environment variables  |
| /api/env            | GET    | 200/400      | application/json     | { name: "MY_ENV_VAR", value: "..." } or error      | Returns a single environment variable by name |
| /api/headers        | GET    | 200          | application/json     | { ...all request headers... }                       | Returns all request headers        |

 # ready to use images

 There's an image available for each branch:
| Branch | Image |
|--------|-------|
| main   | ghcr.io/marcelloraffaele/hello:main |
| blue   | ghcr.io/marcelloraffaele/hello:blue |
| green  | ghcr.io/marcelloraffaele/hello:green |
| under-construction | ghcr.io/marcelloraffaele/hello:under-construction |


this can be used to test blue-green deployment.
Example:
```bash
docker run --name hello -p 8080:8080 ghcr.io/marcelloraffaele/hello:main
# or
docker run --name hello -p 8080:8080 ghcr.io/marcelloraffaele/hello:blue
```