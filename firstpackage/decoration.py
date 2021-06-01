import time


def my_check(fn):
    def inner():
        print("请先登录")
        fn()

    return inner


# 语法糖写法
def check(fn):
    def inner():
        print("请先登录")
        fn()

    return inner


# 在方法前面添加@check等价于check(comment)


def get_time(fn):
    start_time = time.time()
    fn()
    end_time = time.time()
    run_time = end_time - start_time
    print(f"函数运行时间={run_time}")
    return get_time
