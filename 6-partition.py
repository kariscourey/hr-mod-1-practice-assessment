def partition(list, size):
    chunks = []
    in_progress = []
    for item in list:
        if len(in_progress) == size:
            chunks.append(in_progress)
            in_progress = []
        in_progress.append(item)
    return chunks

input = [0, 1, 2, 3, 4, 5, 6]

result = partition(input, 2)
print(result)
