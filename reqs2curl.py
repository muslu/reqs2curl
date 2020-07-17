## Author: Muslu YÜKSEKTEPE @Makdos
## for Python 3

def to_curl(request, verify=True):
    parameters = [f'curl -X {request.method}']

    for k, v in request.headers.items():
        if k == 'User-Agent':
            parameters.append('-H "User-Agent: Muslu Reqs2Curl v.0.1"')
        else:
            parameters.append(f'-H "{k}: {v}"')

    if request.body:
        body = request.body
        if isinstance(body, bytes):
            body = body.decode('utf-8')
        parameters.append(f'-d "{body}"')

    if not verify:
        parameters.append('--insecure ')

    parameters.append(f' {request.url}')

    return ' '.join(parameters)
