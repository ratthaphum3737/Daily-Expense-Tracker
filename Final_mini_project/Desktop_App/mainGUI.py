import tkinter as tk
from tkinter import ttk, messagebox
import operationsGUI

class ExpenseTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("โปรแกรมบันทึกรายรับ-รายจ่าย")
        self.geometry("950x550") 
        self.resizable(False, False) 

        self.create_widgets()
        self.populate_treeview()

    def create_widgets(self):
        
        input_frame = ttk.LabelFrame(self, text="เพิ่มรายการใหม่") # Input & Controls Frame
        input_frame.place(x=10, y=10, width=930, height=150)

        ttk.Label(input_frame, text="ประเภท:").place(x=10, y=10)
        self.expense_type = tk.StringVar(value="รายจ่าย")
        ttk.Radiobutton(input_frame, text="รายรับ", variable=self.expense_type, value="รายรับ").place(x=120, y=10)
        ttk.Radiobutton(input_frame, text="รายจ่าย", variable=self.expense_type, value="รายจ่าย").place(x=200, y=10)

        ttk.Label(input_frame, text="หมวดหมู่:").place(x=10, y=40)
        self.category_entry = ttk.Entry(input_frame)
        self.category_entry.place(x=120, y=40, width=250)
        
        ttk.Label(input_frame, text="จำนวนเงิน:").place(x=400, y=40)
        self.amount_entry = ttk.Entry(input_frame)
        self.amount_entry.place(x=480, y=40, width=250)

        ttk.Label(input_frame, text="บันทึกเพิ่มเติม:").place(x=10, y=70)
        self.note_entry = ttk.Entry(input_frame)
        self.note_entry.place(x=120, y=70, width=610)

        add_button = ttk.Button(input_frame, text="เพิ่มรายการ", command=self.add_new_expense)
        add_button.place(x=350, y=105, width=120)

        delete_button = ttk.Button(input_frame, text="ลบรายการที่เลือก", command=self.delete_selected_expense)
        delete_button.place(x=480, y=105, width=120)


        display_frame = ttk.LabelFrame(self, text="รายการทั้งหมด") # Data Display Frame 
        display_frame.place(x=10, y=170, width=930, height=320)

        columns = ("ID", "Date", "Type", "Category", "Amount", "Note")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings")
        
        self.tree.heading("ID", text="ลำดับ")
        self.tree.heading("Date", text="วันที่/เวลา")
        self.tree.heading("Type", text="ประเภท")
        self.tree.heading("Category", text="หมวดหมู่")
        self.tree.heading("Amount", text="จำนวนเงิน")
        self.tree.heading("Note", text="บันทึกเพิ่มเติม")
        
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Date", width=150)
        self.tree.column("Type", width=80, anchor="center")
        self.tree.column("Category", width=120)
        self.tree.column("Amount", width=100, anchor="e")
        self.tree.column("Note", width=200)

        scrollbar = ttk.Scrollbar(display_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.place(x=5, y=5, width=895, height=290)
        scrollbar.place(x=900, y=5, height=290)

        
        status_frame = ttk.Frame(self) # Status Bar
        status_frame.place(x=10, y=500, width=930, height=40)

        self.total_label = ttk.Label(status_frame, text="ยอดเงินคงเหลือสุทธิ: 0.00 บาท", font=("Helvetica", 12, "bold"))
        # ใช้ relx=1.0 และ anchor='ne' เพื่อจัดชิดขวา
        self.total_label.place(relx=1.0, x=-5, y=5, anchor='ne')

    def populate_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        expenses = operationsGUI.get_all_expenses()
        for i, row in enumerate(expenses, 1):
            self.tree.insert("", "end", values=(i, *row))
        self.update_total_label()

    def update_total_label(self):
        total = operationsGUI.cal_total()
        self.total_label.config(text=f"ยอดเงินคงเหลือสุทธิ: {total:,.2f} บาท")

    def add_new_expense(self):
        success, message = operationsGUI.add_expense_from_gui(
            self.expense_type.get(),
            self.category_entry.get(),
            self.amount_entry.get(),
            self.note_entry.get()
        )
        if success:
            messagebox.showinfo("สำเร็จ", message)
            self.clear_entries()
            self.populate_treeview()
        else:
            messagebox.showerror("ผิดพลาด", message)

    def delete_selected_expense(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("คำเตือน", "กรุณาเลือกรายการที่ต้องการลบ")
            return
        
        if messagebox.askyesno("ยืนยันการลบ", "คุณต้องการลบรายการที่เลือกใช่หรือไม่?"):
            selected_values = self.tree.item(selected_item, "values")
            index_to_delete = int(selected_values[0]) - 1

            if operationsGUI.delete_expense_by_index(index_to_delete):
                messagebox.showinfo("สำเร็จ", "ลบรายการเรียบร้อยแล้ว")
                self.populate_treeview()
            else:
                messagebox.showerror("ผิดพลาด", "ไม่สามารถลบรายการได้")

    def clear_entries(self):
        self.category_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)
        self.expense_type.set("รายจ่าย")

if __name__ == "__main__":
    # ตรวจสอบก่อนว่ามีการสร้างไฟล์ข้อมูลแล้วหรือยัง
    import file_handler
    file_handler.init_file()
    
    app = ExpenseTrackerApp()
    app.mainloop()