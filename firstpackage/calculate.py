class Person(object):
    name: str = "我是类name"

    def __init__(self, name: str, age: int):
        # 同名的实例属性会覆盖类属性
        self.name = name
        self.age = age

    def __str__(self):
        """
        这个方法相当于iOS的description
        :return:
        """
        return "这是一个自定义的返回值obj.name=%s objAddrs=%s,super.str=%s" % (self.name, id(self), super.__str__(self))

    def __del__(self):
        print(f"Person已经销毁了{self}")

    def info(self):
        print(f"我是谁{self},name={self.name},age={self.age}")

    @classmethod
    def country(cls):
        print(f"调用了类方法{cls}")


class Student(Person):
    pass


def my_sum(a: int, b: int) -> int:
    return a + b
