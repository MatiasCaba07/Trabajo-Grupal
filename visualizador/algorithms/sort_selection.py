# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"
    
def step():
    global items, n, i, j, min_idx, fase

    if i >= n - 1:
        return {"a": -1, "b": -1, "swap": False, "done": True}

    if fase == "buscar":
        a = min_idx
        b = j
        swap = False

        if j < n:
            if items[j] < items[min_idx]:
                min_idx = j

            j += 1

            if j == n:
                fase = "swap"

            return {"a": a, "b": b, "swap": swap, "done": False}

        fase = "swap"

    if fase == "swap":
        swap = False
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap = True

        a = i
        b = min_idx
        i += 1

        if i >= n - 1:
            return {"a": a, "b": b, "swap": swap, "done": True}

        j = i + 1
        min_idx = i
        fase = "buscar"

        return {"a": a, "b": b, "swap": swap, "done": False}
