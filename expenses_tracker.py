def log_expenses(func):
  def wrapper(*args,**kwargs):
     print("Entering the expenses data...")
     result = func(*args, **kwargs) #will call the add_expenses function
     return result
  return wrapper
#list to store all the expenses in dictionary
expenses = [] 

@log_expenses
def add_expenses():
  amount = float(input("Enter the amount: "))
  product = input("Enter the product name: ")
  notes = input("Enter any notes: ")
  date = input("Enter date (YYYY-MM-DD): ")
  expense = { "amount": amount,
             "product": product,
              "note": notes,
              "date": date
            }
  expenses.append(expense) #append is used to new item
  print("Expense added successfully")

  more = input("Do you want to add more expenses? (yes/no):").lower()
  if more == "yes":
    add_expenses()
  else:
    print("Thank you")

def view_expenses():
  #checks if there is no data in the dictionary
  if not expenses:
    print("No expenses found")
  else:
      print("Expenses")
      for expense in expenses:
        print(f"₹{expense['amount']} - {expense['product']} - {expense['note']} - {expense['date']}\n")

def total_expenses():
  total = sum(expense["amount"] for expense in expenses)
  print(f"Total Expenses: ₹{total}")  #to get the total expenses

def main_menu():
  while True:
    print("\nExpense Tracker Menu:")
    print("1. View Expenses")
    print("2. Total Expenses")
    print("3. Exit")

    choice= (input("Enter your choice(1-3) "))
    if choice == "1":
      view_expenses()
    elif choice == "2":
      total_expenses()
    elif choice ==  "3":
      print("Thank you for using the expense tracker. Goodbye!")
      break
    else:
      print("Invalid choice. Please select a valid option.")



  
add_expenses()
main_menu()
total_expenses()
print(expenses)
