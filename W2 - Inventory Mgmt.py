# [INSTRUCTION]
"""
จงเขียนส่วนของโปรแกรมภาษา python โดยมีการทำงานดังนี้

    ใช้คำสั่งการวนซ้ำในการประมวลผล order แต่ละอันโดยตัดสต๊อกจาก inventory
    คำนวณยอดขายแต่ละ order เก็บในตัวแปร subtotal และยอดขายรวมทั้งหมดเก็บในตัวแปร total
    หาก order มากกว่าจำนวนของที่มีให้แสดงข้อความว่า "Sorry, insufficient inventory"
    หาก order เป็นสินค้าที่ไม่มีใน warehouse ให้แสดงข้อความว่า "Error, unknown item"
    พิมพ์ยอดขาย subtotal ในแต่ละ order
    สุดท้ายพิมพ์ยอดขายรวม total และ รายการสินค้าคงคลังที่เหลือโดยบอกชนิดและจำนวนที่เหลือ ห้ามพิมพ์ inventory ออกมาโดยตรง
"""

inventory: dict[str, int] = {
    "Laptop":  10,
    "Mouse":   50,
    "Monitor": 15
}

prices: dict[str, int] = {
    "Laptop":  1_000,
    "Mouse":   25,
    "Monitor": 200
} 

# List of orders: (Item Name, Quantity)
orders: list[tuple[str|int]] = [("Laptop", 2), ("Mouse", 60), ("Monitor", 1), ("Keyboard", 5)]

def process_order() -> int:
    total: int = 0

    for (order_item, order_amount) in orders:
        subtotal: int = 0
        inventory_value: int = inventory.get(order_item)

        if not inventory_value:
            print(f"Order: {order_item}*{order_amount} [CANCELLED]:\n  **Error: Unknown Item\n")
            continue

        if order_amount > inventory_value:
            print(f"Order: {order_item}*{order_amount} [CANCELLED]:\n  **Sorry, Insufficient Inventory (has {inventory_value})\n")
            continue

        subtotal: int = prices.get(order_item) * order_amount
        total += subtotal
        print(f"Order: {order_item}*{order_amount}:\n    {prices.get(order_item)}THB each | Subtotal: {subtotal}THB\n")
        subtract_item_from_inventory(order_item, order_amount)

    print(f"Total Of: {total}THB")
    dump_inventory_items()
    
    return total

def subtract_item_from_inventory(item: str, amount: int) -> None:
    inventory[item] -= amount

def dump_inventory_items() -> None:
    items: list[str] = inventory.keys()
    print("Inventory Update:")
    
    for item in items:
        print(f"    {item}: {inventory.get(item)}")

if __name__ == "__main__":
    process_order()