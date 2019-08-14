import requests
from huginnTask import config, auth

def try_login(username:str, password:str) -> requests.Session:    

    r = requests.Session()

    log = r.post(config.login_url, params = {
        "userName": username,
        "passWord": password
    })

    if not "ADMIN" in str(log.text) and not "USER" in str(log.text):
        raise RuntimeError("权限验证出错: ", r.text)

    return r

if __name__ == "__main__":
    from config import username, password
    session = try_login(username, password)
    print(session)