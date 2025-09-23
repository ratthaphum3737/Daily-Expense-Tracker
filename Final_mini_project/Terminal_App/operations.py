from datetime import datetime
import file_handler 

#ฟังก์ชันเพิ่มรายจ่าย
def add_expense():
    try:
        type_money_input = input("ประเภท รายรับ=(IN)/ รายจ่าย=(EX): ").strip().lower()
        if type_money_input == "in":
            type_money = "รายรับ"
        elif type_money_input == "ex":
            type_money = "รายจ่าย"
        else:
            print("กรุณาใส่ประเภทให้ถูกต้อง!")
            return
            
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        category = input("หมวดหมู่ (อาหาร/เดินทาง/บันเทิง/อื่นๆ): ")
        amount = float(input("จำนวนเงิน: "))
        note = input("บันทึกเพิ่มเติม: ")

        new_record = [date, type_money, category, amount, note]
        file_handler.append_data(new_record) # เรียกใช้ฟังก์ชันเขียนต่อท้ายไฟล์
        
        print("เพิ่มรายการเรียบร้อย!\n")
    except ValueError:
        print("กรุณาใส่จำนวนเงินเป็นตัวเลข!\n")
        return

#ฟังก์ชันแสดงรายการรายจ่ายทั้งหมด
def show_expenses():
    expenses = file_handler.read_data()
    if not expenses:
        print("ยังไม่มีข้อมูลรายจ่าย\n")
        return None

    print("\n--- รายการทั้งหมด ---")
    for i, row in enumerate(expenses, 1):
        date, type_money, category, amount, note = row
        print(f"{i}. {date} | {type_money} | {category} | {amount} บาท | Note: {note}")
    print(f"\nยอดเงินคงเหลือ: {cal_total()} บาท")
    return expenses

#ฟังก์ชันลบรายการ
def delete_expense():

    expenses = show_expenses()
    if not expenses:
        return

    try:
        choice_str = input("เลือกลำดับที่ต้องการลบ (หรือพิมพ์ 'c' เพื่อยกเลิก): ").strip().lower()
        if choice_str == 'c':
            print("ยกเลิกการลบ\n")
            return

        index_to_delete = int(choice_str) - 1
        if 0 <= index_to_delete < len(expenses):
            deleted_item = expenses.pop(index_to_delete)
            file_handler.write_data(expenses) # เรียกใช้ฟังก์ชันเขียนข้อมูลทับทั้งหมด
            print(f"ลบรายการ '{deleted_item[2]}' จำนวน {deleted_item[3]} บาท เรียบร้อยแล้ว\n")
        else:
            print("ลำดับที่เลือกไม่ถูกต้อง\n")
    except ValueError:
        print("กรุณาใส่เป็นตัวเลขลำดับที่ หรือ 'c' เพื่อยกเลิก\n")

def cal_total():
    """ฟังก์ชันคำนวณยอดรวม"""
    expenses = file_handler.read_data() # เรียกใช้ฟังก์ชันอ่านข้อมูล
    total = 0
    for row in expenses:
        type_money = row[1]
        amount = float(row[3])
        if type_money == "รายรับ":
            total += amount
        elif type_money == "รายจ่าย":
            total -= amount
    return total