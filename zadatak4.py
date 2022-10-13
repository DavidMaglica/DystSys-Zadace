def fn(ls1, ls2):
    """
    Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
    Error. Vraca novu listu usporedujuci elemente na istim indeksima. Ako
    su vrijednosti iste, vraca taj element, ako nisu vraca -1 na toj poziciji.
    (Funkcija mora imati dvije linije)
    """
    if isinstance(ls1, list) and isinstance(ls2, list) and len(ls1) == len(ls2):
        return([-1 if item1 != item2 else item1 for item1, item2 in zip(ls1, ls2)])        

print(fn([1, 2, 3, 4, 5], [2, 2, 4, 4, 5]))