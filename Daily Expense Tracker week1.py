import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# ฟังก์ชันสำหรับสร้างไฟล์ถ้ายังไม่มี
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Type_Money", "Category", "Amount", "Note"])

# ฟังก์ชันเพิ่มรายรับ/รายจ่าย
def add_expense():
    Type_Money = input("ประเภท รายรับ=(IN)/ รายจ่าย=(EX): ").strip().lower()
    if Type_Money == "in":
        Type_Money = "รายรับ"
    elif Type_Money == "ex":
        Type_Money = "รายจ่าย"
    else:
        print("กรุณาใส่ประเภทให้ถูกต้อง!")
        return     

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("หมวดหมู่ (อาหาร/เดินทาง/บันเทิง/อื่นๆ): ")

    try:
        amount = float(input("จำนวนเงิน: "))
    except ValueError:
        print("กรุณาใส่จำนวนเงินเป็นตัวเลข!")
        return

    note = input("บันทึกเพิ่มเติม: ")

    with open(FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, Type_Money, category, amount, note])
    print("บันทึกเรียบร้อย!\n")

# ฟังก์ชันแสดงรายการทั้งหมด
def show_expenses():
    if not os.path.exists(FILENAME):
        print("ยังไม่มีข้อมูล\n")
        return
    with open(FILENAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # ข้าม header
        print("\n--- รายการ ---")
        for i, row in enumerate(reader, start=1):
            date, Type_Money, category, amount, note = row
            print(f"{i}. {date} | {Type_Money} | {category} {amount} บาท | Note: {note}")
    print()

def main():
    init_file()
    while True:
        print("===== Daily Expense Tracker (Sprint 1) =====")
        print("1. เพิ่มรายการ")
        print("2. แสดงรายการ")
        print("3. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1/2/3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            print("ปิดโปรแกรมแล้ว")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง!\n")

if __name__ == "__main__":
    main()
