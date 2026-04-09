class RList:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def addHead(self, data):
        self.next = RList(self.data, self.next)
        self.data = data

    def addBefore(self, target_value, new_data):
        if self.data == target_value:
            self.addHead(new_data)
            return True

        current = self
        while current.next is not None:
            if current.next.data == target_value:
                current.next = RList(new_data, current.next)
                return True
            current = current.next
        return False

    def removeFirst(self, target_value):
        if self.data == target_value:
            if self.next is not None:
                self.data = self.next.data
                self.next = self.next.next
            else:
                self.data = None
            return True

        current = self
        while current.next is not None:
            if current.next.data == target_value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def removeEvenPositions(self):
        current = self
        while current is not None and current.next is not None:
            current.next = current.next.next
            current = current.next

    def printOddValues(self):
        current = self
        result = []
        while current is not None:
            if current.data is not None and current.data % 2 != 0:
                result.append(str(current.data))
            current = current.next
        print("Непарні значення:", ", ".join(result) if result else "Немає")

    def contains(self, target_value):
        current = self
        while current is not None:
            if current.data == target_value:
                return True
            current = current.next
        return False

    @property
    def Second(self):
        if self.next is not None:
            return self.next.data
        return None

    @Second.setter
    def Second(self, value):
        if self.next is not None:
            self.next.data = value
        else:
            self.next = RList(value)

    def __str__(self):
        if self.data is None:
            return "Empty"
        if self.next is None:
            return str(self.data)
        return str(self.data) + ', ' + str(self.next)


if __name__ == "__main__":
    r = RList(10)
    r.addHead(5)
    r.addHead(3)
    r.addHead(7)

    print("Початковий список:", r)

    print("Другий елемент (Second):", r.Second)
    r.Second = 99
    print("Список після зміни Second:", r)

    r.addBefore(10, 8)
    print("Після додавання 8 перед 10:", r)

    r.printOddValues()

    print("Чи є в списку 99?:", r.contains(99))
    print("Чи є в списку 100?:", r.contains(100))

    r.removeFirst(99)
    print("Після видалення 99:", r)

    r.removeEvenPositions()
    print("Після видалення парних позицій:", r)