def tambah(x, y):
    """Fungsi untuk menjumlahkan dua bilangan."""
    return x + y

def kurang(x, y):
    """Fungsi untuk mengurangkan dua bilangan."""
    return x - y

def kali(x, y):
    """Fungsi untuk mengalikan dua bilangan."""
    return x * y

def bagi(x, y):
    """Fungsi untuk membagi dua bilangan."""
    if y == 0:
        raise ValueError("Tidak bisa membagi dengan nol!")
    return x / y
