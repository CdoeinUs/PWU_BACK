from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordResetView, PasswordResetConfirmView
)
from dj_rest_auth.registration.views import (
    RegisterView, VerifyEmailView, ConfirmEmailView,
    ResendEmailVerificationView, SocialLoginView
)
from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
from allauth.account.views import EmailVerificationSentView

from Account.views import CustomRegisterView

urlpatterns = [
    # 로그인
    path('login/', LoginView.as_view(), name='rest_login'),
    # 로그아웃
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    # 비밀번호 변경
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    # 비밀번호 초기화
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    # 회원가입
    path('registration/', include('dj_rest_auth.registration.urls')),
    # 가입확인 이메일 발송
    path('registration/account-confirm-email/', EmailVerificationSentView.as_view(),
         name='account_email_verification_sent'),
    # 이메일 인증
    path('registration/account-confirm-email/<str:key>/', AllauthConfirmEmailView.as_view(),
         name='account_confirm_email'),
    # 이메일 재발송
    path('registration/resend-email/', ResendEmailVerificationView.as_view(),
         name='account_email_verification_sent'),
    # social login
    path('registration/', CustomRegisterView.as_view(), name='custom_register'),
    # jwt 토큰 발급
    path('api-token-auth/', obtain_jwt_token),
    # jwt 토큰 갱신
    path('api-token-refresh/', refresh_jwt_token),
    # jwt 토큰 검증
    path('api-token-verify/', verify_jwt_token),
    # swagger
    path('swagger/', TemplateView.as_view(template_name='swagger.html')),
]

# 이메일 인증 이후 redirect url 설정
# settings.py
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/api/accounts/email-verified/'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/api/accounts/email-unverified/'