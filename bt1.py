raw_logs = []
processed_logs = []


def clean_log_data(log_input):
    """
    Làm sạch chuỗi log thô bằng cách loại bỏ ký tự đặc biệt
    và tách thành danh sách log.
    """
    translation_table = str.maketrans("", "", "!@#$")
    cleaned_text = log_input.translate(translation_table)
    return [log.strip() for log in cleaned_text.split(";") if log.strip()]


def load_logs():
    """
    Nhập dữ liệu log từ người dùng và lưu vào raw_logs.
    """
    global raw_logs

    print("--- NẠP DỮ LIỆU LOG ---")
    log_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    raw_logs = clean_log_data(log_input)

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_danger_logs():
    """
    Lọc các log chứa ERROR hoặc CRITICAL bằng List Comprehension.
    """
    global processed_logs

    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return
    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]
    print("--- LỌC CẢNH BÁO ---")
    if processed_logs:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")
    else:
        print("Không tìm thấy cảnh báo nguy hiểm.")
def mask_ip_logs():
    """
    Mã hóa hai dải số cuối của địa chỉ IP trong các log nguy hiểm.
    """
    if not raw_logs:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return

    if not processed_logs:
        print("Không có log nguy hiểm để mã hóa.")
        return

    masked_logs = []

    for log in processed_logs:
        words = log.split()

        for i, word in enumerate(words):
            if "." in word:
                ip_parts = word.split(".")

                if len(ip_parts) == 4:
                    words[i] = ".".join(ip_parts[:2] + ["*", "*"])
                    break

        masked_logs.append(" ".join(words))

    print("--- MÃ HÓA IP ---")
    print("Báo cáo log an toàn:")

    for index, log in enumerate(masked_logs, start=1):
        print(f"{index}. {log}")
    return masked_logs
def display_menu():
    """
    Hiển thị menu chức năng và điều khiển chương trình.
    """
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                load_logs()
            case "2":
                filter_danger_logs()
            case "3":
                mask_ip_logs()
            case "4":
                print("Đóng hệ thống. Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ.")