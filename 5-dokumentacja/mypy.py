# ZMIENNA ----------------

# Tutaj jest dobrze
x: int = 5

# Tutaj powinien być błąd
x = "string"


# FUNKCJA ----------------

# Tutaj jest dobrze
def zwracamInt() -> int:
    return 1

# Tutaj powinien być błąd
def zwracamString() -> str:
    return 1
