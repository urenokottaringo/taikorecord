from django.contrib import admin
from taikorecord.models import Genre, Difficulty, Music, Log    #この部分を追加
from .models import Account

admin.site.register(Account)
admin.site.register(Genre)    #もしかするとまとめて登録するやり方があるのかもしれない
admin.site.register(Difficulty)
admin.site.register(Music)       #どなたかご教授していただけると助かります
admin.site.register(Log)
# Register your models here.
