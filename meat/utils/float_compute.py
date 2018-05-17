from decimal import Decimal, getcontext

class Compute:
    """float + - * / 运算"""
    @staticmethod
    def add(*args, prec=2):
        getcontext().prec = prec
        result = Decimal('0')
        for arg in args:
            result += Decimal(str(arg))
        return result

    @staticmethod
    def subtract(num, *args, prec=2):
        getcontext().prec = prec
        result = Decimal(str(num))
        for arg in args:
            result -= Decimal(str(arg))
        return result

    @staticmethod
    def multiply(*args, prec=2):
        getcontext().prec = prec
        result = Decimal('1')
        for arg in args:
            result *= Decimal(str(arg))
        return result

    @staticmethod
    def divide(num, *args, prec=2):
        getcontext().prec = prec
        result = Decimal(str(num))
        for arg in args:
            if arg == 0:
                raise Exception("除数为0,错误")
            result = result / Decimal(str(arg))
        return result
