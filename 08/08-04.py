# 一番

from dataclasses import *
@dataclass
class person:
    name: str
    number: str


addressBook = [
    person("Kazuki Isogai", "03-xxxx-xxxx"),
    person("hoge", "03-xxxx-xxxx"),
    person("hogehoge", ""),
    person("hogeko", None),
    person("hogeko", "090-xxxx-xxxx"),
    person("hogeko", "080-xxxx-xxxx"),
    person("hogeko", "070-xxxx-xxxx"),
    person("hogeko", "050-xxxx-xxxx"),
    person("hogeko", "010-xxxx-xxxx"),
    person("hogeko", "020-xxxx-xxxx"),
    person("hogeko", "030-xxxx-xxxx"),
    person("hogeko", "040-xxxx-xxxx")
]

print(addressBook)


def print_person(person):
    print(f"{person.name}: {person.number}")


# 二番
search = input("名前>>")
triger = False

for person in addressBook:
    if search == person.name:
        print_person(person)
        triger = True

if triger == False:
    print("該当なし")
