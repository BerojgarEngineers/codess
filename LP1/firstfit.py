def first_fit(block_sizes, process_sizes):
    """
    block_sizes: list of ints (sizes of memory blocks)
    process_sizes: list of ints (sizes of processes needing allocation)

    Returns a list allocation of length len(process_sizes):
      allocation[i] = index of block assigned to process i, or -1 if none.
    """
    # Initialize allocation array: -1 means unallocated
    allocation = [-1] * len(process_sizes)

    # Copy block sizes so we can reduce them when allocating
    blocks = block_sizes.copy()

    for i, p_size in enumerate(process_sizes):
        for j, b_size in enumerate(blocks):
            if b_size >= p_size:
                # allocate process i to block j
                allocation[i] = j
                # reduce available size of block j
                blocks[j] -= p_size
                break  # move to next process

    return allocation


if __name__== "__main__":
    blocks = [100, 250, 200, 300, 150]
    processes = [150, 350, 200, 100]
    alloc = first_fit(blocks, processes)
    print("Block sizes:", blocks)
    print("Process sizes:", processes)
    print("Allocation result:", alloc)
    # Also print a nicer view
    for i, p_size in enumerate(processes):
        if alloc[i] != -1:
            print(f"Process {i} (size={p_size}) → Block {alloc[i]} (original size={blocks[alloc[i]] + p_size})")
        else:
            print(f"Process {i} (size={p_size}) → not allocated")