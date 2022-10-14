def fn(x):
    """
    Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
    Vraca novu listu, gdje su string-ovi duži od 4 znaka.
    """
    return([item  for item in x if len(item) > 4 and isinstance(item, str) == True])    
    
print(fn(["Pas", "Macka", "Stol"]))
