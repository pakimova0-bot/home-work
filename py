def test_sum_positive_nims():
    calculator = Calculator()
    res = calculator.sum(4, 5)
    assert res == 9

    def test_sum_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, -10) #поменяли параметры
    assert res == -16 #поменяли ожидаемую сумму

    def test_sum_positive_and_negative_nums(): #поменяли название теста
    calculator = Calculator()
    res = calculator.sum(-6, 6) #поменяли параметры
    assert res == 0 #поменяли ожидаемую сумму
    