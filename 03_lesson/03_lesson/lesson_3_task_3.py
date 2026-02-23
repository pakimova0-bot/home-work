from Mailing import Mailing
from Address import Address

to_address = Address(124498, "Зеленоград", "Центральный проспект", "445", "252")
from_address = Address(124498, "Зеленоград", "Центральный проспект", "445", "25")

mailing = Mailing(to_address, from_address, 810, 124498)

print(mailing)