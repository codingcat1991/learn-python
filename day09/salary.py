from abc import abstractmethod, ABCMeta


class Employee(object, metaclass=ABCMeta):
    __slots__ = '_name'

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):
    __slots__ = '_name'

    def __init__(self, name):
        super().__init__(name)

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    __slots__ = ('_name', '_working_hours')

    def __init__(self, name, working_hours=0):
        super().__init__(name)
        self._working_hours = working_hours

    @property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, working_hours):
        self._working_hours = working_hours if working_hours > 0 else 0

    def get_salary(self):
        return self._working_hours * 150.0


class Salesman(Employee):
    __slots__ = ('_name', '_sales')

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hours = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('请输入%s本月销售额：' % emp.name))
        print('%s本月工资为: ￥%s元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
