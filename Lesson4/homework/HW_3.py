def find_kmers(s, k):
    kmers = []
    for i in range(len(s) - k + 1):
        a = s[i:i + k]
        if a not in kmers:
            kmers.append(s[i:i + k])
    return print(kmers)


find_kmers("ATCGGATTCG", 3)
