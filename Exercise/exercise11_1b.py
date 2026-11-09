from exercise11_1a import city_country

def test_city_country():
    """Menguji format kota dan negara."""
    result = city_country("Edinburgh", "Skotlandia")
    assert result == "Edinburgh, Skotlandia"
