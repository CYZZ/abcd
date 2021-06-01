def func_out(num1):
    def func_inner(num2):
        nonlocal num1  # 告诉编译器，此处使用的是外部变量a
        num1 = 10
        result = num1 + num2
        print(result)
        return result

    # print("preNum1=", num1)
    # func_inner(5)
    # print("later=", num1)
    return func_inner
