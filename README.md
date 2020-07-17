
## Author: Muslu YÜKSEKTEPE @Makdos
## for Python 3

# reqs2curl
> Form Python requests's request to CURL command.


`Usage:`

```url = 'https://api.muslu.org/v1/'
 payload = {
    'access_token': 'access_token',`
    "data": {
        "id": 123213,
    }
 }

 dd = requests.post(url, data=payload, verify=False)
 print(dd)

 import reqs2curl
 print(reqs2curl.convert_curl(dd.request, verify=False))
```
