def fcfs(arrival, burst):
    """
    arrival: list of arrival times of processes
    burst:   list of burst times of processes
    Returns a list of dicts for each process with CT, TAT, WT.
    """
    n = len(arrival)
    # sort processes by arrival time (keeping original index)
    proc = sorted(range(n), key=lambda i: arrival[i])
    completion = [0] * n
    waiting    = [0] * n
    turnaround = [0] * n
    
    time = 0
    for i in proc:
        if time < arrival[i]:
            time = arrival[i]
        time += burst[i]
        completion[i] = time
        turnaround[i] = completion[i] - arrival[i]
        waiting[i] = turnaround[i] - burst[i]
    
    result = []
    for i in range(n):
        result.append({
            'pid':       i,
            'arrival':   arrival[i],
            'burst':     burst[i],
            'completion': completion[i],
            'turnaround': turnaround[i],
            'waiting':    waiting[i]
        })
    return result

if __name__ == "__main__":
    arrival_times = [0, 2, 4, 5]
    burst_times   = [3, 6, 4, 5]
    res = fcfs(arrival_times, burst_times)
    
    print("PID | AT | BT | CT | TAT | WT")
    total_tat = total_wt = 0
    for r in res:
        print(f"P{r['pid']}   | {r['arrival']}  | {r['burst']}  | {r['completion']}  | {r['turnaround']}   | {r['waiting']}")
        total_tat += r['turnaround']
        total_wt  += r['waiting']
    
    print(f"\nAverage Turnaround Time = {total_tat / len(res):.2f}")
    print(f"Average Waiting Time    = {total_wt  / len(res):.2f}")