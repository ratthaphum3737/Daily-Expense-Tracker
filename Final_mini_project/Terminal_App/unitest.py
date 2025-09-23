import unittest 
import os 
import csv
import io 
from unittest.mock import patch 
from contextlib import redirect_stdout 

# นำเข้าโมดูลที่เราต้องการจะทดสอบ
import file_handler
import operations


# สร้างคลาสสำหรับรวบรวม Test Case ทั้งหมด โดยต้องสืบทอดมาจาก unittest.TestCase
class TestExpenseTracker(unittest.TestCase):
 # ======        ส่วนทดสอบฟังก์ชันใน CONFIG.py      ======
    def setUp(self):
        self.test_filename = "test_expenses.csv"
        self.config_patcher = patch('config.FILENAME', self.test_filename)
        self.config_patcher.start() # เริ่มการ patch
        # ตรวจสอบและลบไฟล์ทดสอบเก่าทิ้ง เพื่อให้ทุกการทดสอบเริ่มต้นจากความว่างเปล่า
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    #ฟังก์ชัน tearDown ---
    #ฟังก์ชันนี้จะถูกเรียกใช้งาน "หลัง" การรันแต่ละ test case เสมอ
    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        self.config_patcher.stop() # หยุดการ patch
        
        
 # ======        ส่วนทดสอบฟังก์ชันใน file_handler.py      ======
    #ทดสอบว่า init_file() สามารถสร้างไฟล์ใหม่พร้อมกับ Header ที่ถูกต้องได้หรือไม่
    def test_init_file_creates_file_with_header(self):
        #ตรวจสอบว่าไฟล์ยังไม่มี
        self.assertFalse(os.path.exists(self.test_filename)) 
        #เรียกใช้ฟังก์ชันที่ต้องการทดสอบ
        file_handler.init_file()
        #ตรวจสอบว่าไฟล์ถูกสร้างขึ้นมาแล้ว
        self.assertTrue(os.path.exists(self.test_filename))
        
        #เปิดไฟล์ขึ้นมาอ่านเพื่อตรวจสอบว่า Header ถูกต้องตามที่คาดหวัง
        with open(self.test_filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ["Date", "Type_Money", "Category", "Amount", "Note"])
       
    #ทดสอบการเขียนข้อมูลต่อท้ายไฟล์ (append) และการอ่านข้อมูลกลับมา
    def test_append_and_read_data(self):
        # ทดสอบการอ่านจากไฟล์ที่ยังไม่มีอยู่ ควรคืนค่าเป็น list ว่าง
        self.assertEqual(file_handler.read_data(), [])

        #เริ่มเขียนและอ่านจริง
        file_handler.init_file()
        record1 = ["2025-09-23 10:00:00", "รายจ่าย", "อาหาร", "50.0", "กาแฟ"]
        record2 = ["2025-09-23 12:00:00", "รายรับ", "เงินเดือน", "1000.0", ""]
        file_handler.append_data(record1) # เขียน record 1 ต่อท้าย
        file_handler.append_data(record2) # เขียน record 2 ต่อท้าย
        
        # อ่านข้อมูลทั้งหมดกลับมาแล้วตรวจสอบความถูกต้อง
        data = file_handler.read_data()
        self.assertEqual(len(data), 2) # ตรวจสอบว่ามี 2 รายการ
        self.assertEqual(data[0], record1) # ตรวจสอบว่ารายการแรกถูกต้อง
        self.assertEqual(data[1], record2) # ตรวจสอบว่ารายการที่สองถูกต้อง
    
    #ทดสอบการเขียนข้อมูลทับไฟล์เดิมทั้งหมด (overwrite)
    def test_write_data(self):
        file_handler.init_file()
        file_handler.append_data(["initial_data"]) # ลองใส่ข้อมูลเริ่มต้นไปก่อน

        # ข้อมูลใหม่ที่ต้องการเขียนทับลงไป
        new_data = [
            ["2025-09-24 08:00:00", "รายจ่าย", "เดินทาง", "25.0", "รถไฟฟ้า"],
            ["2025-09-24 09:00:00", "รายรับ", "โบนัส", "500.0", "พิเศษ"]
        ]
        file_handler.write_data(new_data) # เขียนข้อมูลใหม่ทับทั้งหมด

        # อ่านข้อมูลกลับมาตรวจสอบว่าข้อมูลเก่าหายไปแล้ว และมีแค่ข้อมูลใหม่เท่านั้น
        read_back_data = file_handler.read_data()
        self.assertEqual(read_back_data, new_data)


 # ==        ส่วนทดสอบฟังก์ชันใน operations.py      ==


    # @patch คือการบอกให้ unittest ไป "จำลอง" การทำงานของฟังก์ชันที่เราไม่อยากให้ทำงานจริง
    @patch('operations.file_handler.read_data')
    def test_cal_total(self, mock_read_data): # mock_read_data คือ object ที่จำลองขึ้นมา
        """ทดสอบฟังก์ชัน cal_total() ว่าคำนวณยอดเงินคงเหลือได้ถูกต้องหรือไม่"""
        # กำหนดว่าเมื่อ cal_total เรียกใช้ file_handler.read_data() ให้มันคืนค่าข้อมูลจำลองชุดนี้ออกมา
        mock_read_data.return_value = [
            ["date", "รายรับ", "cat", "10000.0", "note"],
            ["date", "รายจ่าย", "cat", "150.50", "note"],
        ]
        # ยอดที่คาดหวัง: 10000.0 - 150.50 = 9849.5
        self.assertAlmostEqual(operations.cal_total(), 9849.5, places=2)

        # ทดสอบกรณีที่ไม่มีข้อมูลเลย
        mock_read_data.return_value = []
        self.assertEqual(operations.cal_total(), 0)

    @patch('operations.file_handler.append_data') # 1. จำลองฟังก์ชัน append_data
    @patch('builtins.input', side_effect=['ex', 'อาหาร', '120.50', 'ข้าวกลางวัน']) # 2. จำลองการพิมพ์ของผู้ใช้
    @patch('operations.datetime') # 3. จำลองเวลา
    def test_add_expense(self, mock_datetime, mock_input, mock_append_data):
        """ทดสอบฟังก์ชัน add_expense() โดยจำลองการกรอกข้อมูลของผู้ใช้"""
        # กำหนดเวลาจำลอง
        mock_now = mock_datetime.now.return_value
        mock_now.strftime.return_value = "2025-09-23 12:30:00"

        operations.add_expense() # เรียกใช้ฟังก์ชัน

        # ตรวจสอบว่าฟังก์ชัน append_data ถูกเรียกใช้ด้วยข้อมูลที่ถูกต้องตามที่ผู้ใช้ (จำลอง) กรอกเข้ามา
        mock_append_data.assert_called_once_with([
            "2025-09-23 12:30:00", "รายจ่าย", "อาหาร", 120.50, "ข้าวกลางวัน"
        ])

    @patch('operations.file_handler.read_data')
    @patch('operations.cal_total', return_value=950.0) # จำลองให้ cal_total คืนค่า 950.0 เสมอ
    def test_show_expenses(self, mock_cal_total, mock_read_data):
        """ทดสอบฟังก์ชัน show_expenses() ว่าแสดงผลข้อมูลถูกต้องหรือไม่"""
        # กำหนดข้อมูลจำลอง
        sample_data = [
            ["2025-09-23 10:00:00", "รายรับ", "เงินเดือน", "1000.0", ""],
            ["2025-09-23 12:00:00", "รายจ่าย", "อาหาร", "50.0", "กาแฟ"]
        ]
        mock_read_data.return_value = sample_data
        
        # ดักจับทุกอย่างที่ฟังก์ชันจะ print() ออกมา แล้วเก็บไว้ในตัวแปร
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            operations.show_expenses()
        
        output = captured_output.getvalue() # ดึงข้อความที่ดักจับได้ออกมา
        
        # ตรวจสอบว่าข้อความที่ print ออกมานั้นถูกต้องตามที่คาดหวัง
        self.assertIn("1. 2025-09-23 10:00:00 | รายรับ | เงินเดือน | 1000.0 บาท", output)
        self.assertIn("ยอดเงินคงเหลือ: 950.0 บาท", output)

    @patch('operations.file_handler.write_data')
    @patch('builtins.input', return_value='1') # จำลองว่าผู้ใช้พิมพ์ '1' เพื่อลบรายการแรก
    @patch('operations.show_expenses')
    def test_delete_expense(self, mock_show_expenses, mock_input, mock_write_data):
        """ทดสอบฟังก์ชัน delete_expense() ว่าลบข้อมูลได้ถูกต้อง"""
        initial_data = [
            ["date1", "รายจ่าย", "อาหาร", "50.0", "กาแฟ"], # รายการที่จะถูกลบ
            ["date2", "รายรับ", "เงินเดือน", "1000.0", ""]
        ]
        mock_show_expenses.return_value = initial_data

        operations.delete_expense()
        
        # ข้อมูลที่คาดหวังว่าจะเหลืออยู่หลังการลบ
        expected_data_after_delete = [
            ["date2", "รายรับ", "เงินเดือน", "1000.0", ""]
        ]
        # ตรวจสอบว่า write_data ถูกเรียกใช้พร้อมกับข้อมูลที่ถูกต้อง (คือข้อมูลที่เหลืออยู่)
        mock_write_data.assert_called_once_with(expected_data_after_delete)

# --- 5. ส่วนที่ทำให้ไฟล์นี้สามารถรันได้ ---
# บรรทัดมาตรฐานเพื่อให้สามารถรันไฟล์ python นี้ได้โดยตรงจาก command line
if __name__ == '__main__':
    unittest.main()