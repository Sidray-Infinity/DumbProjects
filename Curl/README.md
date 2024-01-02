# cURL from scratch using python
## Usages
### GET
```bash
python3 ccurl.py http://eu.httpbin.org/get
python3 ccurl.py http://eu.httpbin.org/get -X GET
```

### DELETE
```bash
python3 ccurl.py http://eu.httpbin.org/delete -X DELETE
```

### POST
```bash
python3 ccurl.py http://eu.httpbin.org/post -X POST -d '{"key": "value"}'
```

### PUT
```bash
python3 ccurl.py http://eu.httpbin.org/put -X PUT -d '{"key": "value2"}'
```

Ref: 
* https://codingchallenges.fyi/challenges/challenge-curl/
* https://datatracker.ietf.org/doc/html/rfc9110