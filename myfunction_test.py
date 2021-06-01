
def request(account: str, password: int, callback: (str, str)):
    if password == 8888:
        callback(account + "123", 30)
    else:
        callback(account + "456", 100)
