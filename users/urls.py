from django.urls import path
from users.views import *

urlpatterns = [
    path('', profile_views,name="profile"),
    path('edit/',profile_edit_view,name="profile-edit"),
    path('onbaording/',profile_edit_view,name="profile-onboarding"),
    path('settings/',profil_settings_view,name="profile-settings"),
    path('emailchange/',profile_emailchange,name="profile-emailchange"),
]