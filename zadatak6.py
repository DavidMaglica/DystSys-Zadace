from heapq import merge


def fn(x, y):
    """
    Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
    ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
    Vraca se spojena lista ili dictionary.
    """
    return(x + y if type(x) == type(y) and isinstance(x, list) and isinstance(y, list) else {**x, **y})


print(fn([1,2,1,2],[3,2]))
print(fn({1:2,3:2},{5:2,4:1}))