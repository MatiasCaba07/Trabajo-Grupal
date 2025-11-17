elementos = []
norte = 0
i = 0
j = 0

def init(vals):
    global elementos, norte, i, j
    elementos = list(vals)
    norte = len(elementos)
    i = 0
    j = 0

def step():
    global elementos, norte, i, j

    # Si ya terminamos todas las pasadas
    if i >= norte - 1:
        return {"done": True}

    # Si j llegó al final de la pasada, avanzar i
    if j >= norte - i - 1:
        i += 1
        j = 0
        if i >= norte - 1:
            return {"done": True}

    # Indices
    a = j
    b = j + 1
    swap = False

    # Swap si corresponde
    if elementos[a] > elementos[b]:
        elementos[a], elementos[b] = elementos[b], elementos[a]
        swap = True

    # Avanzar j
    j += 1

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }
