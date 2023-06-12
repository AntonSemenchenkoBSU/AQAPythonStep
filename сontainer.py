# Parents or Kids
class MyContainer:
    def __init__(self):
        self.items = ["Mother", "Father"]

    def __contains__(self, item):
        return item in self.items

def main(first, second):
    family = MyContainer()

    print("Father" in family)  # True
    print("Mother" in family)  # True
    print("Lover" in family)   # False

    if (("Father" in family) and ("Mother" in family)):
        print("Happy childhood!")

    simple_container = [1, 2, 3]
    if (first in simple_container):
        print(first)
        print("This element placed in container")
    if not(second in simple_container):
        print(second)
        print("This element isn't placed in container")

    # Список — изменяемая последовательность с упорядоченными элементами.
    first_empty_list = list()
    second_empty_list = []
    first_list = [1, 'some', 3.5, list()]
    second_list = list(idx for idx in range(3))  # [0, 1, 2]
    #second_list = list(range(3))  # [0, 1, 2]
    print(first_empty_list)
    print(second_empty_list)
    print(first_list)
    print(second_list)
    first_list[0] = 25
    first_list[1] = 125
    first_list[3] = 225
    print(first_list)
    #first_list[4] = 325 #IndexError

    my_list = [1, 2, 3, 4, 5]
    print(my_list)
    del my_list[2]      # [2, 3, 4, 5]
    print(my_list)
    del my_list[:2]     # [4, 5]
    print(my_list)
    del my_list[:]      # []
    print(my_list)
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)

    #for i in range(1000000000):
    #    my_list.append(i)

    #strange_list = list(idx for idx in range(1000000000))

    #strange_list = []
    #for i in range(1000000000):
    #    strange_list.append(i)


    print(my_list)

    a = [3, 2, 1]
    b = [1, 2, 3]
    d = [3, 2, 2]
    e = [3, 2]
    f = [3, 2, 'a']
    a > b  # True
    a > d  # False
    d > b  # True
    a > e  # True
    #a > f  # False # TypeError: '>' not supported between instances of 'int' and 'str'

    some_list = [1, 3, 8, 7]
    print(some_list[-3])
    print(some_list[-4])
    #print(some_list[-5]) # Out of range

    #item[START:STOP:STEP]
    print(some_list[4::-1])

    #another_list = list(range(2, 10, 2))
    another_list = list(range(2, -10, -2))
    print(another_list)

    #sequence.index(val[, start[, finish]]) -> int
    value_index = another_list.index(-6, 0, len(another_list));
    #value_index = another_list.index(-6);
    print(value_index)

    #Кортеж — неизменяемая последовательность с упорядоченными элементами.
    first_tuple = tuple()             # ()
    second_tuple = tuple('abc')       # ('a', 'b', 'c')
    third_tuple = tuple([1, 2, 3])    # (1, 2, 3)
    list_tuple = tuple(another_list)
    range_tuple = tuple(range(5))
    print(first_tuple)
    print(second_tuple)
    print(third_tuple)
    print(list_tuple)
    print(range_tuple)

    print(second_tuple[1])
    #second_tuple[1] = 'd'

    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict)
    print(my_dict.items())          # dict_items([('a', 1), ('b', 2), ('c', 3)])
    #print(my_dict.items()[1])      # 'dict_items' object does not support indexing
    print(list(my_dict.items())[1]) # ('a', 1)
    # TODO: read and applay https://pythonz.net/references/named/dict/

main(2, "some text")

# Нотация О большое и сложность операций
# https://pythonz.net/references/named/slozhnost-operatsii-so-spiskami/


