def reverseLookup(dictionary, value):

    finding_keys = []

    for key, val in dictionary.items():
        if val == value:
            finding_keys.append(key)

    return finding_keys 

Lookup = { "Alina": 18, "Veronika": 20, "Zarina": 13, "Margo": 18}

print("Keys:" , reverseLookup(Lookup, 18))
