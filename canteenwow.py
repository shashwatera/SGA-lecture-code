canteen_location = ("Block A", "Ground Floor")
working_hours = ("9AM", "5PM")
canteen_contact_details = ("9292929292", "1010101010", "8205728483")

print(canteen_location)
print(canteen_location[0])
print(len(canteen_location))

print(canteen_contact_details[0])
if "Block A" in canteen_location:
    print("Block A is present in the tuple 'canteen_locations'")