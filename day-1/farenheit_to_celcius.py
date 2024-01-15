def convert_to_celcius(farenheit):
    celcius = (farenheit-32) * 5/9
    return celcius

if __name__ == "__main__":
    farenheit = float(input("Enter temperature in Farenheit: "))
    print("Temperature in Celcius is:", convert_to_celcius(farenheit))