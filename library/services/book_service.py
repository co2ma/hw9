from library.models import Book, BorrowHistory
from django.shortcuts import get_object_or_404

def get_all_books():
    return Book.objects.all() # 여기에 동작 코드를 작성하세요 (1점)
def get_book_by_id(book_id: int) -> Book:
    return get_object_or_404(Book, pk=book_id) # 여기에 동작 코드를 작성하세요 (1점)
def get_borrow_history_for_book(book: Book):
    return BorrowHistory.objects.filter(book=book).order_by('-borrowed_at') # 여기에 동작 코드를 작성하세요 (1점) 