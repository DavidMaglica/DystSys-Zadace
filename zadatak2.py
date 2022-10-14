def fn(ls, dikt):
    """
    Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne
    error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
    liste tipa integer. Vraca novi dictionary, gdje je value element iz liste na
    tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.
    """
    if isinstance(ls, list) and isinstance(dikt, dict) and len(ls) == len(dikt):
        return({k:v if v in range(5, 11) and isinstance(k, int) else -1 for k, v in zip(dikt, ls) }) # range(5, 11) zbog off by one behavioura
    else:
        return("Error")


print(fn([8,7,1], {1:2,2:1,3:2}))