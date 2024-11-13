def check_phone_number(phone_number):
  if len(str(phone_number)) != 9:
    print("ERROR: Phone number should have 9 numbers")
    exit(1)

def check_contact_not_exists(agenda, name, phone_number):
  for contact in agenda:
    if contact["name"] == name:
      print("ERROR: This name already exists. Exiting program")
      exit(1)
    if contact["phone_number"] == phone_number:
      print(f"ERROR: This phone number is already associated with another name")
      exit(1)