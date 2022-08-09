from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.contrib.auth import get_user_model

class UserListView(View):

    def get(self, request, *args, **kwargs):
        users_str = ' '
        for user in get_user_model().objects.all():
            users_str += f'| {user.username} |; '

        return HttpResponse(users_str)