'''
Users Accounts form and fields
developer: #ABS
'''

# Import all requirements
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, ReadOnlyPasswordHashField, AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate, login as DjangoLogin
from django.contrib.auth.forms import UsernameField
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from wagtail.users.forms import UserEditForm, UserCreationForm
from allauth.account.forms import SignupForm , ChangePasswordForm
from .models import CustomUser
from .utils import validate_Opassword
  
   
# Custom User Creation Form class
class CustomUserCreationForm(SignupForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تایید رمز عبور', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('email','password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, request):
        user = super().save(request)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


# Custom User authentication Form class
class LoginForm(AuthenticationForm):
    username = UsernameField(label='نام کاربری/ایمیل :')


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            # Check if user exists with username or email
            try:
                user = CustomUser.objects.get(
                    Q(username=username) | Q(email=username)
                )
            except CustomUser.DoesNotExist:
                raise forms.ValidationError('Invalid username or email')

            userDet = CustomUser.objects.get(Q(username=username) | Q(email=username))
            if userDet.has_new_password:
                auth = authenticate(request=self.request, username=username, password=password)
                if not auth:
                    raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است')
                elif auth:
                    self.confirm_login_allowed(auth)
                    DjangoLogin(self.request, auth)
                    
            else:
                WOPass = userDet.WPOPass
                is_valid_password = validate_Opassword(password, userDet.WPOPass)
                if is_valid_password:
                    userDet.has_new_password = True
                    new_password_hash = make_password(password, salt='PDHTwqLLv7nIsw60zr767s')
                    userDet.password = new_password_hash
                    userDet.save(update_fields=['password', 'has_new_password'])
                    user = authenticate(request=self.request, username=username, password=password)
                    self.confirm_login_allowed(user)
                    DjangoLogin(self.request, user)
                else:
                    raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است')
            # Check if password is valid
            if not user.check_password(password):
                raise forms.ValidationError('نام کاربری یا رمز عبور اشتباه است')



        return self.cleaned_data




# Custom User Change Form
class CustomUserChangeForm(UserEditForm):
    email = forms.EmailField(label='Email')
    username = UsernameField(label='Username')
    full_name = forms.CharField(label='Full Name')
    is_active = forms.BooleanField(label='Active', required=False)
    is_staff = forms.BooleanField(label='Staff', required=False)
    date_joined = forms.DateTimeField(label='Date Joined', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'full_name', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]
    

# Custom User Password Change Form
class CustomPasswordChangeForm(ChangePasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput,
        strip=False,
        required=False,
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput,
        required=False,
    )

    class Meta:
        model = CustomUser

    def clean(self):
        cleaned_data = super().clean()

        # Check if user is new and requires a strong password
        if self.user.password == '':
            new_password1 = cleaned_data.get('new_password1')
            new_password2 = cleaned_data.get('new_password2')
            if not new_password1:
                raise forms.ValidationError(
                    _("You must enter a new password.")
                )
            if not validate_password(new_password1):
                raise forms.ValidationError(
                    _("Your password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
                )
            if new_password1 != new_password2:
                raise forms.ValidationError(
                    _("The two password fields didn't match.")
                )
        else:
            # Check if user only needs to confirm their current password
            old_password = cleaned_data.get('old_password')
            if not self.user.check_password(old_password):
                raise forms.ValidationError(
                    _("Your old password was entered incorrectly. Please enter it again.")
                )

            new_password1 = cleaned_data.get('new_password1')
            new_password2 = cleaned_data.get('new_password2')
            if new_password1 or new_password2:
                raise forms.ValidationError(
                    _("You can only change your password if you enter your current password correctly.")
                )

        return cleaned_data
