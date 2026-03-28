a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# a) Tổng và tích
tong = a + b + c
tich = a * b * c
print("Tổng =", tong)
print("Tích =", tich)

# b) Hiệu của 2 số bất kỳ (ví dụ a - b)
print("Hiệu a - b =", a - b)
print("Hiệu b - c =", b - c)
print("Hiệu a - c =", a - c)

# c) Phép chia
# Ví dụ chia a cho b
if b != 0:
    print("a // b =", a // b)   # chia lấy phần nguyên
    print("a % b =", a % b)     # phần dư
    print("a / b =", a / b)     # chia chính xác
else:
    print("Không thể chia cho 0")