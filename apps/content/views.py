from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from apps.content.models import Book
from apps.content.serializers import BookSerializer


class BookListCreateAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if request.data['image'] == '':
            del request.data['image']
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=201)


class BookRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        saved_book = get_object_or_404(Book, pk=pk)
        if request.data['image'] == '':
            del request.data['image']
        serializer = BookSerializer(instance=saved_book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, {'error':serializer.errors})

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=204)
