class Queue:
    def __init__(self):
        self.inside = []

    def __str__(self):
        return '=>'.join(self.inside)

    def add(self, name):
        self.inside.append(name)

    def take_out(self):
        if self.inside:
            return self.inside.pop(0)
        else:
            return 'Queue is empty'

    def __iadd__(self, name):
        self.add(name)
        return self

    def __isub__(self, name):
        self.take_out()
        return self

    def __add__(self, name):
        new_queue = Queue()
        new_queue.inside = self.inside.copy()
        new_queue.add(name)
        return new_queue

    def __sub__(self, name):
        new_queue = Queue()
        new_queue.inside = self.inside.copy()
        new_queue.take_out()
        return new_queue


queue = Queue()
queue.add("Alice")
queue.add("Bob")
queue.add("Charlie")
print(queue)

queue.take_out()
print(queue)

queue += "Dave"
print(queue)

queue -= "Bob"
print(queue)

new_queue = queue + "Eve"
print(new_queue)

new_queue = queue - "Charlie"
print(new_queue)
