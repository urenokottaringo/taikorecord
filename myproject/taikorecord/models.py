from django.db import models
from django.utils import timezone #時間を扱うための道具を持ってくる

# Create your models here.


class Genre(models.Model): #ジャンルの表
    name = models.CharField(max_length=10, verbose_name="ジャンル") 
    def __str__(self):
        return self.name

class Difficulty(models.Model): #難易度の表
    difficulty = models.CharField(max_length=10, verbose_name="難易度")
    def __str__(self):
        return self.difficulty
    
class Music(models.Model): #曲名表をつくる
    title = models.CharField(max_length=100, verbose_name="曲名")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="ジャンル", related_name='music')
    diff = models.ForeignKey(Difficulty, on_delete=models.CASCADE, verbose_name="難易度", related_name='music')
    result_date = models.DateField(verbose_name="日付") #timezoneで日付のデータ
    def __str__(self):            #genreというfieldは「ジャンル表」から紐付けして持ってきますよという宣言
        return self.title         #related_nameに関しては別の回で詳しく説明予定


class Log(models.Model): #Log
    text = models.TextField(verbose_name="メモ") #textというfieldにはたくさん文字列を入力するための場所ですよという宣言
    music = models.ForeignKey(Music, on_delete=models.CASCADE, verbose_name="曲名", related_name='log')
    def __str__(self):            #muiscというfieldは「Musicという表」から紐付けして持ってきますよという宣言
        return self.text          #self.textで管理サイトを使ってデータ入力したときに入力した内容で表示される