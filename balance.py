

import util


def hands(path, layout):
    keys = layout.keys
    string = ''
    strings = {}
    on_hand = 'L'
    def add():
        nonlocal string, strings
        if len(string) < 3: return
        try:
            strings[string] += 1
        except KeyError:
            strings[string] = 1
        string = ''

    with util.read_file_or_stdin(path) as f:
        while True:
            c = f.read(1)
            if not c: break
            try:
                hand = keys[c].finger[0]
            except KeyError:
                add()
                continue
            if hand == on_hand:
                string += c
            else:
                on_hand = hand
                add()
    return strings


# {'a': 100}, {'o': 100}
def balance(charcounts, layout):
    lkeys = {}
    rkeys = {}
    for c, n in charcounts.items():
        hand = layout.keys[c].finger[0]  # finger might be e.g. RI
        if hand == 'R':
            rkeys[c] = n
        elif hand == 'L':
            lkeys[c] = n
    return lkeys, rkeys


def fingers(charcounts, layout):
    # Iterate over finger->keylist mapping and change each keylist into a dict.
    fingers = {}
    for f, keys in layout.fingers().items():
        keydict = {}
        for k in keys:
            k = k.value
            try:
                count = charcounts[k]
            except KeyError:
                break
            keydict[k] = count
        fingers[f] = keydict
    return fingers


