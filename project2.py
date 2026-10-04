name = input("name: ")


java = float(input("java: "))
python = float(input("python: "))
html = float(input("HTML: "))

grades = [java, python, html]

avg = sum(grades) / len(grades)

print("name:", name)
print("avg:", avg)
