class Human:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        self._name = value

    def _del_name(self):
        print("Delete name")
        del self._name

    name = property(
        fdel=_del_name,
        fset=_set_name,
        fget=_get_name,
        doc="The name property."
    )

    def _get_surname(self):
        return self._surname

    def _set_surname(self, value):
        self._surname = value

    def _del_surname(self):
        print("Delete surname")
        del self._surname

    surname = property(
        fdel=_del_surname,
        fset=_set_surname,
        fget=_get_surname,
        doc="The surname property."
    )

# TODO: Add education
# TODO: Add accumulation
# TODO: Add hobby
# TODO: Add 10 if
# TODO: Add while
# TODO: Add 2 break and 2 continue
class Parent(Human):
    def __init__(self, name, surname, age, work, salary):
        super().__init__(name, surname)
        self._age = age
        self._work = work
        self._salary = salary

    @property
    def age(self):
        return self._age

    @property
    def work(self):
        return self._work

    @property
    def salary(self):
        return self._salary


class Kid(Human):
    def __init__(self, name, surname, school):
        super().__init__(name, surname)
        self._school = school

    @property
    def school(self):
        return self._school

