def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed as a error"
        case _:
            return "Something's wrong with the internet"
        
result = http_error(400)
print(result)

result = http_error(401)
print(result)