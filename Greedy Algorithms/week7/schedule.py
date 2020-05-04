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

    def __lt__(self, other):
        # jobs have equal difference (weight - length),
        # you should schedule the job with higher weight first.
        # reverted < with > as we use reversed min heap
        return self.weight > other.weight

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
        complete_time += job.weight * (job.length + last_length)
        last_length += job.length
    print(f"Score: {complete_time}")
    return complete_time

def test_quiz(input):
    with open(input) as file:
        number = int(file.readline())
        jobs = []
        for line in file:
            weight, length = map(int, line.split())
            jobs.append(Job(weight, length))
        # (weight - length) = 31
        schedule(jobs, score_dif)
        # (weight/length) = 29
        schedule(jobs, score_ratio)

test_quiz("test_quiz1")
test_quiz("quiz1")


