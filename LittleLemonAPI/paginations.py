from rest_framework import pagination

class MenuItemListPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'perpage'
    max_page_size = 50
    page_query_param = 'page'