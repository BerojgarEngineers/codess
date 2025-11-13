def sjf_preemptive(arrival, burst):
    # number of processes
    n = len(arrival)
    # copy of burst times to track how much time remains for each process
    remaining = burst.copy()
    # list to mark whether each process is finished
    finished  = [False] * n
    # current time in simulation
    time      = 0
    # count of how many processes have completed
    done_count = 0
    # list to store results (completion, turnaround, waiting) for each process
    results   = []

    # Loop until all processes are completed
    while done_count < n:
        # find the index of process to run now (that has arrived, not finished, smallest remaining)
        idx     = -1
        min_rem = float('inf')
        for i in range(n):
            if (arrival[i] <= time) and (not finished[i]) and (remaining[i] < min_rem) and (remaining[i] > 0):
                min_rem = remaining[i]
                idx     = i

        # If no process is ready (either all arrived later or none left), advance time
        if idx == -1:
            time += 1
            continue

        # “Run” that chosen process for 1 unit of time
        remaining[idx] -= 1
        time           += 1

        # If this process has finished (remaining time becomes 0)
        if remaining[idx] == 0:
            finished[idx]  = True
            done_count    += 1
            # completion time is current time
            CT  = time
            # turnaround time = completion time − arrival time
            TAT = CT - arrival[idx]
            # waiting time = turnaround time − original burst time
            WT  = TAT - burst[idx]
            # store the result for this process
            results.append({
                'pid':        idx,
                'arrival':    arrival[idx],
                'burst':      burst[idx],
                'completion': CT,
                'turnaround': TAT,
                'waiting':    WT
            })

    return results

if __name__ == "__main__":
    arrival_times = [0, 1, 2, 3]
    burst_times   = [8, 4, 3, 2]
    # run the scheduling simulation
    res = sjf_preemptive(arrival_times, burst_times)

    print("PID | AT | BT | CT | TAT | WT")
    total_tat = total_wt = 0
    # sort results by process id so output is in order P0, P1, …
    for r in sorted(res, key=lambda x: x['pid']):
        print(f"P{r['pid']} | {r['arrival']}  | {r['burst']}  | {r['completion']}  | {r['turnaround']}  | {r['waiting']}")
        total_tat += r['turnaround']
        total_wt  += r['waiting']

    # print average turnaround and waiting time
    print(f"\nAverage Turnaround Time = {total_tat/len(res):.2f}")
    print(f"Average Waiting Time    = {total_wt/len(res):.2f}")