def optimal_page_replacement(pages, capacity):
    """ Simulate the Optimal (OPT) Page Replacement algorithm.:param pages: list of page references (integers)
    :param capacity: number of frames in memory :return: number of page faults"""
    frames = []
    page_faults = 0

    for i, page in enumerate(pages):
        if page in frames:
            # Hit: no page fault
            print(f"Page {page} → HIT    | Frames: {frames}")
        else:
            # Miss / page fault
            page_faults += 1
            if len(frames) < capacity:
                # free frame available
                frames.append(page)
                print(f"Page {page} → MISS (loaded)             | Frames: {frames}")
            else:
                # choose a victim page: the one in frames whose next use is farthest in future (or never used again)
                # For each page in frame, find how far in future it is used next
                farthest_index = -1
                victim = None
                for f in frames:
                    try:
                        next_use = pages[i+1:].index(f)
                    except ValueError:
                        # if f not used again, we can pick it immediately
                        victim = f
                        break
                    if next_use > farthest_index:
                        farthest_index = next_use
                        victim = f
                # replace victim
                frames[frames.index(victim)] = page
                print(f"Page {page} → MISS (evicted {victim})     | Frames: {frames}")

    print(f"\nTotal Page Faults: {page_faults}")
    return page_faults

# Example usage:
if __name__ == "__main__":
    page_references = [1,2,3,4,2,1]
    memory_capacity = 3
    optimal_page_replacement(page_references, memory_capacity)