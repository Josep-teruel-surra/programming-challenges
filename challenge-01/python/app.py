from contacts_agenda import ContactsAgenda

def helper():
  print("1. Search contact")
  print("2. Insert new contact")
  print("3. Update contact")
  print("4. Delete contact")
  print("5. Show agenda")
  print("6. Exit\n")

def options_mapping(contacts_agenda, option_selected):  
  options_map = {1: contacts_agenda.search_contact,
                 2: contacts_agenda.insert_contact,
                 3: contacts_agenda.update_contact,
                 4: contacts_agenda.delete_contact,
                 5: contacts_agenda.show_agenda,
                 6: exit}
  action = options_map.get(option_selected, lambda: "invalid option selected.")
  result = action()
  if result is not None:
    print(result)

def main():
  try:
    contacts_agenda = ContactsAgenda()
    print("Welcome to my agenda!\n")
    while True:
      helper()
      option_selected = int(input("Select an option: "))
      options_mapping(contacts_agenda, option_selected)
  except ValueError:
    print("Please enter a valid option.")

main()