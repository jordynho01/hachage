def mon_hachage_perso(chaine):
    # 1. Valeur initiale (un nombre premier est préférable)
    hash_value = 5381
    
    # Masque pour simuler un entier de 64 bits (Python gère les entiers arbitrairement grands)
    # 0xFFFFFFFF correspond à (2^64 - 1)
    mask = 0xFFFFFFFFFFFFFFFFF

    for char in chaine:
        # 2. Récupérer le code Unicode du caractère
        code_ascii = ord(char)
        
        # 3. Mixage : (hash * 33) XOR code_ascii
        # Le décalage de 5 (hash << 5) est équivalent à hash * 32
        hash_value = ((hash_value << 5) + hash_value) ^ code_ascii
        
        # 4. Appliquer le masque pour rester sur 32 bits
        hash_value &= mask

    # Retourner la valeur en hexadécimal pour le format "classique"
    return hex(hash_value)

# Test
print(f"Test 1: {mon_hachage_perso('je suis un message haché')}")
print(f"Test 2: {mon_hachage_perso('nyembo')}") # Différent juste par la casse
