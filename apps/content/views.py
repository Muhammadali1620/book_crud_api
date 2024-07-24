from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.content.models import Book
from apps.content.serializers import BookSerializer


class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'book':serializer.data}, status=201)


class BookRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        serializer = BookSerializer(book)
        return Response({"book": serializer.data})

    def patch(self, request, pk):
        saved_book = get_object_or_404(Book.objects.all(), pk=pk)
        data = request.data.get("book")
        serializer = BookSerializer(instance=saved_book, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'book':serializer.data}, status=200)

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response({"message": "Book with id `{}` has been deleted.".format(pk)}, status=204)