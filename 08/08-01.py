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
    person("hogeko", None)
]

print(addressBook)


# 二番
search = input("名前>>")
triger = False

for person in addressBook:
    if search == person.name:
        print(f"{person.name}: {person.number}")
        triger = True

if triger == False:
    print("該当なし")
