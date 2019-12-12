# coding=utf-8
# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
si = nth_power(4)
a = int(input('请输入需要计算的平方：'))
b = int(input('请输入需要计算的立方：'))
c = int(input('请输入需要计算的四次方：'))
print('%s平方是：' % a, square(a))
print('%s平方是：' % b, cube(b))
print('%s平方是：' % c, si(c))

