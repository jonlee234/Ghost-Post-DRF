from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer
from django.db.models import F
from rest_framework.decorators import action

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-post_date")
    serializer_class = PostSerializer

    @action(detail=True, methods=["put"], name="Upvote")
    def upvote(self, request, pk=None):
        post = self.get_object()
        Post.objects.filter(id=pk).update(upvotes=F("upvotes") + 1)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=True, methods=["put"], name="Downvote")
    def downvote(self, request, pk=None):
        post = self.get_object()
        Post.objects.filter(id=pk).update(downvotes=F("downvotes") + 1)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False)
    def most_voted(self, request):
        most_voted = Post.objects.annotate(
            fieldsum=F("upvotes") - F("downvotes")
        ).order_by("-fieldsum")

        page = self.paginate_queryset(most_voted)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(most_voted, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def all_roasts(self, request):
        all_roasts = Post.objects.filter(post_type="Roast")

        page = self.paginate_queryset(all_roasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_roasts, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def all_boasts(self, request):
        all_boasts = Post.objects.filter(post_type="Boast")

        page = self.paginate_queryset(all_boasts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(all_boasts, many=True)
        return Response(serializer.data)
