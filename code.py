import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from tabulate import tabulate


def number_check(phone_number):
    number = phonenumbers.parse(phone_number)
    description = geocoder.description_for_number(number, "en")
    supplier = carrier.name_for_number(number, "en")
    info = [["Country", "Supplier"], [description, supplier]]
    return tabulate(info, headers="firstrow", tablefmt="github")


if __name__ == "__main__":
    number = input("Enter number: ")
    print(number_check(number))
