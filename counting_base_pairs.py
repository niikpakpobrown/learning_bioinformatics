strDNA = "3’-TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGATT-5’"

def countBase(strDNA):
    '''Counts the number of bases'''
    dict = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for x in strDNA:
        for key, val in dict.items():
            if key == x:
                dict[key] += 1
    return(dict)

print(countBase(strDNA))