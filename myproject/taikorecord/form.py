from django.forms import ModelForm
from taikorecord.models import Difficulty, Music, Genre, Log

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