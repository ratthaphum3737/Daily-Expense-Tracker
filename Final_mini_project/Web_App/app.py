# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import operations
import file_handler
import config
file_handler.init_file()

app = Flask(__name__)
#โหลดค่าตั้งค่าทั้งหมดจากไฟล์ config.py ---
app.config.from_object(config)

 
#สำหรับแสดงรายการทั้งหมดและฟอร์ม
@app.route('/')
def index():
    expenses = operations.get_all_expenses() 
    total = operations.cal_total()          
    return render_template('index.html', expenses=expenses, total=total)

@app.route('/add', methods=['POST'])
def add_expense():
    """รับข้อมูลจากฟอร์มเพื่อเพิ่มรายการใหม่"""
    expense_type = request.form.get('expense_type')
    category = request.form.get('category')
    amount = request.form.get('amount')
    note = request.form.get('note')

    success, message = operations.add_expense(
        expense_type, category, amount, note
    )

    if success:
        flash(message, 'success') 
    else:
        flash(message, 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_expense(index):
    """ลบรายการตามลำดับ (index) ที่ส่งมา"""
    if operations.delete_expense(index):
        flash('ลบรายการเรียบร้อยแล้ว', 'success')
    else:
        flash('ไม่สามารถลบรายการได้', 'error')
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)