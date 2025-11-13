def priority_non_preemptive(arrival, burst, priority):
    """
    arrival: list of arrival times of processes
    burst:   list of burst times
    priority: list of priority values (smaller value = higher priority, for this example)
    
    Returns a list of dicts for each process with CT (completion time), TAT (turnaround time), WT (waiting time)
    """
    n = len(arrival)
    # list of process indices
    proc_indices = list(range(n))
    # we will sort by arrival time first, then during selection use priority
    # keep result holders
    completion = [0] * n
    turnaround = [0] * n
    waiting = [0] * n
    
    time = 0
    
    # mark which processes are done
    done = [False] * n
    done_count = 0
    
    while done_count < n:
        # find all ready (arrived & not done) processes
        ready = [i for i in proc_indices if (arrival[i] <= time and not done[i])]
        if not ready:
            # no process ready now → advance time
            time += 1
            continue
        
        # pick from ready the process with highest priority (smallest priority value)
        # tie-break by arrival time or index
        selected = min(ready, key=lambda i: (priority[i], arrival[i]))
        
        # start it now
        time += burst[selected]
        completion[selected] = time
        turnaround[selected] = completion[selected] - arrival[selected]
        waiting[selected] = turnaround[selected] - burst[selected]
        done[selected] = True
        done_count += 1
    
    # build results
    result = []
    for i in range(n):
        result.append({
            'pid':        i,
            'arrival':    arrival[i],
            'burst':      burst[i],
            'priority':   priority[i],
            'completion': completion[i],
            'turnaround': turnaround[i],
            'waiting':    waiting[i]
        })
    return result

if __name__ == "__main__":
    arrival_times = [0, 2, 4, 5]
    burst_times   = [3, 6, 4, 5]
    priorities    = [2, 1, 4, 3]  # lower number => higher priority
    results = priority_non_preemptive(arrival_times, burst_times, priorities)
    
    print("PID | AT | BT | Pr | CT | TAT | WT")
    total_tat = 0
    total_wt  = 0
    for r in results:
        print(f"P{r['pid']}   | {r['arrival']}  | {r['burst']}  | {r['priority']}  | {r['completion']}  | {r['turnaround']}  | {r['waiting']}")
        total_tat += r['turnaround']
        total_wt  += r['waiting']
    print(f"\nAverage TAT = {total_tat / len(results):.2f}")
    print(f"Average WT  = {total_wt  / len(results):.2f}")