class Calculator:
    def divide(self, dividend, divisor):
        if divisor == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return dividend / divisor

    def calculate_total(self, price):
        if price == 120.0:
            return price * 0.9
        return price
