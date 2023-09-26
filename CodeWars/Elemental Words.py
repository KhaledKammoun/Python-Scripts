def elemental_forms(word):
    result = []

    def dfs(liste, i):
        if i >= len(word):
            result.append(liste.copy())
            return

        if i < len(word) and word[i].upper() in ELEMENTS:
            liste.append("{} ({})".format(ELEMENTS[word[i].upper()], word[i].upper()))
            dfs(liste, i + 1)
            liste.pop()

        if i + 1 < len(word) and (word[i].upper() + word[i + 1].lower()) in ELEMENTS:
            liste.append("{} ({})".format(ELEMENTS[word[i].upper() + word[i + 1].lower()], word[i].upper() + word[i + 1].lower()))
            dfs(liste, i + 2)
            liste.pop()
        if i +2 < len(word) and (word[i].upper() + word[i + 1].lower() + word[i + 2].lower()) in ELEMENTS:
            liste.append("{} ({})".format(ELEMENTS[word[i].upper() + word[i + 1].lower() + word[i + 2].lower()], word[i].upper() + word[i + 1].lower() + word[i + 2].lower()))
            dfs(liste, i + 3)
            liste.pop()
            
    dfs([], 0)
    return result
