class Batary:
    def __init__(self, max_charge=5):
        self.capacity = []
        self.max_charge = max_charge

    def charge(self):
        if len(self.capacity) < self.max_charge:
            self.capacity.append(")")
        else:
            print("Батарея полностью заряжена")

    def discharge(self):
        if len(self.capacity) > 0:
            self.capacity.pop()
        else:
            print("Батарея разряжена")

    def __str__(self):
        return "[" + "".join(self.capacity) + "]"

b = Batary()
print(b)  # []

b.charge()
print(b)  # [)]

b.charge()
print(b)  # [))]

b.discharge()
print(b)  # [)]

b.discharge()
print(b)  # []

b.discharge()