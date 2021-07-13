from solution import diff


def test_diff_modularity():
    assert diff(720, 0) == 0
    assert diff(-720, 0) == 0


def test_diff_in_same_quadrant():
    assert diff(60, 30) == 30
    assert diff(125, 120) == 5
    assert diff(200, 199) == 1
    assert diff(300, 340) == 40


def test_diff_commutativity():
    assert diff(0, 90) == diff(90, 0)
    assert diff(15, -15) == diff(-15, 15)
    assert diff(45, 315) == diff(315, 45)


def test_diff_difficult_cases():
    assert diff(0, 0) == 0
    assert diff(0, 180) == 180
    assert diff(30, 270) == 120
    assert diff(30, 240) == 150
    assert diff(240, 30) == 150
    assert diff(-100, 200) == 60
