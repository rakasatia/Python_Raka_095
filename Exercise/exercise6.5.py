nama_sungai = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'bengawan solo': 'indonesia',
}

for sungai, negara in nama_sungai.items():
    print(f"Sungai {sungai.title()} mengalir melalui {negara.title()}.")

print("\nSungai yang ada di dictionary:")
for sungai in nama_sungai.keys():
    print(sungai.title())

print("\nNegara yang ada di dictionary:")
for negara in nama_sungai.values():
    print(negara.title())