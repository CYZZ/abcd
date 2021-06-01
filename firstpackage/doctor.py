

class Father(object):
    def cure(self):
        print("父亲给人治病")


class Son(Father):
    def cure(self):
        print("儿子给人治病")


def call_cure(doc: Father):
    doc.cure()


def mytest():
    print("调用了测试的方法")
    one_person: Father = Father()
    one_person = Son()
