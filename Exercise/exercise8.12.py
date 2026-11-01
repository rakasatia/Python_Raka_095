def buat_sandwich(*bahan):
    """Mencetak ringkasan sandwich yang dipesan."""
    print("\nKamu memesan sandwich dengan bahan:")
    for satu_bahan in bahan:
        print(f"- {satu_bahan}")


buat_sandwich('keju')
buat_sandwich('ayam', 'selada', 'tomat')
buat_sandwich('tuna', 'mayones', 'timun', 'bawang bombay')