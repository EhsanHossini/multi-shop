
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import User, Address
from django.core import validators


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار گذرواژه', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('number',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('number', 'password', 'is_active', 'is_admin')


# def phone_wite_0(value):
#     if value[0] != '0':
#         raise forms.ValidationError("شماره شما باید با صفر شروع بشود")

class FormLogin(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "phone and email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "password"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(username) > 50:
            raise ValidationError(
                '%(value)s شماره شما درست نمی باشد لطف دوباره تلاش کنید',
                code='invalid',
                params={'value': f'{username}'},
            )
        return username

    # def clean(self):
    #     cd = super().clean()
    #     number = cd['number']
    #     if len(number) > 12:
    #         raise ValidationError(
    #             'invalid value: %(value)s is invalid',
    #             code='invalid',
    #             params={'value':f'{number}'},
    #         )
    #     return number


class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = Address
        fields = "__all__"


class OtpLoginForm(forms.Form):
    number = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "phone"}), validators=[validators.MaxLengthValidator(12)])


class CzechOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "code"}), validators=[validators.MaxLengthValidator(4)])


















# from django import forms
#
# from . import models
# from .models import MyUser
# from django.core.exceptions import ValidationError
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.core import validators
#
# #
# # class UserCreationForm(forms.ModelForm):
# #     """A form for creating new users. Includes all the required
# #     fields, plus a repeated password."""
# #
# #     password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
# #     password2 = forms.CharField(
# #         label="تکرار گذرواژه", widget=forms.PasswordInput
# #     )
# #
# #     class Meta:
# #         model = MyUser
# #         fields = ['mobile']
# #
# #     def clean_password2(self):
# #         # Check that the two password entries match
# #         password1 = self.cleaned_data.get("password1")
# #         password2 = self.cleaned_data.get("password2")
# #         if password1 and password2 and password1 != password2:
# #             raise ValidationError("Passwords don't match")
# #         return password2
# #
# # def save(self, commit=True):
# #     # Save the provided password in hashed format
# #     user = super().save(commit=False)
# #     user.set_password(self.cleaned_data["password1"])
# #     if commit:
# #         user.save()
# #     return user
#
#
# # class UserChangeForm(forms.ModelForm):
# #     """A form for updating users. Includes all the fields on
# #     the user, but replaces the password field with admin's
# #     disabled password hash display field.
# #     """
#
#     # password = ReadOnlyPasswordHashField()
#     #
#     # class Meta:
#     #     model = models.MyUser
#         # fields = ["mobile"]
#
# #
# # def start_with_0(vlue):
# #     if vlue[0] != '0':
# #         raise forms.ValidationError("Phone should start with 0")
#
#
# class LoginForm(forms.Form):
#     mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     #
#
#     def clean_mobile(self):
#         mobile = self.cleaned_data.get('mobile')
#         if len(mobile) > 11:
#             raise ValidationError(
#                 'Invalid value: %(value)s is invalid',
#                 code='invalid',
#                 params={'value': f'{mobile}'},
#             )
#         return mobile
#
#
# class OtpLoginForm(forms.Form):
#     mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(11)])
#
#     class Meta:
#         model = models.MyUser
#         fields = ["mobile"]
#
#     def save(self, commit):
#         pass
#
#
# class CheckOtpForm(forms.Form):
#     code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validators.MaxLengthValidator(4)])
#
#
#
