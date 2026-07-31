print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
second = int(input("Insert second: "))

#procoss
hours = second // 3600
seconds_remain = second % 3600

minute = seconds_remain // 60
seconds_remain = second % 60

#output
print(f"{second} seconds = {hours} hours, {minute} minute, {seconds_remain} second")