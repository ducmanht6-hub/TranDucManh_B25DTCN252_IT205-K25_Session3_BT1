print (" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG --- ")

# Vòng Lặp chạy 3 lần dể nhập Lương cho 3 nhân viên
for employee_number in range(1, 4):

    # Khởi tạo chiếc hộp dựng tổng tiên
    total_budget = 0

    print ("Đang xử lý nhân viên số", employee_number)
    # Nhập mức Lương
    salary = int(input(" Nhập mức Lương (VNĐ): "))

    # Thực hiện thao tác cộng dồn tiền vào chiếc hộp
    total_budget = total_budget + salary

# Sau khi nhập xong cả 3 người, in tổng tiền ra màn hình
print ("= KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẤN BỊ LÀ:", total_budget, "VNĐ")

""" Code cơ bản không sai nhưng logic có 1 vấn đề khiến code chạy lỗi
total_budget = 0 đang nằm bên trong vòng lặp, nên mỗi lần lặp nó lại reset về 0.
Phần nhập lương và cộng dồn cũng cần nằm trong for.
Cách giải quyết: Dòng in kết quả cuối cùng nên đặt sau khi vòng lặp kết thúc. """