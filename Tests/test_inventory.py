from InventoryManagement import InventoryManager

# Initialize
manager = InventoryManager()

# Add Sections
manager.add_section("Electronics")
manager.add_section("Clothing")

# Add Items
manager.add_item("Electronics", "Laptop", 10)
manager.add_item("Clothing", "T-shirt", 20)

# Stock Management
manager.add_item("Electronics", "Laptop", 5)
manager.remove_item("Electronics", "Laptop", 2)

# Moving Items
manager.move_item("Electronics", "Clothing", "Laptop", 3)

# Display Inventory
print(manager.get_inventory_overview())
