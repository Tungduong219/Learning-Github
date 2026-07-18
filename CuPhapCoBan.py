#Thụt dòng-----------------------------------------------------------------------------
score = 4

# Case 1: both lines belong to the if block
if score >= 5:
    print("You passed!")
    print("Congratulations!")   # Only printed when score >= 5

# Case 2: the second line is OUTSIDE the if block
if score >= 5:
    print("You passed!")
    print("Congratulations!")


#Dấu : là bắt buộc trước mỗi câu lệnh----------------------------------------------------------
if True:
    print("OK")

for i in range(3):
    print(i)


#Quy tắc đặt tên biến--------------------------------------------------------------
#Có thể đặt theo Pascal, Camel và snack_case nhưng snack_case thường được dùng nhiều hơn
my_score = 8,5
my_name = "Đỗ Tùng Dương"
CHECK_VAR = "Penalty"
PI = 3.14

#Phân biệt chữ hoa và chữ thường
a = 1
A = 4
print(a+A)


#Xuống dòng trong 1 biểu thức dài-----------------------------------------
#Khi 1 biểu thức quá dài có thể xuống dòng bằng dấu \ hoặc dùng () để xuống dòng
min = 100+200+\
    300+400
print(min)
#Hoăc
max = (100+200+300+400+
       500)
print(max)

