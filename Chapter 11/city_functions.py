def city_country(city, country, population=""):
    """Return a string of the form 'City, Country'."""
    if population:
        return f"{city.title()}, {country.title()} - Population: {population}"
    return f"{city.title()}, {country.title()}"