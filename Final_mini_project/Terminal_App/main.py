import operations     
import file_handler   


def main():
    file_handler.init_file() 

    while True:
        print("===== Daily Expense Tracker =====")
        print("1. เพิ่มรายการ")
        print("2. แสดงรายการทั้งหมด")
        print("3. ลบรายการ")
        print("4. ออกจากโปรแกรม")
        
        choice = input("เลือกเมนู (1/2/3/4): ")

        if choice == "1":
            operations.add_expense()
        elif choice == "2":
            operations.show_expenses()
            print("-" * 25)
        elif choice == "3":
            operations.delete_expense()
        elif choice == "4":
            print("ปิดโปรแกรมแล้ว")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง!\n")

if __name__ == "__main__":
    main()