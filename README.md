# partibus

## Usage

### Python

```Python
import partibus
lemmas = partibus.lemmatize("facturusne operae pretium sim")
```

### Command line

```Shell
$ python3 -m partibus facturusne operae pretium sim
```

### HTTP server

```Shell
$ python3 -m partibus.http_server
```

```Shell
$ curl -X POST http://localhost:5000/lemmatize       \
    -H "Content-Type: application/json"              \
    -d '{"words": "facturusne operae pretium sim"}'
```
