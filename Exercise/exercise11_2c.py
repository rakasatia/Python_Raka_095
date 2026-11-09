def city_country(city, country, population=""):
    """Mengembalikan kota dan negara; populasi bersifat opsional."""
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" – population {population}"

    return result