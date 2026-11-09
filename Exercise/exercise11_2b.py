from exercise11_2a import city_country

def test_city_country():
    """Test lama ini sengaja dijalankan untuk menunjukkan kegagalan tahap wajib."""
    result = city_country("Edinburgh", "Skotlandia")
    assert result == "Edinburgh, Skotlandia"
