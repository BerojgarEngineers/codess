def lru_page_replacement(pages, capacity):
    """ Simulate LRU page replacement.:param pages: list of page references, e.g. [1, 2, 1, 3, 4]
    :param capacity: number of frames in memory
    :return: number of page faults
    """
    frames = []         # current pages in memory
    page_faults = 0

    for page in pages:
        if page in frames:
            # HIT: page already in memory → mark it as most recently used
            frames.remove(page)
            frames.append(page)
            print(f"Page {page} → HIT   | Frames: {frames}")
        else:
            # MISS: page not in memory → page fault
            page_faults += 1
            if len(frames) < capacity:
                # free frame available
                frames.append(page)
                print(f"Page {page} → MISS  (loaded)         | Frames: {frames}")
            else:
                # frames full → evict the least recently used (first element)
                evicted = frames.pop(0)
                frames.append(page)
                print(f"Page {page} → MISS  (evicted {evicted}) | Frames: {frames}")

    print(f"\nTotal page faults: {page_faults}")
    return page_faults

# Example usage:
if __name__ == "__main__":
    page_references = [0,1,7,2,3,2,7,1,0,3]
    memory_capacity = 4
    lru_page_replacement(page_references, memory_capacity)