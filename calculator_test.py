from calculator import Calculator 
calculator = Calculator()
calculator

res = calculator.sum(4, 5)
assert res == 9

res = calculator.sum(-6, -10)
assert res == -16

res = calculator.sum(-6, 6)
assert res == 0

res = calculator.sum(5.6, 4.3)
assert res == 9.9

res = calculator.sum(5.6, 4.3)
print(res)
assert res == 9.9
 
res = calculator.sum(5.6, 4.3) #Python посчитает сумму
res = round(res, 1) #округлит ее до одного знака после запятой
print(res) #напечатает сумму
assert res == 9.9 #сравнит с предполагаемым значением

res = calculator.sum(10, 0)
assert res == 10

res = calculator.div(10, 2)
assert res == 5

res = calculator.div(10, 0)
assert res == None

numbers = []
res = calculator.avg(numbers)
assert res == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = calculator.avg(numbers)
print(res)
assert res == 5

