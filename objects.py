

class Layout:
    def __init__(self, positions, keys, fingers, costs):
        self.keys = { k:Key(p,k,f,int(c)) for p,k,f,c in
            zip(positions, keys, fingers, costs) }

    def print(self):
        for key in self.keys.values():
            if key.position in ["B01", "C01"]: print()
            print(key.value, end=' ')
        print()

    def _group(self, keyfunc):
        groups = {}
        for key in self.keys.values():
            try:
                groups[keyfunc(key)].append(key)
            except KeyError:
                groups[keyfunc(key)] = [key]
        return groups

    def fingers(self):
        return self._group(lambda k: k.finger)

    def difficulties(self):
        return self._group(lambda k: k.ease)


class Key:
    def __init__(self, position, value, finger, ease):
        self.position = position
        self.value = value
        self.finger = finger
        self.ease = ease

    def __repr__(self):
        return self.value
