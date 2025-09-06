# Daily Income and Expenses Tracker

แน่นอนครับ สำหรับโปรเจกต์ "Daily Income and Expenses Tracker" ในสัปดาห์ที่ 1 / สปรินต์ที่ 1 เราจะมาปรับแผนงานให้เข้ากับบริบทของการทำงานร่วมกันผ่าน GitHub และนำเสนอ โค้ดฟังก์ชันเต็มรูปแบบ สำหรับสัปดาห์นี้ครับ  
การใช้ GitHub จะช่วยให้ โอ๊ต และ เอเดน ได้ฝึกฝนกระบวนการทำงานแบบมืออาชีพ ทั้งการเขียนโค้ด การตรวจสอบ การให้ข้อเสนอแนะ และการประสานงาน ซึ่งเป็นทักษะสำคัญที่ AI ยังไม่สามารถทำแทนได้

---

## แผนงานสัปดาห์ที่ 1 / สปรินต์ที่ 1: การสร้างรากฐานของโปรแกรมบน GitHub

**เป้าหมายของสัปดาห์นี้:**  
สร้างโครงสร้างหลักของโปรแกรมติดตามรายรับ-รายจ่ายรายวัน โดยให้โปรแกรมสามารถแสดงข้อความต้อนรับ ตัวเลือกต่างๆ และมีฟังก์ชัน "quit" เพื่อออกจากโปรแกรมได้อย่างถูกต้อง และเรียนรู้การทำงานร่วมกันบน GitHub.  

**บทบาทสำหรับสัปดาห์ที่ 1:**  
- โอ๊ต: Planner (ผู้วางแผน) และ Coder (ผู้สร้าง)  
- เอเดน: Debugger (ผู้ตรวจสอบ)  

---

## 1. การตั้งค่า GitHub Repository และ Workflow พื้นฐาน
1. **สร้าง Repository (โอ๊ต):**
    - โอ๊ตในฐานะ Planner/Coder จะเป็นผู้เริ่มต้นสร้าง GitHub Repository ใหม่สำหรับโปรเจกต์นี้ (เช่น daily-tracker-project).
    - สร้างไฟล์ README.md เพื่ออธิบายโปรเจกต์และวัตถุประสงค์สั้นๆ.
    - เชิญ เอเดน เข้ามาเป็น Collaborator ใน Repository.  

2. **Clone Repository (เอเดน):**
    - เอเดนจะ git clone Repository นี้ลงในเครื่องของตัวเอง.  

3. **Branching Strategy:**
    - ทุกคนจะทำงานบน Branch ของตัวเองเพื่อแยกงานออกจาก Branch หลัก (main หรือ master).
    - โอ๊ต: จะสร้าง Branch สำหรับการพัฒนาฟีเจอร์แรก เช่น feature/week1-base-structure.
    - เอเดน: จะทำงานโดยการ pull โค้ดล่าสุดจาก Branch ของโอ๊ตเพื่อทำการทดสอบ หรือสร้าง Branch bugfix/week1-testing หากพบข้อผิดพลาด.  

---

## 2. ภารกิจและกระบวนการทำงานบน GitHub สำหรับสัปดาห์ที่ 1

### 2.1 ภารกิจของโอ๊ต (Planner / Coder):

**ในฐานะ Planner (ผู้วางแผน):**
- วางแผนโครงสร้างหลัก: กำหนดว่าโปรแกรมควรมีอะไรบ้างในสัปดาห์นี้:
    - ข้อความต้อนรับ `print("Welcome to your Daily Income and Expenses Tracker!")`
    - ลูปหลัก ที่ทำงานต่อเนื่อง (while True).
    - ตัวเลือกคำสั่ง ให้ผู้ใช้เห็น เช่น add_income, add_expense, view_summary, quit.
    - การรับคำสั่งจากผู้ใช้ (input()) และแปลงเป็นตัวพิมพ์เล็ก (.lower()).
    - คำสั่ง 'quit' ที่ทำให้โปรแกรมแสดงข้อความ "Goodbye!" และออกจากลูป (break).
    - การจัดการคำสั่งที่ไม่ถูกต้อง (else block).
- จัดทำเอกสารแผนงาน: เขียนสรุปแผนงานนี้ในไฟล์ PLANNING.md หรือใน README.md ของ Repository และ Commit ขึ้น GitHub.  
    - ทักษะที่ฝึกฝน: Problem Formulation & Context และ Big-Picture & Systems Thinking.  

**ในฐานะ Coder (ผู้สร้าง):**
- เขียนโค้ด Python สำหรับโครงสร้างพื้นฐาน:
    - ใน Branch feature/week1-base-structure ของตัวเอง.
    - ตามแผนที่วางไว้ (ดูส่วน "3. โค้ด Python สำหรับสัปดาห์ที่ 1" ด้านล่าง).
    - เน้นการเขียน Clean Code ใช้ชื่อตัวแปรที่สื่อความหมาย และเพิ่มคอมเมนต์ในส่วนที่สำคัญ.
- Git Workflow (โอ๊ต):
    ```bash
    git checkout -b feature/week1-base-structure
    git add .
    git commit -m "feat: Implement basic program loop and quit functionality"
    git push origin feature/week1-base-structure
    ```
    - สร้าง Pull Request (PR): เปิด PR จาก feature/week1-base-structure ไปยัง main (หรือ dev ถ้ามี). ใน PR ให้แน่ใจว่าได้ระบุ เอเดน เป็น reviewer.  
    - ทักษะที่ฝึกฝน: Problem-solving และ Software Craftsmanship.  

---

### 2.2 ภารกิจของเอเดน (Debugger):

**ในฐานะ Debugger (ผู้ตรวจสอบ):**
- ตรวจสอบและทดสอบโค้ด: เมื่อโอ๊ตสร้าง Pull Request แล้ว เอเดนจะ:
    - git pull เพื่อดึงโค้ดล่าสุดมาไว้ในเครื่อง.
    - เรียกใช้โค้ดจาก Branch ของโอ๊ต (feature/week1-base-structure).
    - ทดสอบอย่างเป็นระบบ:
        - ทดสอบการเริ่มต้นโปรแกรม: ข้อความต้อนรับและตัวเลือกแสดงถูกต้องหรือไม่.
        - ทดสอบฟังก์ชัน quit: พิมพ์ 'quit', 'Quit', 'QUIT' เพื่อดูว่าโปรแกรมปิดตัวลงและแสดงข้อความกล่าวลาหรือไม่.
        - ทดสอบกรณีขอบ (Edge Cases): ลองพิมพ์คำสั่งที่ไม่ถูกต้อง เช่น 'hello', 'exit', 'qUiT' เพื่อดูว่าโปรแกรมตอบสนองอย่างไร (ควรจะปิดตัวลงสำหรับ 'quit' ในรูปแบบต่างๆ และแสดงข้อความ "คำสั่งไม่ถูกต้อง" สำหรับคำสั่งอื่นๆ).
- ให้ข้อเสนอแนะผ่าน GitHub Pull Request:
    - หากพบข้อบกพร่อง ให้เพิ่มคอมเมนต์โดยตรงใน Pull Request ของโอ๊ต โดยใช้รูปแบบ Bug Report ที่ชัดเจน:
        - **What I did** (สิ่งที่ฉันทำ)
        - **What I expected to happen** (สิ่งที่ฉันคาดหวัง)
        - **What actually happened** (สิ่งที่เกิดขึ้นจริง)
    - หากโค้ดทำงานได้ถูกต้อง ให้อนุมัติ Pull Request และให้คำชมเชย/ข้อเสนอแนะเพิ่มเติมเกี่ยวกับการปรับปรุง (Refinement).
    - ทักษะที่ฝึกฝน: Systematic Thinking, Attention to Detail และ Master Communication (โดยเฉพาะการให้ Feedback).  

---

### 2.3 กระบวนการสื่อสารบน GitHub และการประชุม:
- **The Monday Huddle (การประชุมต้นสัปดาห์):** โอ๊ตนำเสนอแผนในไฟล์ PLANNING.md ให้เอเดนฟัง และหารือเพื่อให้เข้าใจตรงกัน.
- **Mid-Week Handoff (ส่งมอบโค้ด):** โอ๊ตสร้าง Pull Request เพื่อส่งมอบโค้ดให้เอเดนตรวจสอบ.
- **The Friday Review (ทบทวนประจำสัปดาห์):** เอเดนนำเสนอผลการทดสอบและข้อบกพร่องที่พบผ่าน Pull Request. โอ๊ตและเอเดนร่วมกันแก้ไข และพิจารณา Merge โค้ดเข้าสู่ main Branch. ทั้งคู่จะทบทวน "Wow!" และ "Whoops!" ของสัปดาห์.
    - "The Bug is the Team's Problem": เน้นย้ำว่าข้อบกพร่องใดๆ ที่พบเป็นความรับผิดชอบร่วมกันของทีม ไม่ใช่ความผิดของโอ๊ตแต่เพียงผู้เดียว.  

---

## 3. โค้ด Python สำหรับสัปดาห์ที่ 1 / สปรินต์ที่ 1
นี่คือโค้ด Python เบื้องต้นสำหรับ Week 1 ที่โอ๊ต (Coder) จะเป็นผู้เขียนและ Commit ขึ้น GitHub:

```python
# daily_tracker.py

def run_tracker():
    """
    เริ่มต้นและจัดการลูปหลักของโปรแกรมติดตามรายรับ-รายจ่ายรายวัน
    ในสัปดาห์ที่ 1 นี้ จะเน้นไปที่การแสดงผลข้อความต้อนรับ,
    ตัวเลือกคำสั่ง และฟังก์ชัน 'quit' เท่านั้น.
    """
    
    print("Welcome to your Daily Income and Expenses Tracker!")
    print("--------------------------------------------------")

    while True:
        # แสดงตัวเลือกคำสั่งให้ผู้ใช้ [22]
        print("\nAvailable commands:")
        print("  - add_income   (เพิ่มรายรับ)")
        print("  - add_expense  (เพิ่มรายจ่าย)")
        print("  - view_summary (ดูสรุป)")
        print("  - quit         (ออกจากโปรแกรม)")
        
        # รับคำสั่งจากผู้ใช้และแปลงเป็นตัวพิมพ์เล็ก [22]
        command = input("Please enter a command: ").lower().strip() # .strip() เพื่อลบช่องว่างหน้าหลัง
        
        if command == 'quit':
            # หากผู้ใช้พิมพ์ 'quit' ให้แสดงข้อความกล่าวลาและออกจากโปรแกรม [22]
            print("\nGoodbye! Thank you for using the tracker.")
            break
        elif command == 'add_income':
            print("\n(Feature coming soon: Add Income)")
            # ในอนาคต จะมีโค้ดสำหรับเพิ่มรายรับที่นี่
        elif command == 'add_expense':
            print("\n(Feature coming soon: Add Expense)")
            # ในอนาคต จะมีโค้ดสำหรับเพิ่มรายจ่ายที่นี่
        elif command == 'view_summary':
            print("\n(Feature coming soon: View Summary)")
            # ในอนาคต จะมีโค้ดสำหรับดูสรุปที่นี่
        else:
            # จัดการคำสั่งที่ไม่ถูกต้อง [23]
            print(f"\nInvalid command: '{command}'. Please try again.")
            print("Type 'quit' to exit.")

# นี่คือส่วนที่ทำให้โปรแกรมทำงานเมื่อไฟล์ถูกรันโดยตรง
if __name__ == "__main__":
    run_tracker()

```

## สรุปสำหรับสัปดาห์นี้:

การใช้ GitHub ไม่ใช่แค่การเก็บโค้ด แต่เป็นเครื่องมือในการฝึกฝนทักษะที่ทำให้คุณเป็น "irreplaceable programmer". การที่โอ๊ตวางแผนและเขียนโค้ดอย่างเป็นระบบ และเอเดนตรวจสอบอย่างละเอียดพร้อมให้ข้อเสนอแนะที่ชัดเจน จะเป็นการสร้างรากฐานที่ดีเยี่ยมไม่เพียงแค่สำหรับโปรเจกต์นี้ แต่ยังรวมถึงทักษะการทำงานเป็นทีมและทักษะมนุษย์ที่ AI ทำแทนไม่ได้อีกด้วย. จงจำไว้ว่า AI เป็นเพียง co-pilot ที่ทรงพลัง แต่คุณคือผู้ควบคุมเครื่องบิน!

