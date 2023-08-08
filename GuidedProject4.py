#Step 1: The show_todo_list Function
def show_todo_list():
    i=1
    f = open('todo.txt', 'r')
    for line in f:
        if line == "":
            print("Nothing in the list!")
        print('  * (' + str(i) + ') ' + line.strip())
        i+=1

#Step 2: The add_to_todo_list Function
def add_to_todo_list(item):
    f = open('todo.txt', 'a')
    f.write(item+'\n')
    f.close()

#Step 3: The remove_from_todo_list Function
def remove_from_todo_list(number):
    f = open('todo.txt', 'r+')
    data = f.readlines()
    data.pop(number - 1)  
    f.seek(0)
    f.writelines(data)
    f.truncate()  # Dosyanın kalan kısmını sil
    f.close()

#Last Step: Main Function
def main():
    #It handles the command loop logic, and calls the other functions when necessary.
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

main()