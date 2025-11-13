def next_fit(block_sizes, process_sizes):
    """
    block_sizes: list of ints (sizes of memory blocks)
    process_sizes: list of ints (sizes of processes needing allocation)

    Returns:
      allocation: list such that allocation[i] = index of block assigned or -1 if none
      remaining: list of remaining sizes of each block after allocation
    """
    m = len(block_sizes)
    allocation = [-1] * len(process_sizes)
    blocks = block_sizes.copy()
    j = 0  # pointer to the block to start searching from

    for i, p_size in enumerate(process_sizes):
        start = j
        allocated = False
        # loop over blocks circularly
        while True:
            if blocks[j] >= p_size:
                allocation[i] = j
                blocks[j] -= p_size
                allocated = True
                j = (j + 1) % m  # next search starts from next block
                break
            j = (j + 1) % m
            if j == start:
                break

        # if not allocated, j remains at next block anyway (for next process)
    return allocation, blocks

if __name__ == "__main__":
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]
    alloc, remaining = next_fit(blocks, processes)
    print("Initial block sizes:", blocks)
    print("Process sizes:", processes)
    print("Allocation result (process → block index):", alloc)
    print("Remaining block sizes after allocation:", remaining)
    for i, p in enumerate(processes):
        if alloc[i] != -1:
            print(f"Process {i} (size={p}) → Block {alloc[i]} (remaining size = {remaining[alloc[i]]})")
        else:
            print(f"Process {i} (size={p}) → Not allocated")