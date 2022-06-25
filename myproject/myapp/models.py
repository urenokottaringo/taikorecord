from django.db import models #表をつくるための道具を持ってくる
from django.utils import timezone #時間を扱うための道具を持ってくる


class Director(models.Model): #Directorという表を作る
    name = models.CharField(max_length=100, verbose_name="監督") #nameというfieldに文字列で監督名を入れる宣言
    def __str__(self): #以下2行は管理サイト使ってデータ入力したときに監督の名前で表示するための関数
        return self.name


class Movie(models.Model): #Movieという表をつくる
    title = models.CharField(max_length=100, verbose_name="タイトル")
    watch_date = models.DateField() #timezoneという道具を持ってきたので、日付のデータを入力できる
    director = models.ForeignKey(Director, on_delete=models.CASCADE, verbose_name="監督", related_name='movie')
    def __str__(self):            #directorっていうfieldは「Directorという表」から紐付けして持ってきますよという宣言
        return self.title         #related_nameに関しては別の回で詳しく説明予定


class Log(models.Model): #Logという表をつくる
    text = models.TextField() #textというfieldにはたくさん文字列を入力するための場所ですよという宣言
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="タイトル", related_name='log')
    def __str__(self):            #movieっていうfieldは「Movieという表」から紐付けして持ってきますよという宣言
        return self.text          #self.textで管理サイトを使ってデータ入力したときに入力した内容で表示される
