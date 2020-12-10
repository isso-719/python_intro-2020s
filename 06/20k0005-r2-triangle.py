count = 0
array = []

for x in range(99):
    if 0 < x < 100:

        for y in range(99):
            if x < y < 100:

                for z in range(99):
                    if y < z < 100:

                        if x ** 2 + y ** 2 == z ** 2:
                            count = count + 1
                            array.append([x, y, z])

print("条件を満たすx, y, z の組の個数")
print(count)

print("条件を満たすx, y, z の組のうち、z が最小となるような組")
print(array[0])

print("条件を満たすx, y, z の組のうち、x が最大となるような組")
print(array[count - 1])
