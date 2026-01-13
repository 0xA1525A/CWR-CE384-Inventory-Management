กำหนดข้อมูลของ warehouse ดังนี้

inventory = {
    "Laptop": 10,
    "Mouse": 50,
    "Monitor": 15
}
prices = {"Laptop": 1000, "Mouse": 25, "Monitor": 200}

# List of orders: (Item Name, Quantity)
orders = [("Laptop", 2), ("Mouse", 60), ("Monitor", 1), ("Keyboard", 5)]

จงเขียนส่วนของโปรแกรมภาษา python โดยมีการทำงานดังนี้

    ใช้คำสั่งการวนซ้ำในการประมวลผล order แต่ละอันโดยตัดสต๊อกจาก inventory
    คำนวณยอดขายแต่ละ order เก็บในตัวแปร subtotal และยอดขายรวมทั้งหมดเก็บในตัวแปร total
    หาก order มากกว่าจำนวนของที่มีให้แสดงข้อความว่า "Sorry, insufficient inventory"
    หาก order เป็นสินค้าที่ไม่มีใน warehouse ให้แสดงข้อความว่า "Error, unknown item"
    พิมพ์ยอดขาย subtotal ในแต่ละ order
    สุดท้ายพิมพ์ยอดขายรวม total และ รายการสินค้าคงคลังที่เหลือโดยบอกชนิดและจำนวนที่เหลือ ห้ามพิมพ์ inventory ออกมาโดยตรง

สิ่งที่ต้องส่ง

    รายชื่อของสมาชิกทุกคนในกลุ่ม (รวมชื่อผู้ส่งด้วย)
    ไฟล์โปรแกรม python
    video clip แสดงหน้าสมาชิกทุกคนและคำอธิบายการทำงานของ code แต่ละบรรทัด โดยให้ส่ง link ของ video clip มา (ไม่ต้องส่ง video file มา)
    สำหรับสมาชิกคนอื่นๆ ให้ส่งชื่อของผู้ส่งหลักมา ไม่ต้องต้องไฟล์และ link
