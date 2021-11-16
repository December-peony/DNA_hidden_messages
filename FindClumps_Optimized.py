from collections import defaultdict


def FindClumpsOptimized(text, k, L, t):
    '''
    A function to find clumps of k-mer in specific window within Genome to shed light 
    on the location of Ori
    INPUT:
    text - the genome as string
    k - the length of k-mer we're looking for
    L - the length of the window
    t - the window must have at least t-number of k-mer repetition to be considered
    OUTPUT:
    lis_kmers - a list of possible k-mers

    '''
    indexMap = defaultdict(list)
    # getting all possible k-mers and the indices where it starts as a list
    for i in range(len(text)-k):
        pattern = text[i:i+k]
        indexMap[pattern].append(i)
    lis_kmers=[]
    for pattern in indexMap.keys():
        count = len(indexMap[pattern])
        if count >= t:
            for i in range(count-1):
                if i+t-1 >= count:
                    break
                if (indexMap[pattern][i+t-1]+k)-indexMap[pattern][i] <= L:
                    lis_kmers.append(pattern)
                    # break to make no dublications
                    break  
    return lis_kmers