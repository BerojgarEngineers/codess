def best_fit(block_sizes, process_sizes):
    """
    block_sizes: list of ints (sizes of memory blocks)
    process_sizes: list of ints (sizes of processes needing allocation)

    Returns:
      allocation: list of same length as process_sizes, allocation[i] = index of block assigned or -1 if none
      remaining: list of remaining sizes of each block after allocation
    """
    m = len(block_sizes)
    n = len(process_sizes)
    allocation = [-1] * n
    blocks = block_sizes.copy()

    for i in range(n):
        p_size = process_sizes[i]
        best_idx = -1
        # find block that fits and leaves minimal leftover
        for j in range(m):
            if blocks[j] >= p_size:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        # allocate if found
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= p_size

    return allocation, blocks

if __name__== "__main__":
    blocks = [100, 500, 200, 300, 600]
    processes = [212, 417, 112, 426]
    alloc, remaining = best_fit(blocks, processes)
    print("Initial block sizes:", blocks)
    print("Process sizes:", processes)
    print("Allocation result (process → block index):", alloc)
    print("Remaining block sizes:", remaining)
    for i, p_size in enumerate(processes):
        if alloc[i] != -1:
            print(f"Process {i} (size={p_size}) → Block {alloc[i]} (remaining size after = {remaining[alloc[i]]})")
        else:
            print(f"Process {i} (size={p_size}) → Not allocated")