#Gán giá trị cho biến (Sử dụng dấu = để gán giá trị mà không cần phải khai báo)------------------------------
a = 5
b = "Duong so handsome"
ck = "Argentina vs Spanish"

#Quy tắc đặt tên------------------------------------------------------------------------------------------
#Không bắt đầu = số và có _ giữa các chữ
name = "Dương"
full_name = " Đỗ Tùng Dương"
score = 8.5
item_quality = 100

# Kiểu dữ liệu động có thể thay đổi trong quá trình chạy--------------------------
x = 10
print(x,type(x))
x = "Đỗ Tùng Dương"
print(x,type(x))
x = float(10.34)
print(x,type(x))

#Hàm type trả về kiểu dữ liệu----------------------
c = ["danh từ","động","trạng","tính"]
print(type(c))

#hàm len() trả về độ dài của biến---------------------
print(len(c))
print(len(name))

#None là một giá trị đặc biệt nghĩa là không có gì------------------------------
data = None
print(data)
print(type(data))

if data is None:
    print("Không có giá trị được gán cho biến")

#fString nhúng biến vào chuỗi---------------------------------------------
name = "Dương"
full_name = "Đỗ Tùng Dương"
age = 24
avg_score = 7,34333333
print(f"Tôi tên là: {name} - Họ tên đầy đủ là: {full_name} -  Tuổi: {age}")
print(f"Điểm trung bình của tôi: {avg_score:.2f}")
print(f"Birth Year: {2026-age}")


