# Validation methods
test_str = "Hello123"
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")

# เขียนโปรแกรม ตรวจสอบความแข็งแรงของ password
# password ที่แข็งแรง ยาวมากกว่า 8 ตัว และผสมกันระหว่างตัวเลข ตัวอักษร และอักขระพิเศษ

# ตัวอย่างหน้าจอ
# Insert your password: Test123
# Your password is not strong!

# Insert your password: Test1234;
# Your password is strong 

password = input ("Insert your password:")
lenght = len(password)
check = password.isalnum()

if lenght > 8 and check == False:
    print("Your password is strong!")
else :
    print("Your password is not strong!")
