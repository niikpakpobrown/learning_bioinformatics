
def complement_bp(strDNA):
    """This function returns the complemenent of a sequence"""
    comp_list = {'3' : '5', '5' : '3', 'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C', '’' : '’', '-' : '-'}
    complement = ""
    for x in strDNA:
        for key, value in comp_list.items():
            if x == key:
                complement += value

    return complement

strDNA = "3’-TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGATT-5’"

print(complement_bp(strDNA))

                
        