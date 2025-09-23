import csv
import os
import config 

#ฟังก์ชันสำหรับสร้างไฟล์ถ้ายังไม่มี พร้อมใส่ Header
def init_file():
    if not os.path.exists(config.FILENAME):
        with open(config.FILENAME, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Type_Money", "Category", "Amount", "Note"])

#ฟังก์ชันสำหรับอ่านข้อมูล
def read_data():
    if not os.path.exists(config.FILENAME):
        return []  # ถ้าไม่มีไฟล์ คืนค่าเป็น list ว่าง
    
    with open(config.FILENAME, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader) 
        return list(reader)

#ฟังก์ชันสำหรับเขียนทับข้อมูลทั้งหมดลงในไฟล์ CSV
def write_data(data):
    header = ["Date", "Type_Money", "Category", "Amount", "Note"]
    with open(config.FILENAME, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
   
#ฟังก์ชันสำหรับต่อท้ายข้อมูลลงในไฟล์ CSV    
def append_data(record):
    with open(config.FILENAME, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(record)