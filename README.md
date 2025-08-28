# Daily Expense Tracker -- Week 1 / Sprint 1

โอ๊ตและเอเดน การนำแผนการทำงานสำหรับ Week 1/Sprint 1 ของโปรเจกต์ 'Daily
Expense Tracker' ไปใช้ร่วมกับ GitHub
จะช่วยให้คุณทั้งคู่สามารถทำงานร่วมกันได้อย่างมีประสิทธิภาพ
มีการจัดการเวอร์ชันของโค้ด และติดตามความคืบหน้าได้ชัดเจนยิ่งขึ้น
กระบวนการนี้สอดคล้องกับหลักการของ Agile Methodology และ DevOps Culture
ที่เน้นการทำงานร่วมกันและวงจรการพัฒนาที่รวดเร็ว

------------------------------------------------------------------------

## การตั้งค่าโปรเจกต์บน GitHub สำหรับ Week 1/Sprint 1

1.  **สร้าง Repository บน GitHub:**
    -   โอ๊ตในฐานะ Planner/Coder ควรเริ่มต้นด้วยการสร้าง GitHub
        Repository ใหม่สำหรับโปรเจกต์ 'Daily Expense Tracker' นี้\
    -   ตั้งชื่อที่ชัดเจน เช่น `daily-expense-tracker-team-a`
        (หรือชื่อทีมของคุณ)\
    -   เลือกเป็น Private repository
        เพื่อความเป็นส่วนตัวระหว่างการพัฒนา\
    -   เพิ่มไฟล์ `README.md` และ `.gitignore` (เลือก Python template)
        ในขั้นตอนการสร้าง
2.  **เชิญเอเดนเข้าร่วม:**
    -   โอ๊ตเชิญเอเดนเข้าเป็น Collaborator ใน Repository
        เพื่อให้เอเดนสามารถเข้าถึงโค้ด, สร้าง Pull Request, และ Review
        โค้ดได้
3.  **Clone Repository:**
    -   ทั้งโอ๊ตและเอเดนทำการ `git clone` Repository
        ลงบนเครื่องคอมพิวเตอร์ของตนเอง

------------------------------------------------------------------------

## เป้าหมายสำหรับ Week 1/Sprint 1 (ในมุมมอง GitHub)

เป้าหมายยังคงเดิมคือ การสร้างโครงสร้างพื้นฐานของโปรแกรม ได้แก่:\
- ลูปหลักของโปรแกรม (main program loop)\
- ฟังก์ชันพื้นฐานสำหรับการบันทึกค่าใช้จ่าย (add expense)\
- ฟังก์ชันการออกจากโปรแกรม ('quit')

โดยข้อมูลค่าใช้จ่ายจะจัดเก็บในรูปแบบ `list of dictionaries`
และโค้ดโดยรวมไม่ควรเกิน 50 บรรทัด เพื่อให้จัดการได้ง่าย

------------------------------------------------------------------------

## บทบาทและภารกิจของแต่ละคนสำหรับ Week 1/Sprint 1 (รวม GitHub Workflow)

### โอ๊ต (Planner & Coder) 🗺️💻

**ในฐานะ Planner (สถาปนิก) 🗺️:**\
- กำหนดแผนงานและข้อกำหนด: โอ๊ตจะใช้ไฟล์ `README.md` หรือสร้างไฟล์
`PLANNING.md` ใน Repository เพื่อระบุ *"What are we building?"* และ
*"Why are we building it this way?"* สำหรับสัปดาห์นี้\
- ระบุว่าโปรแกรมจะเริ่มต้นด้วยข้อความต้อนรับ, แสดงตัวเลือก (add, quit)\
- หากผู้ใช้พิมพ์ 'quit' โปรแกรมจะกล่าวลาและออก\
- หากผู้ใช้พิมพ์ 'add' โปรแกรมจะถาม amount (จำนวนเงิน) และ category
(หมวดหมู่) จากนั้นบันทึกใน list of dictionaries (เช่น `expenses = []`)\
- กำหนดเกณฑ์ 'เสร็จสิ้น' (Define "Done"):
โอ๊ตต้องระบุให้ชัดเจนว่าฟังก์ชัน 'quit'
และการเพิ่มค่าใช้จ่ายพื้นฐานจะถือว่า 'เสร็จสิ้น' ได้เมื่อใด (เช่น
*"ผู้ใช้สามารถออกจากโปรแกรมได้โดยการพิมพ์ 'quit'
โดยไม่คำนึงถึงตัวพิมพ์เล็ก/ใหญ่"* และ
*"ผู้ใช้สามารถเพิ่มค่าใช้จ่ายโดยระบุจำนวนเงินและหมวดหมู่
และข้อมูลถูกจัดเก็บในรายการ"*)\
- **Commit แผนงาน:** เมื่อโอ๊ตสรุปแผนงานใน `PLANNING.md` แล้ว ให้
`git commit` และ `git push` ขึ้นไปที่ `main` branch เพื่อให้เอเดนรับทราบ

**ในฐานะ Coder (ผู้สร้าง) 💻:**\
- **สร้าง Feature Branch:** โอ๊ตจะเริ่มต้นด้วยการสร้าง Branch ใหม่จาก
`main` เพื่อทำงานในส่วนของโค้ดสำหรับสัปดาห์นี้ เช่น:\
- การทำงานใน Branch แยกจะช่วยให้ `main` branch ยังคงเสถียรอยู่\
- **เขียนโค้ดเริ่มต้น:** โอ๊ตจะเขียนโค้ด Python (เช่น ในไฟล์ `app.py`)
เพื่อสร้าง `while loop` หลัก, `if` statement สำหรับคำสั่ง 'quit', และ
`elif` block สำหรับคำสั่ง 'add' รวมถึงการใช้ `input()`
เพื่อรับข้อมูลและเพิ่มลงใน `expenses` list\
- **Commit อย่างสม่ำเสมอ:** เมื่อโค้ดมีความคืบหน้า ให้\
`bash   git add .   git commit -m "feat: implement main loop and basic quit command"   git push origin feature/week1-core-functionality`\
- **สร้าง Pull Request (PR):**
เมื่อโอ๊ตเขียนโค้ดส่วนของตนเองเสร็จสิ้นตามแผนแล้ว ให้สร้าง PR บน GitHub
โดยขอให้เอเดน (Debugger) ทำการ Review โค้ด\
- ระบุใน PR ว่าโค้ดนี้ครอบคลุมฟังก์ชันอะไรบ้าง
และขอให้เอเดนทดสอบตามเกณฑ์ 'เสร็จสิ้น' ที่กำหนดไว้ใน `PLANNING.md`

------------------------------------------------------------------------

### เอเดน (Debugger - ผู้ตรวจสอบคุณภาพ) 🕵️‍♀️

**ในฐานะ Debugger (ผู้ตรวจสอบคุณภาพ) 🕵️‍♀️:**\
- ตรวจสอบแผนงาน: เอเดนควรอ่าน `PLANNING.md` ที่โอ๊ต (Planner)
สร้างขึ้นตั้งแต่ต้นสัปดาห์เพื่อให้เข้าใจเป้าหมายและเกณฑ์ 'เสร็จสิ้น'\
- **Review Pull Request:** เมื่อโอ๊ตสร้าง PR ขึ้นมา เอเดนจะทำการ:\
- *Code Review บน GitHub:* ตรวจสอบโค้ดที่โอ๊ตเขียนโดยตรงบนแพลตฟอร์ม
GitHub เพื่อดูความสะอาด, การใช้ชื่อตัวแปรที่เหมาะสม, และ Comments ต่างๆ\
- *Clone Branch สำหรับทดสอบ:* ทำการ\
`bash     git checkout feature/week1-core-functionality`\
เพื่อดึงโค้ดลงมาทดสอบบนเครื่องของตนเอง\
- *ทดสอบอย่างเป็นระบบ:* เรียกใช้โปรแกรม (`python app.py`)
และทดสอบตามเกณฑ์ 'เสร็จสิ้น' และ พิจารณากรณีพิเศษ (Edge Cases) เช่น:\
- พิมพ์ 'quit', 'Quit', 'QUIT' เพื่อทดสอบ case-sensitivity\
- พิมพ์คำสั่งอื่นที่ไม่รู้จัก\
- ป้อนค่าใช้จ่าย (amount) เป็นตัวเลข, ตัวอักษร\
- ป้อนหมวดหมู่ (category) เป็นช่องว่าง\
- **ให้ข้อเสนอแนะใน Pull Request:** หากพบข้อผิดพลาดหรือไม่เป็นไปตามเกณฑ์
'เสร็จสิ้น' เอเดนจะเขียนรายงานข้อผิดพลาดที่ชัดเจน ในรูปแบบ Comments บน
Pull Request ของโอ๊ต\
- Observation (สิ่งที่ฉันทำ):
`"When I type 'Quit' (with capital Q'...)"`\
- Expectation (สิ่งที่ฉันคาดหวัง): `"...I expect the program to exit."`\
- Result (สิ่งที่เกิดขึ้นจริง):
`"...but the program continues to run, printing 'Invalid command.'"`\
- **อนุมัติ/ขอแก้ไข:**\
- หากพบข้อผิดพลาด: เอเดนจะคอมเมนต์และขอให้โอ๊ตแก้ไข\
- โอ๊ตจะทำการแก้ไขใน Branch เดิม (`feature/week1-core-functionality`),
`git commit`, `git push`\
- เอเดนจะ re-test และเมื่อทุกอย่างถูกต้อง ให้ Approve Pull Request\
- **Merge Pull Request:** หลังจาก Debugger (เอเดน) Approve แล้ว โอ๊ต
(หรือเอเดน ตามที่ตกลงกัน) สามารถ Merge Pull Request เข้าสู่ `main`
branch ได้ ซึ่งเป็นการยืนยันว่าโค้ดชุดนี้ผ่านการตรวจสอบและพร้อมใช้งาน

------------------------------------------------------------------------

## The Friday Review & Feedback (15 นาที)

ก่อนจะเริ่ม Week 2 ทั้งทีมควรมีการประชุมร่วมกัน:\
- Debugger นำเสนอผลการทดสอบ: เอเดนอธิบายว่าได้ทดสอบอะไรไปบ้าง,
พบปัญหาอะไร และแก้ไขอย่างไร\
- ทบทวนสิ่งที่เรียนรู้: การพูดคุยเกี่ยวกับ "Wow!" (ความสำเร็จ) และ
"Whoops!" (ความท้าทาย) จะช่วยให้ทีมเรียนรู้และปรับปรุงกระบวนการทำงานใน
Sprint ถัดไป\
- ยืนยันการ Merge: ตรวจสอบให้แน่ใจว่าโค้ดที่ผ่านการรับรองถูกรวมเข้าสู่
`main` branch แล้วบน GitHub

------------------------------------------------------------------------

## Full Function Source Code สำหรับ Week 1/Sprint 1

นี่คือโค้ดตัวอย่างสำหรับ `app.py` ที่ โอ๊ต (Coder) จะพัฒนาขึ้นใน Week
1/Sprint 1 เพื่อให้เป็นไปตามเป้าหมาย (ประมาณ 35 บรรทัด):

``` python
# A simple command-line Daily Expense Tracker

expenses = [] # This will store our expenses as a list of dictionaries

print("Welcome to your Daily Expense Tracker!")

while True:
    # Display options to the user
    command = input("\nChoose an option: add, quit\n> ").lower() # Convert input to lowercase for case-insensitivity

    if command == 'quit':
        print("Goodbye! See you next time.")
        break # Exit the loop and the program
    elif command == 'add':
        try:
            amount_str = input("Enter expense amount (e.g., 50.00): ")
            amount = float(amount_str) # Convert input to a float
            category = input("Enter expense category (e.g., Food, Transport): ")
            
            # Store the expense as a dictionary
            expense = {
                'amount': amount,
                'category': category
            }
            expenses.append(expense)
            print(f"Expense of {amount:.2f} in category '{category}' added.")
            # print(f"Current expenses: {expenses}") # For debugging/checking internal state
        except ValueError:
            print("Invalid amount. Please enter a number for the amount.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Invalid command. Please try again.")
```

**หมายเหตุ:** โค้ดข้างต้นมีการเพิ่ม `try-except` block เพื่อจัดการกับ
`ValueError` ในกรณีที่ผู้ใช้ป้อน amount ที่ไม่เป็นตัวเลข
ซึ่งเป็นตัวอย่างที่ดีของการคิดถึง Edge Cases ที่เอเดน (Debugger)
อาจจะทดสอบเจอ

------------------------------------------------------------------------

การใช้ GitHub จะช่วยให้คุณทั้งคู่เรียนรู้การทำงานแบบมืออาชีพ
ทั้งในเรื่องการเขียนโค้ด, การสื่อสาร, การให้ Feedback
และการจัดการโปรเจกต์ ซึ่งเป็นทักษะที่ AI ยังไม่สามารถทำแทนมนุษย์ได้
อย่างสมบูรณ์
