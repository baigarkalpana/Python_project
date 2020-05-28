#storage and retriving data

books=[]

def add_book(name,author):
    books.append({'name':name,'author':author,'read':False})


def display_books():
    return books

def mark_book_read(name):
    for book in books:
        if(book['name']==name):
            book['read']=True

def delete_book(name):
    global books

    for book in books:
        if(book['name']==name):
            books.remove(book)