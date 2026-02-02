from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# ListView: Retrieve all books, open to all users with filtering, searching, and ordering
class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books. Supports:
    - Filtering by title, publication_year, or author name (e.g., ?title=Harry, ?publication_year=1997, ?author__name=Rowling).
    - Searching by title or author name via query parameter (e.g., ?search=Harry).
    - Ordering by title or publication_year via query parameter (e.g., ?ordering=title, ?ordering=-publication_year).
    Accessible to all users (read-only).
    """  
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Ensuring that OrderingFilter and SearchFilter are properly used
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]  
    filterset_fields = ['title', 'publication_year', 'author__name']  # Fields for filtering
    search_fields = ['title', 'author__name']  # Fields for searching
    ordering_fields = ['title', 'publication_year']  # Fields for ordering
    ordering = ['title']  # Default ordering (alphabetical by title)

    def get_queryset(self):
        # Custom filter: Return books published on or after the specified year
        queryset = Book.objects.all()
        year = self.request.query_params.get('year', None)
        if year is not None:
            queryset = queryset.filter(publication_year__gte=year)
        return queryset

# DetailView: Retrieve a single book by ID, open to all users
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by its ID. Accessible to all users (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book, restricted to authenticated users
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book instance. Only authenticated users can access this endpoint.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        instance = serializer.save()
        print(f"Book created: {instance.title} by {self.request.user}")

# UpdateView: Modify an existing book, restricted to authenticated users
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book by ID. Only authenticated users can modify books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        if not self.request.data.get('title'):
            raise serializer.ValidationError("Title cannot be empty.")
        instance = serializer.save()
        print(f"Book updated: {instance.title} by {self.request.user}")

# DeleteView: Remove a book, restricted to authenticated users
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book by ID. Only authenticated users can perform this action.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
