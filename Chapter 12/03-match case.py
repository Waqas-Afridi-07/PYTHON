def http_status(status):
    match status:
        case 200:
            return "ok"
    match status:
        case 404:
            return "Not found"
    match status:
        case 500:
            return "Internal server error"
    match status:
        case _:
            return "Unknown status"
        
print(http_status(500))