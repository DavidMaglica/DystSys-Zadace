def fn(ls):
    """
    Funkcija prima listu tuple-a o studentima (id, ime, prezime). Vraca novu
    sortiranu po id-u (manji->veci) listu dictionary-a o studentima kojima ime
    i prezime pocinje istim slovom. (One-liner u return-u)
    """
    return[{"id": id, "ime": name, "prezime": surname} for tupl in zip(sorted(ls)) 
    for (id, name, surname) in tupl if name[0] == surname[0]]

print(fn([
    (121, "Ivan", "Ivic"),
    (431, "Pero", "Horvat"),
    (31, "Marija", "Maric")]))