from datetime import datetime
import file_handler


#เพิ่มรายการที่รับข้อมูลมาจาก Web App
def add_expense(type_money, category, amount, note):
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
    
#ลบรายการตามลำดับที่ได้รับจาก Web App
def delete_expense(index_to_delete):
    expenses = file_handler.read_data()
    if 0 <= index_to_delete < len(expenses):
        expenses.pop(index_to_delete)
        file_handler.write_data(expenses)
        return True
    return False

#สำหรับดึงข้อมูลทั้งหมดมาแสดงผล
def get_all_expenses():
    return file_handler.read_data()

#คำนวณยอดรวม
def cal_total():
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