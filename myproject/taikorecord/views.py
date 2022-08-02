from django.shortcuts import render

# Create your views here.
from django.views import generic
from taikorecord.models import Music, Genre, Log
from django.shortcuts import redirect, get_object_or_404
from .form import GenreForm, MusicForm, LogForm
from .form import AccountForm, AddAccountForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'taikorecord/index.html'
    context_object_name = 'music_list'
    
    queryset= Music.objects.all().order_by("diff")
    

def musicdetail(request, pk):
    m = Music.objects.get(pk=pk)
    return render(request, 'taikorecord/detail.html', {'music': m})
    
def registergenre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('taikorecord:registermusic')
    else:
        form = GenreForm()
        return render(request, 'taikorecord/register.html', {'form': form})
    
def registermusic(request):
    if request.method  == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            return redirect('taikorecord:music_detail', pk=m.pk)
    else:
        form = MusicForm()
        return render(request, 'taikorecord/register.html', {'form': form})

def writinglog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('taikorecord:music_detail', pk=l.music.pk)
    else:
        form = LogForm()
        return render(request, 'taikorecord/register.html', {'form': form})
    
def updatelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('taikorecord:music_detail', pk=obj.music.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, 'taikorecord/register.html', {'form': form}) 

def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    music_id = obj.music.pk
    if request.method =="POST": 
        obj.delete() 
        return redirect('taikorecord:music_detail', pk=music_id)
    context = {'obj':obj}
    return render(request, "taikorecord/delete.html", context)

def deletemusic(request, pk):
    obj = get_object_or_404(Music, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('taikorecord:index')
    context = {'obj':obj}
    return render(request, "taikorecord/delete.html", context)

def writingthismusiclog(request, pk):
    obj = get_object_or_404(Music, id=pk)
    form = LogForm({'music':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('taikorecord:music_detail', pk=l.music.pk)
    else:
        return render(request, "taikorecord/register.html", {'form': form})
    
def Login(request):
    # POST
    if request.method == 'POST':
        # フォーム入力のユーザーID・パスワード取得
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        # Djangoの認証機能
        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('taikorecord:home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'taikorecord/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('taikorecord:Login'))


#ホーム
@login_required
def home(request):
    params = {"UserID":request.user,}
    return render(request, "taikorecord/home.html", context=params)


#新規登録
class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        "add_account_form":AddAccountForm(),
        }

    #Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["add_account_form"] = AddAccountForm()
        self.params["AccountCreate"] = False
        return render(request,"taikorecord/createAccount.html",context=self.params)

    #Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)
        self.params["add_account_form"] = AddAccountForm(data=request.POST)

        #フォーム入力の有効検証
        if self.params["account_form"].is_valid() and self.params["add_account_form"].is_valid():
            # アカウント情報をDB保存
            account = self.params["account_form"].save()
            # パスワードをハッシュ化
            account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし
            add_account = self.params["add_account_form"].save(commit=False)
            # AccountForm & AddAccountForm 1vs1 紐付け
            add_account.user = account

            # 画像アップロード有無検証
            if 'account_image' in request.FILES:
                add_account.account_image = request.FILES['account_image']

            # モデル保存
            add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,"taikorecord/createAccount.html",context=self.params)