from exercise11_2c import city_country


def test_city_country():
    """Menguji fungsi tanpa populasi."""
    result = city_country("santiago", "chile")
    assert result == "Santiago, Chile"


def test_city_country_population():
    """Menguji fungsi dengan populasi."""
    result = city_country("santiago", "chile", 5000000)
    assert result == "Santiago, Chile – population 5000000"