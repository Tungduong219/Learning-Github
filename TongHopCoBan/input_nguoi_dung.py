#1. Hàm input
name = input("Nhập tên của bạn: ")
print(f"Chào {name}")

#2. Hàm input luôn trả về giá trị strinfg
print(type(name))

#3. Chuyển kiểu dữ liệu
# Cách 1:
age = input("Nhập tuổi của bạn: ")
age = int(age)

# Cách 2:
age = int(input("Nhập tuổi của bạn: "))
print(age)

#4. Xử lý lỗi khi nhập giữ liệu
try:
    age = int(input("Nhập tuổi của bạn: "))
    print(f"Tuổi của bạn là: {age}")
except ValueError:
    print("Bạn phải nhập vào kiểu so nguyên")

# Check that the string is not empty
name = input("Enter your name: ").strip()
if not name:
    print("Name must not be empty!")
else:
    print(f"Hello, {name}!")

# Check that the number is in a valid range
score = float(input("Enter a score (0-10): "))
if 0 <= score <= 10:
    print(f"Valid score: {score}")
else:
    print("Score must be between 0 and 10!")