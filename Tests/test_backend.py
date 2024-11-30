from InventoryManagement import InventoryManager

# Initialize the InventoryManager
manager = InventoryManager()

# adding sections
manager.add_section("Electronics")
manager.add_section("Clothing")
print(manager.get_inventory_overview())  # Should display both sections

# adding items
manager.add_item("Electronics", "Laptop", 10)
manager.add_item("Clothing", "T-shirt", 50)
print(manager.get_inventory_overview())  # Should show items under sections

# removing items
manager.remove_item("Electronics", "Laptop", 5)
print(manager.get_inventory_overview())  #update the Laptop quantity
