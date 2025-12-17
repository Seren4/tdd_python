from errors import UnderflowException


class Stack:
    __size = 0
    __elements = list(range(5))

    def is_empty(self) -> bool:
        return self.__size == 0

    def get_size(self) -> int:
        return self.__size

    def push(self, element: int) -> None:
        self.__elements[self.__size] = element
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise UnderflowException
        self.__size -= 1
        return self.__elements[self.__size]

    def peek(self) -> int:
        return self.__elements[self.__size-1]