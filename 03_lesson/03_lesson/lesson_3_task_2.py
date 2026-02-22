from smartphone import Smartphone

catalig = [
smartphone, ("iPhone", "13Pro", "+71234567"),
smartphone("honor", "13Pro", "+71234567"),
smartphone("Fly", "13Pro", "+71234567"),
smartphone("Redme", "13Pro", "+71234567"),
smartphone("Samsung", "13Pro", "+71234567")
]

for phone in catalig:
    print(f"{phone.marka} - {phone.model}. {phone.number}")
