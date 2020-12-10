def read_address():
    address = []
    with open(r"addressBook.txt", encoding="UTF-8") as file:
        for i in file:
            information = i.rstrip("\n")
            information = information.split(",")
            address.append(information)
    return address


def write_address(address):
    with open(r"addressBook.txt", encoding="UTF-8", mode="w") as file:
        current = 0
        for x in address:
            if current == 0:
                file.write(f"{x[0]},{x[1]},{x[2]}")
            else:
                file.write(f"\n{x[0]},{x[1]},{x[2]}")
            current = current + 1


def input_address():
    new_name = input("追加したい名前は?>>")
    new_number = input("追加したい電話番号?>>")
    new_mail = input("追加したいメール?>>")
    new_address = [new_name, new_number, new_mail]
    return new_address


address = read_address()
new_address = input_address()
address.append(new_address)
write_address(address)
