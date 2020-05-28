'''

      Author:Kalpana Baigar

      This project is based on storing books into a list,it uses following functionalities:
      add books into a list
      displaying all books
      mark a book as read-'YES' if we finished reading
      delete books
'''


from util import database

User_Choice='''
 -a to add into a list
 -l to list all data
 -r to mark a book as read
 -d to remove data
 -q quit data 
 your choice:'''


def menu():
     user_input=input(User_Choice)
     while user_input!= 'q':
          if user_input =='a':
               promt_add_book()
          elif user_input =='l':
               list_book()
          elif user_input =='r':
               prompt_read_book()
          elif user_input =='d':
               prompt_delete_book()
          else:
               print("Invalid Input...")

          user_input = input(User_Choice)


def promt_add_book():
     name=input("enter new book name:")
     author=input("enter author of new book:")
     database.add_book(name,author)


def list_book():

     for i in database.display_books():
          if i['read']:
               read='YES'
          else:
               read='NO'
          print(f"{i['name']} by {i['author']} - Read:{read}")

          #read = 'YES' if book['read'] else 'NO'


def prompt_read_book():
    name=input("Enter name of book you just finished Reading...")
    database.mark_book_read(name)


def prompt_delete_book():
     name = input("Enter name of book you just finished Reading...")
     database.delete_book(name)


menu()




