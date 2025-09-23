from datetime import datetime
import file_handler


def add_expense_from_gui(type_money, category, amount, note):
    """ฟังก์ชันเพิ่มรายการที่ถูกเรียกจาก GUI"""
    if not all([type_money, category, amount]):
        return False, "กรุณากรอกข้อมูลประเภท, หมวดหมู่, และจำนวนเงินให้ครบถ้วน"
    try:
        amount_float = float(amount)
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_record = [date, type_money, category, amount_float, note]
        file_handler.append_data(new_record)
        return True, "เพิ่มรายการเรียบร้อย"
    except ValueError:
        return False, "จำนวนเงินต้องเป็นตัวเลขเท่านั้น"

def delete_expense_by_index(index_to_delete):
    """ฟังก์ชันลบรายการตามลำดับ (index) ที่ได้รับจาก GUI"""
    expenses = file_handler.read_data()
    if 0 <= index_to_delete < len(expenses):
        expenses.pop(index_to_delete)
        file_handler.write_data(expenses)
        return True
    return False

def get_all_expenses():
    """ฟังก์ชันสำหรับดึงข้อมูลทั้งหมดมาแสดงผล"""
    return file_handler.read_data()

def cal_total():
    """ฟังก์ชันคำนวณยอดรวม (เหมือนเดิม)"""
    expenses = file_handler.read_data()
    total = 0
    for row in expenses:
        type_money = row[1]
        amount = float(row[3])
        if type_money == "รายรับ":
            total += amount
        elif type_money == "รายจ่าย":
            total -= amount
    return total