import requests
import json
from huginnTask import config, auth

def get_status(group_name:str, token:tuple):

    group_task = config.server_url + "/task/" + group_name

    status_url = group_task + "/fetch"

    s = auth.try_login(token[0], token[1])
    status = s.get(status_url)
    return status.json()

def push_data(group_name:str, max_retry:int, push_data:list, token:tuple):

    push_task_url = config.server_url + "/task/push"

    push_task_data = push_data

    s = auth.try_login(token[0], token[1])

    status = s.post(push_task_url, params = {
        "maxWorkerRetryTime": max_retry
    }, json = push_data)

    return status.json()