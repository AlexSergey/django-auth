from django.conf.urls import url
from views import Authorization, Register, Logout

urlpatterns = [
    url(r'^authorization/', Authorization.as_view(), name="authorization"),
    url(r'^logout/', Logout.as_view(), {'next_page': '/accounts/authorization/'}),
    url(r'^registration/', Register.as_view(), name="registration"),
]