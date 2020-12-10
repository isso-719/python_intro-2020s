from dataclasses import *
@dataclass
class Grade:
    name: str
    math: int
    physics: int
    english: int


def oneMost(subject):
    oneMostPerson = []
    if subject == "math":
        most = 0
        for i in people:

            if i.math > most:
                most = i.math

        for i in people:

            if i.math == most:
                oneMostPerson.append(i.name)

    elif subject == "physics":
        most = 0
        for i in people:

            if i.physics > most:
                most = i.physics

        for i in people:

            if i.physics == most:
                oneMostPerson.append(i.name)

    elif subject == "english":
        most = 0
        for i in people:

            if i.english > most:
                most = i.english

        for i in people:

            if i.english == most:
                oneMostPerson.append(i.name)

    return oneMostPerson


def allMost():
    most = 0
    allMostPerson = []
    for i in people:
        total = i.math + i.physics + i.english

        if total > most:
            most = total

    for i in people:

        if most == i.math + i.physics + i.english:
            allMostPerson.append(i.name)

    return allMostPerson


people = [Grade("Alice", 100, 65, 57),
          Grade("Bob", 45, 98, 100),
          Grade("Charley", 50, 50, 50),
          Grade("Aimi", 100, 100, 100),
          Grade("Ex", 100, 100, 100)]


mathCount = 0
physicsCount = 0
englishCount = 0
allCount = 0

for i in oneMost("math"):
    if mathCount == 0:
        mathMost = i
    else:
        mathMost = mathMost + "," + i
    mathCount = mathCount + 1

for i in oneMost("physics"):
    if physicsCount == 0:
        physicsMost = i
    else:
        physicsMost = physicsMost + "," + i
    physicsCount = physicsCount + 1

for i in oneMost("english"):
    if englishCount == 0:
        englishMost = i
    else:
        englishMost = englishMost + "," + i
    englishCount = englishCount + 1

for i in allMost():
    if allCount == 0:
        allMost = i
    else:
        allMost = allMost + "," + i
    allCount = allCount + 1


print("数学で最も高いのは")
print(mathMost)

print("物理で最も高いのは")
print(physicsMost)

print("英語で最も高いのは")
print(englishMost)

print("合計点数が最も高いのは")
print(allMost)
