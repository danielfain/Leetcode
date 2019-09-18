class MapSum:
    def __init__(self):
        self.hm = {}

    def insert(self, key, value):
        self.hm[key] = value

    def sum(self, prefix):
        total = 0
        for key, value in self.hm.items():
            if key[:len(prefix)] == prefix:
                total += value

        return total

ms = MapSum()
ms.insert("test", 5)
ms.insert("adadada", 5)
ms.insert("testinggg", 5)
ms.insert("teaaa", 5)
ms.insert("tesadadt", 5)
print(ms.sum("tes"))