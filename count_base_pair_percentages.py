
def base_percentage(strDNA):
    """Returns the base percentages"""
    dict = {'A': 0, 'G': 0, 'C': 0, 'T' : 0}

    for x in strDNA:
        for key, value in dict.items():
            if key == x:
                dict[key] += 1

    for key, value in dict.items():
        dict[key] = (value / sum(dict.values())) * 100

    return dict


strDNA = "3’-TACTCTCGTTCTTGCAGCTTGTCAGTACTTTCAGAATCATGGTGTGCATGGTAGAATGACTCTTATAACGAACTTCGACATGGCAATAACCCCCCGATT-5’"

print(base_percentage(strDNA))
