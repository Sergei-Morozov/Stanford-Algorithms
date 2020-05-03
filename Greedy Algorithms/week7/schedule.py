"""
Scheduling jobs(priotiy, length) in 1 resource
- minimize weighted sums E priotiry*l
- to achieve: calculate job score, execute in score order
"""
from dataclasses import dataclass

@dataclass
class Job:
    weight: int
    length : int

def score_dif(job):
    """
    Compute score base on diff
    """
    return job.weight - job.length

def score_ratio(job):
    """
    Compute score based on ratio
    """
    return job.weight/job.length


from heapq import heappush, heappop
def schedule(jobs, priority):
    """
    Compute score
    """
    ordered = []
    for job in jobs:
        # to have max heap from standart min heap just revert priority
        heappush(ordered, (-priority(job), job))

    complete_time = 0
    last_length = 0
    while ordered:
        score, job = heappop(ordered)
        print(score, job)
        complete_time += job.weight * (job.length + last_length)
        last_length += job.length
    print(f"Score: {complete_time}")

jobs = [Job(3,5), Job(1,2)]
schedule(jobs, score_ratio)

schedule(jobs, score_dif)



