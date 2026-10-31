rivers = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'bengawan solo': 'indonesia',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nSungai yang ada di dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nNegara yang ada di dictionary:")
for country in rivers.values():
    print(country.title())