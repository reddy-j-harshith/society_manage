from django.urls import path
from members.views import show_all_members, member_detail

urlpatterns = [
    path("all/", show_all_members, name = "show-all-members"),
    path("<int:id>/", member_detail, name = "member-detail"),
]