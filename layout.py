
from constants import LAYOUTDIR, COSTDATA, FINGERDATA, POSDATA


class Layout:
    def __init__(self, positions, keys, fingers, costs):
        self.keys = { k:Key(p,k,f,int(c)) for p,k,f,c in
            zip(positions, keys, fingers, costs) }

    def print(self):
        keys = sorted(self.keys.values(), key=lambda key: key.position)
        for key in keys:
            if key.position == 'B01':
                print('\n', end=' ')
            elif key.position == 'C01':
                print('\n', end='  ')
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

    def positions(self):
        return self._group(lambda k: k.position)


class Key:
    def __init__(self, position, value, finger, ease):
        self.position = position
        self.value = value
        self.finger = finger
        self.ease = ease

    def __repr__(self):
        return self.value


def load(name, costpath=COSTDATA, fingerpath=FINGERDATA, pospath=POSDATA):
    with open(pospath, 'r') as f:
        poslist = f.read().split()
    with open(LAYOUTDIR+name, 'r') as f:
        keylist = f.read().split()
    with open(fingerpath, 'r') as f:
        fingerlist = f.read().split()
    with open(costpath, 'r') as f:
        costlist = f.read().split()
    return Layout(poslist, keylist, fingerlist, costlist)
