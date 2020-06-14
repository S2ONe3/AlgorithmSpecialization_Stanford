import heapq_max

if __name__ == '__main__':
    Jobs = []
    with open("jobs.txt") as f:
        for x in f:
            weight, length = map(int, x.split())
            #Jobs.append((weight-length, weight, length))
            Jobs.append((weight/length, weight, length))

    heapq_max.heapify_max(Jobs)

    currentTime = 0
    sum = 0
    while Jobs:
        job = heapq_max.heappop_max(Jobs)
        currentTime += job[2]
        sum += (job[1] * currentTime)

    print(sum)