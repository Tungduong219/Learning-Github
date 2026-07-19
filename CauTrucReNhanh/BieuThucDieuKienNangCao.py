#1. Chained Comparison — So sánh chuỗi
score = 8
#Có thể viết:
if score >= 8 and score < 10:
    print("Bạn thật giỏi")

#hoặc
if 5 <= score < 7:
    print("Average")

x = 5
if 1 < x < 10:
    print(f"{x} is in the range (1, 10)")

if 1 <= x <= 5 <= 10:
    print("Chaining multiple comparisons")



#2. Biểu thức điều kiện 1 dòng
age = 20
#Có thể viết biểu thứ 4 dòng
# The usual way (4 lines)
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

#hoặc viết 1 dòng
status = "Adult" if age >=18 else "Minor"
print(status)

# Đối với print
print(f"Kết quả: {'Pass' if score>5 else 'Fail'}")


#3. Toán từ in kiểm tra thành viên
fruits = ["apple","orange","mango","grape"]
if "apple" in fruits:
    print("Có apple")

email = "dotungduong2194@gmail.com"
if "@" in email:
    print("Có tồn tại Email")

if "durian" not in fruits:
    print("Không có durian")

#Ứng dụng thay thế = elif
color = "red"

# Instead of writing many elifs:
# if color == "red" or color == "orange" or color == "yellow":

if color in ["red", "orange", "yellow"]:
    print("Warm color")
elif color in ["blue", "green", "purple"]:
    print("Cool color")
else:
    print("Other color")

weight = 115   # kg
height = 1.80   # m

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.1f} → {category}")



#Ứng dụng kiểm tra đăng nhập
username = "admin"
password = "xomdata123"

if not username or not password:
    print("Please fill in all fields")
elif username == "admin" and password == "xomdata123":
    print("Login successful!")
else:
    print("Wrong username or password")

