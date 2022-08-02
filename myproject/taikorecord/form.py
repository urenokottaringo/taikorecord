
from django.forms import ModelForm
from taikorecord.models import Difficulty, Music, Genre, Log
from django import forms
from django.contrib.auth.models import User
from .models import Account

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)

class MusicForm(ModelForm):
    class Meta:
        model = Music
        fields = ('title', 'genre', 'diff', 'result_date',)

class DifficultyForm(ModelForm):
    class Meta:
        model = Difficulty
        fields = ('difficulty',)
        
class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('music','text')

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name','account_image',)
        labels = {'last_name':"苗字",'first_name':"名前",'account_image':"写真アップロード",}