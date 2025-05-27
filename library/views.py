from django.shortcuts import render
from library.services import book_service

def book_list(request):
    books = book_service.get_all_books() # 여기에 동작 코드를 작성하세요 (1점)
    return render(request, 'library/book_list.html', {'books': books})

def book_history(request, book_id):
    book = book_service.get_book_by_id(book_id) # 여기에 동작 코드를 작성하세요 (1점)
    histories = book_service.get_borrow_history_for_book(book) # 여기에 동작 코드를 작성하세요 (1점)
    return render(request, 'library/book_history.html', {
        'book': book,
        'histories': histories,
    })