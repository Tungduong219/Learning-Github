#1. Vòng lặp while
from operator import truediv

counter = 1
while counter <= 5:
    print(f"Round:{counter}")
    counter += 1
print("done")

#2. While và For: Khi nào dùng gì?
for i in range(10):
    print(i)

numbers = 5000
while numbers > 1:
    numbers  = numbers // 2
    print(numbers,end="  ")
print()

#3. Break - thoát vòng lặp ngay lập tức
numbers = [3,6,5,4,9,2]
for number in numbers:
    if number % 2 == 0:
        print(number)
        break


#4. Continue - Bỏ qua lần lặp hiện tại và chạy luôn lần lặp tiếp theo
# Print odd numbers from 1 to 10 (skip evens)
for i in range(1, 11):
    if i % 2 == 0:
        continue   # Skip even numbers, jump back to the top of the loop
    print(i, end=" ")   # 1 3 5 7 9

#5. Pass (Không làm gì cả)
for i in range (10):
    if i % 2 == 0:
        pass
    else:
        print(f"{i} is odd")

#6. While + break - Vòng lặp có điều kiện thoát
secret_number = 7
temp = 0
while True:
    temp +=1
    guess = temp *2+1
    if guess == secret_number:
        print(f"You guessed the secret number {temp} times.!")
        break
    if temp>10:
        print("Sorry, you guessed too high.")
        break
