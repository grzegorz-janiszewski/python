import pytest

def dodaj(a, b):
    return float(a) + float(b)

def odejmij(a, b):
    return float(a) - float(b)

def mnozenie(a, b):
    return float(a) * float(b)

def dzielenie(a, b):
    return float(a) / float(b)

def test_dodaj1():
    assert dodaj(1, 3) == 4

def test_dodaj2():
    assert dodaj(209, 10) == 219

def test_dodaj3():
    assert dodaj(-1, 3) == 2

def test_dodaj4():
    assert dodaj(1.4, 3) == 4.4

def test_dodaj5():
    assert dodaj(1.000000000004, 3) == 4.000000000004

def test_dodaj6():
    assert dodaj(0, 0) == 0

def test_dodaj7():
    assert dodaj(2, "7") == 9

def test_dodaj7():
    assert dodaj("-4", "7") == 3

def test_odejmij1():
    assert odejmij(2, 5) == -3

def test_odejmij2():
    assert odejmij(22, -5) == 27

def test_odejmij3():
    assert odejmij(0.000000002, -0.00002) == 2.0002000000000003e-05

def test_odejmij2():
    assert odejmij("22", -5) == 27

def test_mnozenie1():
    assert mnozenie(2, 3) == 6

def test_mnozenie2():
    assert mnozenie(3, 10) == 30

def test_mnozenie3():
    assert mnozenie(-2, 0.2) == -0.4

def test_mnozenie4():
    assert mnozenie("-2", 0.2) == -0.4

def test_mnozenie5():
    assert mnozenie(-2, "0.2") == -0.4

def test_dzielenie1():
    with pytest.raises(ZeroDivisionError):
        dzielenie(1, 0)

def test_dzielenie2():
    assert dzielenie(5, 2) == 2.5

def test_dzielenie3():
    with pytest.raises(ZeroDivisionError):
        dzielenie(1, "0")