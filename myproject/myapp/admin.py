from django.contrib import admin
from myapp.models import Director, Movie, Log    #この部分を追加

admin.site.register(Director)    #もしかするとまとめて登録するやり方があるのかもしれない
admin.site.register(Movie)       #どなたかご教授していただけると助かります
admin.site.register(Log)