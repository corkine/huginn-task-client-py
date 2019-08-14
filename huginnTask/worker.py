import requests
import huginnTask.auth as auth
import huginnTask.config as config

def fetch_job(
    runner_name:str, group_name:str, 
    fetch_count:int, return_group_in_seconds:int, 
    token:tuple):  

    group_job = config.server_url + "/job/" + group_name

    get_url = group_job + "/fetch"

    get_options = {
        "groupId": group_name,
        "number": str(fetch_count),
        "runner": runner_name,
        "workerPromiseReturnSeconds": return_group_in_seconds
    }

    s = auth.try_login(token[0], token[1])
    res = s.get(get_url, params= get_options)

    given_task = res.json()
    
    return given_task

def finish_job(
    runner_name:str, group_name:str,
    taskId: int, status:str, result:str, note:str, token:tuple):

    finish_job_url = config.server_url + "/job/" + group_name + "/finish"

    if note == None:
        post_options = {
            "runner": runner_name,
            "taskId": str(taskId),
            "status": status.upper(),
            "result": result
        }
    else:
        post_options = {
            "runner": runner_name,
            "taskId": str(taskId),
            "status": status.upper(),
            "result": result,
            "note": note
        }

    s = auth.try_login(token[0], token[1])
    res = s.post(finish_job_url, params = post_options)

    result = res.json()

    return result