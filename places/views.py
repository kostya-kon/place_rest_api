from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Notice, Author
from .serializers import NoticeSerializer, NoticeSerializer2
from rest_framework.generics import get_object_or_404


class NoticeView(APIView):

    def get(self, request):
        """Получение всех записей Notice"""
        notices = Notice.objects.all()
        serializer = NoticeSerializer(notices, many=True)
        return Response({"notices": serializer.data})

    def post(self, request):
        """Создание заметки про место"""
        notice = request.data.get('notice')
        serializer = NoticeSerializer(data=notice)
        if serializer.is_valid(raise_exception=True):
            notice_saved = serializer.save()
        return Response({"success": "Article '{}' created successfully".format(notice_saved.title)})

    def put(self, request, pk):
        """Обновление заметки про место"""
        saved_notice = get_object_or_404(Notice.objects.all(), pk=pk)
        data = request.data.get('notice')
        serializer = NoticeSerializer(instance=saved_notice, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            notice_saved = serializer.save()
        return Response({
            "success": "Article '{}' updated successfully".format(notice_saved.title)
        })

    def delete(self, request, pk):
        """Удаление заметки про место"""
        notice = get_object_or_404(Notice.objects.all(), pk=pk)
        notice.delete()
        return Response({
            "message": "Article with id `{}` has been deleted.".format(pk)
        }, status=204)


class Notice2View(ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer2

    def perform_create(self, serializer):
        author = get_object_or_404(Author, id=self.request.data.get('author_id'))
        return serializer.save(author=author)


class SingleNotice2View(RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer2
