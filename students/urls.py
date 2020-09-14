from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from .import views as projectview
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    # path('', projectview.home, name = 'student-home'),
    # path('',student_list , name = 'student_list'),
    # path('<int:id>/details/', student_details, name = 'student_details'),
    # path('<int:id>/edit/', student_edit, name = 'student_edit'),
    # path('add/', student_add, name = 'student_add'),
    # path('<int:id>/delete/', student_delete, name = 'student_delete')





    # FOR LOGIN LOG OUT REGISTER AND PASSWORD RESET
    #
    # url(r'^signup/$', TemplateView.as_view(template_name="signup.html"),
    #     name='signup'),
    # url(r'^email-verification/$',
    #     TemplateView.as_view(template_name="email_verification.html"),
    #     name='email-verification'),
    # url(r'^login/$', TemplateView.as_view(template_name="login.html"),
    #     name='login'),
    # url(r'^logout/$', TemplateView.as_view(template_name="logout.html"),
    #     name='logout'),
    # url(r'^password-reset/$',
    #     TemplateView.as_view(template_name="password_reset.html"),
    #     name='password-reset'),
    # url(r'^password-reset/confirm/$',
    #     TemplateView.as_view(template_name="password_reset_confirm.html"),
    #     name='password-reset-confirm'),
    # url(r'^password-change/$',
    #     TemplateView.as_view(template_name="password_change.html"),
    #     name='password-change'),
    #
    # url(r'^user-details/$',
    #     TemplateView.as_view(template_name="user_details.html"),
    #     name='user-details'),
    #
    # # this url is used to generate email content
    # url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     TemplateView.as_view(template_name="password_reset_confirm.html"),
    #     name='password_reset_confirm'),
    #
    # url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^account/', include('allauth.urls')),

]
