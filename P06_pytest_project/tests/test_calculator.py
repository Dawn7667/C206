from calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 9876
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 100
        b = 50
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5000
        assert result == expected

    def test_divide(self):
        # arrange
        a = 100
        b = 50
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 2
        assert result == expected
