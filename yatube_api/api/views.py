from rest_framework import viewsets, permissions, filters, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from posts.models import User, Post, Group, Follow
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post)

    # а можно короче так как для модели коммент нужен только id:
    # def perform_create(self, serializer):
    #     post_id = self.kwargs.get('post_id')
    #     serializer.save(author=self.request.user, post_id=post_id)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого комментария запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого комментария запрещено!')
        instance.delete()


class CreateRetrieveListViewSet(
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.ListModelMixin,
        viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateRetrieveListViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return Follow.objects.filter(user=user)

# ЭТО Я ИЗВРАЩАЛСЯ В НАЧАЛАЕ ЧЕРЕЗ ViewSet
# class FollowViewSet(viewsets.ViewSet): 
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('=following__username',)

#     def list(self, request):
#         queryset = Follow.objects.filter(user=self.request.user)
#         serializer = FollowSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = FollowSerializer(data=request.data)
#         user = self.request.user
#         follow_obj = serializer.initial_data.get('following')
#         if user.username == follow_obj:
#             raise PermissionDenied('Невозможно подписаться на самого себя')
#         elif Follow.objects.filter(
#             user=user,
#             following__username=follow_obj # или как на след строке
#             # following=User.objects.get(username=follow_obj) или так, но так ругается почему-то pytest, хотя работает
#         ).exists():
#             raise PermissionDenied('Вы уже подписаны')
#         elif serializer.is_valid():
#             serializer.save(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def destroy(self, request, pk=None): САМ НАПИСАЛ РАДИ ФАНА, НО КОРЯВО, ТАК КАК УДАЛЯЕТ ПО following, НА ПО PK
#     #     serializer = FollowSerializer(data=request.data)
#     #     follow_obj = serializer.initial_data.get('following')
#     #     queryset = Follow.objects.filter(user=self.request.user, following__username=follow_obj)
#     #     queryset.delete()
#     #     return Response(status=status.HTTP_201_CREATED)