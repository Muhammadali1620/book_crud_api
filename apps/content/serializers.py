from rest_framework import serializers

from apps.content.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author_full_name', 'description', 'image', 'price')

{
"title": "qichchu kitob",
"author_full_name": "Abdulla Qodiriy",
"description": "yomon zo'r kitob lekin",
"price": 20000
}
