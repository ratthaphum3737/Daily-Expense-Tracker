import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"


def init_file(): # ฟังก์ชันสำหรับสร้างไฟล์ถ้ายังไม่มี
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Type_Money", "Category", "Amount", "Note"])

# ฟังก์ชันเพิ่มรายจ่าย
def add_expense():
    try:
        Type_Money = input("ประเภท รายรับ=(IN)/ รายจ่าย=(EX): ").strip().lower()
        if Type_Money =="in":
            Type_Money="รายรับ"
        elif Type_Money =="ex":
            Type_Money="รายจ่าย"
        else:
            print("กรุณาใส่ประเภทให้ถูกต้อง!")
            return     
    except ValueError:
        print("กรุณาใส่จำนวนเงินเป็นตัวเลข!")
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
        writer.writerow([date,Type_Money, category, amount, note])
    print("เพิ่มรายจ่ายเรียบร้อย!\n")

# ฟังก์ชันแสดงรายการรายจ่ายทั้งหมด
def show_expenses():
    if not os.path.exists(FILENAME):
        print("ยังไม่มีข้อมูลรายจ่าย\n")
        return
    expenses=[]
    total = 0
    Number=0
    with open(FILENAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # ข้าม header
        print("\n--- รายการรายจ่าย ---")
        for row in reader:
            Number += 1
            date,Type_Money, category, amount, note = row
            print(f"{Number}. {date} | {Type_Money} | {category}  {amount} บาท Note {note}")
            total += float(amount)
            expenses.append(row)
    return expenses

def Cal_Total():
    if not os.path.exists(FILENAME):
        print("ยังไม่มีข้อมูลรายจ่าย\n")
        return
    total = 0
    with open(FILENAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            date,Type_Money, category, amount, note = row
            if Type_Money=="รายรับ":
                total += float(amount)
            elif Type_Money=="รายจ่าย":
                total -= float(amount)

    return total 

# ฟังก์ชันลบรายการ
def delete_expense():
    try:
        expenses = show_expenses()
        #print(expenses)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดขณะอ่านไฟล์: {e}\n")
        return
    while True:
        s = input("เลือกลำดับที่ต้องการลบ (หรือพิมพ์ 'cancel OR C' เพื่อยกเลิก): ").strip().lower()
        if s.lower() == 'cancel' or s.lower() =='c': 
            print("ยกเลิกแล้ว\n")
            return
        try:
            index = int(s) - 1
        except ValueError:
            print("กรุณาใส่ตัวเลขที่ถูกต้อง หรือพิมพ์ 'c' ยกเลิก\n")
            continue

        if index < 0 or index >= len(expenses):
            print("เลขที่คุณเลือกไม่ถูกต้อง ลองอีกครั้ง\n")
            continue
        break

    deleted = expenses.pop(index)
    
    try:
        temp_name = FILENAME + ".tmp"
        with open(temp_name, mode="w", newline="", encoding="utf-8") as tmp:
            writer = csv.writer(tmp)
            writer.writerow(["Date","Type_Money", "Category", "Amount", "Note"])
            writer.writerows(expenses)
        os.replace(temp_name, FILENAME)
    except Exception as e:
        print(f"ไม่สามารถเขียนไฟล์ได้: {e}\n")
        return

    print(f"ลบรายการเรียบร้อย: {deleted[0]} | {deleted[1]} | {deleted[2]} บาท | {deleted[3]} | {deleted[4]}")



def main():
    init_file()
    while True:
        print("===== Daily Expense Tracker =====")
        print("1. เพิ่มรายจ่าย")
        print("2. แสดงรายการรายจ่าย")
        print("3. ลบรายการ")
        print("4. ออกจากโปรแกรม")
        choice = input("เลือกเมนู (1/2/3/4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
            print(f"\n{"="*20}\n  ยอดรวม    {Cal_Total()}\n{"="*20}\n")
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("ปิดโปรแกรมแล้ว")
            break
        else:
            print("กรุณาเลือกเมนูให้ถูกต้อง!\n")

if __name__ == "__main__":
    main()
