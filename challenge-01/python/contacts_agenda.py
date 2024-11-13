from checkers import check_contact_not_exists, check_phone_number

class ContactsAgenda():
  def __init__(self):
    self.agenda = [{"name": "Josep", "phone_number": 672253676}]
  
  def search_contact(self):
    print("searching_contact")
    input_name = str(input("Enter contact name: "))
    for contact in self.agenda:
      if contact["name"] == input_name:
        print(contact)
  
  def insert_contact(self):
    print("Insert contact")
    input_name = str(input("Name: "))
    input_phone_number = int(input("Phone Number: "))

    check_phone_number(input_phone_number)
    check_contact_not_exists(self.agenda, input_name, input_phone_number)

    print(f"Adding new contact with name: {input_name}, phone number: {input_phone_number}")
    new_contact = {"name": input_name, "phone_number": input_phone_number}
    self.agenda.append(new_contact)
    print(self.agenda)
    
  def update_contact(self):
    print("Update_contact")
    input_name = str(input("Contact name to be updated: "))
    x = 0
    for contact in self.agenda:
      if contact["name"] == input_name:
        print(f"Previous name={contact['name']} and phone number={contact['phone_number']}")
        new_name = str(input("Enter new name: "))
        new_phone_number = int(input("Enter new phone number: "))
        self.agenda[x]["name"] = new_name
        self.agenda[x]["phone_number"] = new_phone_number
      x = x + 1  
  
  def delete_contact(self):
    print("Delete contact")
    input_name = str(input("Name: "))
    x = 0
    for contact in self.agenda:
      if contact["name"] == input_name:
        self.agenda.pop(x)
      x = x + 1
    print(f"Contact {input_name} deleted successfully!\n")
  
  def show_agenda(self):
    print("Show agenda")
    print(f"{self.agenda}\n")