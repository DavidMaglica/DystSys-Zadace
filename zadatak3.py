def fn(listOfDicts):
    """
    Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
    lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
    Provjerava imaju li svi dictionary odgovarajuca 3 kljuceva, ako ne error.
    (“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) Vraca novi nested
    dictionary s kljucem “ukupno” i dictionary sa kljucem “artikli” i listom
    svih odabranih artikala te “cijena” s ukupnom cijenom racuna.
    """
    if isinstance(listOfDicts, list):
            return{"ukupno": {"artikli": [item["naziv"] for item in listOfDicts], 
            "cijena": sum(item["cijena"] * item["kolicina"] for item in listOfDicts)}}

print(fn([{"cijena": 8, "naziv": "Kruh", "kolicina": 1},
    {"cijena": 13, "naziv": "Sok", "kolicina": 2},
    {"cijena": 7, "naziv": "Upaljac", "kolicina": 1}]))