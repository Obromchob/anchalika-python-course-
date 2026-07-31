#รับข้อมูล "ชื่อจริง (เป็นภาษาอังกฤษ)"จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว

#ตัวอย่างหน้าจอ
#What is you name?: Boonchoo
#You have 4 vowels in your text.

name = input("What is you name?: ")
letters = list(name)
print(letters)

counter = 0

for char in letters:
    if char == 'a' or char == 'A':
        counter = counter + 1

    if char == 'e' or char == 'E':
        counter = counter + 1

    if char == 'i' or char == 'I':
        counter = counter + 1

    if char == 'o' or char == 'O':
        counter = counter + 1

    if char == 'u' or char == 'U':
        counter = counter + 1

print("You have", counter, "vowels in your text.")

# ท่าที่2
a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

vowels = a + e + i + o + u

print("You have", counter, "vowels in your text,")
print(f"You have{vowels} vowels in your text.")