def FindClumps(text, k, L, t):
    '''
    A function to find clumps of k-mer in specific window within Genome to shed light 
    on the location of Ori
    INPUT:
    text - the genome as string
    k - the length of k-mer we're looking for
    L - the length of the window
    t - the window must have at least t-number of k-mer repetition to be considered
    OUTPUT:
    patterns - a list of possible k-mers

    '''
    patterns =[]
    length = len(text)
    # scanning the genome by window length
    for sub_text in range(0,length-L):
        window = text[sub_text:sub_text+L]
        freqMap = FrequencyTable(window, k)
        for pattern in freqMap.keys():
            if freqMap[pattern] >= t:
                patterns.append(pattern)
    # remove dublications
    patterns = list(set(patterns))
    return patterns