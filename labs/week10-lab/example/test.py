print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = 'Hello World'
for letter in text:
    if letter == 'l':
        count += 1
print(f"{count} letters 'l' found in '{text}'")


# เขียนโปรแรกม นับจำนวนอักขระที่สนใจในข้อความที่กำหนดโดยผู้ใช้
# 1.รับข้อความที่กำหนดให้จากผู้ใช้ (text)
# 2.รับอักขระที่สนใจจากผู้ใช้ (char)
# 3.แสดงผลการนับอักขระที่สนใจในข้อความออกทางหน้า

# ตัวอย่างหน้าจอ
# Insert the text: Kasetsart Sriracha
# Character to find: r
# 3 letter 'r' found in 'Kasetsart Sriracha'


print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input ("Insert the text:")
char = input ("Character to find:")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'")