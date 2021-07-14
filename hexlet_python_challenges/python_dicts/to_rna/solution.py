MAPPING = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
}


def to_rna(nucleotide):

    rna = []
    for item in nucleotide:
        rna.append(MAPPING[item])

    return "".join(rna)


# Альтернативный вариант с использованием map
# def to_rna(nucleotide):
#     return ''.join(map(MAPPING.get, nucleotide))
