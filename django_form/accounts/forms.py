from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

# class formName(forms.ModelForm):
#     class Meta:
#         model =
#         fields =


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model() # 현재 활성화된 user model을 리턴한다
        fields = ('first_name', 'last_name')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # username, password1, password2, email
        model = get_user_model() #바뀐 account user 참조하게 알려주기
        fields = UserCreationForm.Meta.fields + ('email',)