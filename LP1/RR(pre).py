def round_robin(arrival, burst, quantum):
    # number of processes
    n = len(arrival)
    # copy of burst times so we know how much each still needs
    remaining = burst.copy()
    # completion times of each process (init zero)
    completion = [0] * n
    # turn-around times
    turnaround = [0] * n
    # waiting times
    waiting = [0] * n
    # time when current CPU time is
    time = 0
    # queue of process indices ready to run
    ready_queue = []
    # track which have arrived
    arrived = [False] * n
    # count of finished processes
    finished_count = 0

    # keep looping until all finish
    while finished_count < n:
        # add newly arrived processes to ready queue
        for i in range(n):
            if arrival[i] <= time and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        if not ready_queue:
            # if no one is ready, just advance time
            time += 1
            continue

        # pick next process from front of ready queue
        idx = ready_queue.pop(0)

        # if its burst remaining is bigger than quantum
        if remaining[idx] > quantum:
            # run it for quantum
            time += quantum
            remaining[idx] -= quantum
            # during this quantum, new arrivals might come – add them
            for i in range(n):
                if arrival[i] <= time and not arrived[i]:
                    ready_queue.append(i)
                    arrived[i] = True
            # after quantum ends, put this process at end of ready queue
            ready_queue.append(idx)
        else:
            # if remaining time ≤ quantum, it will finish now
            time += remaining[idx]
            remaining[idx] = 0
            # mark completion time, turnaround time, waiting time
            completion[idx] = time
            turnaround[idx] = completion[idx] - arrival[idx]
            waiting[idx]    = turnaround[idx] - burst[idx]
            finished_count += 1
            # optionally don’t re-queue finished

    # return results
    return completion, turnaround, waiting

if __name__ == "__main__":
    arrival_times = [0, 1, 2, 3]
    burst_times   = [5, 4, 2, 1]
    time_quantum  = 2
    comp, tat, wt = round_robin(arrival_times, burst_times, time_quantum)

    print("PID | AT | BT | CT | TAT | WT")
    for i in range(len(arrival_times)):
        print(f"P{i}   | {arrival_times[i]}  | {burst_times[i]}  | {comp[i]}   | {tat[i]}    | {wt[i]}")
    avg_tat = sum(tat)/len(tat)
    avg_wt  = sum(wt)/len(wt)
    print(f"\nAverage Turnaround Time = {avg_tat:.2f}")
    print(f"Average Waiting Time    = {avg_wt:.2f}")