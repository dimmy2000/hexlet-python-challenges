import solution


def test_to_rna():
    assert solution.to_rna("C") == "G"
    assert solution.to_rna("G") == "C"
    assert solution.to_rna("T") == "A"
    assert solution.to_rna("A") == "U"
    assert solution.to_rna("ACGTGGTCTTAA") == "UGCACCAGAAUU"
