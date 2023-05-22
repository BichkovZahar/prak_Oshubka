class ValueError(Exception):
    def __init__(self , temperatura):
        self.temperatura = temperatura
class TemperatureConverte:
    def celsius_to_fahrenheit(self , celsius):
        if celsius < -273:
            raise ValueError(celsius)
        return celsius * 9/5 + 32
    def fahrenheit_to_celsius(self ,fahrenheit):
        if fahrenheit < -460:
            raise ValueError(fahrenheit)
        return (fahrenheit - 32) * 9/5
rezult = TemperatureConverte()
try:
    temperature_1 = rezult.celsius_to_fahrenheit(55)
    print(f"Температура -> {temperature_1} в фарангейтах")
except ValueError as b:
    print(f"{b.temperatura} слишком низька температура")
try:
    temperature_2 = rezult.fahrenheit_to_celsius(30)
    print(f"Температура -> {temperature_2} в цельціях")
except ValueError as a :
    print(f"{a.temperatura} слишком низька температура")