## Fetch Job from worker.py
from huginnTask.worker import fetch_job, finish_job

token = ("mvn-2233","mvn123456")

runner_name = "RUNNER-3"
group_name = "zsw_g"
fetch_count = 10
promise_return_seconds = 10

result = fetch_job(runner_name, group_name, fetch_count, promise_return_seconds, token)
print("Fetched Job: ", len(result))
print("Result is ", result)

# Finished Job from worker.py
ids = []
for res in result:
	id = res["id"]
	ids.append(id)
import random
for t_id in ids:
	print("Finishing Job For ", t_id)
	st = random.choice(["FINISHED","FAILED"])
	res = "RESULT" + str(random.randint(10000,99999))
	no = random.choice([None, "Note" + str(random.randint(10000,99999))])
	finish_job(runner_name, group_name, t_id, st, res, no, token)
