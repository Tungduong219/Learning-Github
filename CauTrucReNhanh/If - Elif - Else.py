#1. Cấu trúc rẽ nhánh cơ bản
from time import process_time_ns

score = 8
if score >= 5:
    print("Chúc mừng!")
    print("Bạn đã qua môn")
#Các khối thuộc câu lệnh if sẽ thụt vào 4 spaces. Không thụt sẽ nằm ngoài khối

#2. Cấu trúc hai nhánh if - else
age = 16
if age <= 18:
    print("Bạn không đủ tuổi bầu cử")
else:
    print("Chúc mừng")
    print("Bạn đã đủ tuổi tham gia bầu cử")

#3. Cấu trúc nhiều nhánh if - elif - else
diem = 5
if diem >= 9:
    print("Chúc mừng bạn được học sinh giỏi")
elif 7 <= diem < 9 :
    print("Bạn đã đạt học sinh khá")
elif 5 <= diem < 7 :
    print("Bạn đạt học sinh trung bình")
else:
    print("Thật tiếc!")
    print("Bạn ở mức học sinh yếu")


#4. Nhiều điều kiện kết hợp: Sử dụng and, or, not
age = 25
has_license = True
years_experience = 2

if age >= 18 and has_license and years_experience >= 1:
    print("Eligible to drive")
else:
    print("Not eligible yet")