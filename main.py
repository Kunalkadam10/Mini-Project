# Add task
# view task
# del task
# clear all task

def add():
    a = input("Enter task : " )
    task = a + "\n"
    with open ("TODO" , 'a') as f:
        f.write(task)
    print(f"New Task : {a}")

def view():
    with open("TODO" , 'r') as f:
        content = f.readlines()
        print("---TASK---")

        if not content:
           print("No task found!")
        else:
           for i,a in enumerate(content,start = 1):
              print(f"{i}.{a.strip()}")       

def delete():
    with open("TODO" , 'r') as f:
        line = f.readlines()
    if len(line) == 0:
       print("No task to delete ")
       return
    
    for i in range(len(line)):
       print(f"{i+1}. {line[i].strip()}")

    try:
       b = int(input("enter task no to delete :"))    
    except ValueError:
       print("Invalid input! Please enter a number.")
       return

    c = b-1

    if 0 <= c < len(line):
       line.pop(c)
       with open("TODO" , 'w') as f:
          f.writelines(line)
    else:
       print("Enter valid option")
       
def clear():
  with open("TODO" , 'w') as f:
     print("All task cleared!")

def show():     
    print("---- TODO LIST----")
    print('1)Add task')
    print('2)view task')
    print('3)del task')
    print('4)clear all task')
    print('5)Exit') 

def main():
    while True:
        show()
        try:
            choice = int(input("Enter your choice : "))

            if choice == 1:
              add()

            elif choice == 2:
              view()

            elif choice == 3:
              delete()

            elif choice == 4:
              clear()
            elif choice ==5:
              print("Goodbye")
              break
            else:
              print("enter valid option")

        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
   main()


