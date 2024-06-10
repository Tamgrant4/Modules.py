# Q1 

#Task 1

def mood_response(mood):
  """
  Provides a custom message based on the user's entered mood.

  Args:
      mood: A string representing the user's mood (e.g., happy, sad, excited).

  Returns:
      A string containing a message corresponding to the mood.
  """
  moods = {
      "happy": "That's great to hear! I hope you have a wonderful day.",
      "sad": "I'm sorry to hear that. Is there anything I can do to help?",
      "excited": "That's awesome! What are you excited about?",
      "angry": "It's okay to feel angry sometimes. Take a deep breath and try to calm down.",
      "frustrated": "I understand feeling frustrated. Maybe taking a break can help.",
  }
  # Default message if the mood is not found in the dictionary
  default_message = "Thanks for sharing your mood! How can I help you today?"

  return moods.get(mood.lower(), default_message)

# Example usage (no user input or file reading required)
# print(mood_response("happy"))  # Output: That's great to hear! I hope you have a wonderful day.
# print(mood_response("frustrated"))  # Output: I understand feeling frustrated. Maybe taking a break can help.
# print(mood_response("unknown"))  # Output: Thanks for sharing your mood! How can I help you today?

import mood_responses

mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))


# Q 1

# Task 1

def add_contact(contacts, name, phone_number, email):
  """
  Adds a new contact to the list.

  Args:
      contacts: A list to store contacts (dictionaries).
      name: The name of the contact (string).
      phone_number: The phone number of the contact (string).
      email: The email address of the contact (string).

  Returns:
      None
  """
  if not name:
    print("Name cannot be empty.")
    return

  contact = {"name": name, "phone_number": phone_number, "email": email}
  contacts.append(contact)
  print(f"Contact added successfully: {name}")

def remove_contact(contacts, name):
  """
  Removes a contact from the list by name.

  Args:
      contacts: A list to store contacts (dictionaries).
      name: The name of the contact to remove (string).

  Returns:
      None
  """
  found = False
  for i, contact in enumerate(contacts):
    if contact["name"] == name:
      contacts.pop(i)
      found = True
      print(f"Contact removed successfully: {name}")
      break
  if not found:
    print(f"Contact not found: {name}")

def display_contacts(contacts):
  """
  Displays all contacts in the list.

  Args:
      contacts: A list to store contacts (dictionaries).

  Returns:
      None
  """
  if not contacts:
    print("There are no contacts in the list.")
    return
  print("Contacts:")
  for i, contact in enumerate(contacts):
    print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")

def search_contact(contacts, name):
  """
  Searches for a contact by name and displays its details.

  Args:
      contacts: A list to store contacts (dictionaries).
      name: The name of the contact to search for (string).

  Returns:
      None
  """
  found = False
  for contact in contacts:
    if contact["name"] == name:
      print(f"Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}")
      found = True
      break
  if not found:
    print(f"Contact not found: {name}")

from contacts_manager import add_contact, remove_contact, display_contacts, search_contact

# Initialize an empty list to store contacts
contacts = []

while True:
  print("\nContact List Manager")
  print("1. Add Contact")
  print("2. Remove Contact")
  print("3. Display Contacts")
  print("4. Search Contact")
  print("5. Exit")

  choice = input("Enter your choice (1-5): ")

  if choice == '1':
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number (optional): ")
    email = input("Enter email address (optional): ")
    add_contact(contacts, name, phone_number, email)
  elif choice == '2':
    name = input("Enter name of contact to remove: ")
    remove_contact(contacts, name)
  elif choice == '3':
    display_contacts(contacts)
  elif choice == '4':
    name = input("Enter name of contact to search: ")
    search_contact(contacts, name)
  elif choice == '5':
    print("Exiting Contact List Manager.")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 5.")
# Q3 

# Task1

def reverse_string(s):
  """
  Reverses the characters of a given string.

  Args:
      s: The string to be reversed (str).

  Returns:
      The reversed string (str).
  """
  return s[::-1]

def capitalize_string(s):
  """
  Capitalizes the first letter of each word in a string.

  Args:
      s: The string to be capitalized (str).

  Returns:
      The capitalized string (str).
  """
  return s.title()

# Import text_utils with an alias 'tu'
from text_utils import reverse_string as tu_reverse, capitalize_string as tu_capitalize

# Get user input
text = input("Enter some text: ")

# Use functions with aliases
reversed_text = tu_reverse(text)
capitalized_text = tu_capitalize(text)

# Print results
print("Original Text:", text)
print("Reversed Text:", reversed_text)
print("Capitalized Text:", capitalized_text)
