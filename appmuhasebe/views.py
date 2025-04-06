from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| HTML sayfalarını görüntüleme
def index(request):
    return render(request, "appmuhasebe/index.html")

def defterolur(request):
    return render(request, "appmuhasebe/defterolur.html")





# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| Defterlere veri kaydetme
# ------------------------------------------------------------------------ Olur defterine veri kaydetme
def kayitOlurDefterView(request):
    if request.method == "POST":
        olurNo          = request.POST.get("olurNo", "")
        olurAciklama    = request.POST.get("olurAciklama", "")
        olurTarih       = request.POST.get("olurTarih", "")
        olurOdemeTutar  = request.POST.get("olurOdemeTutar", "")
        olurParaBirimi  = request.POST.get("olurParaBirimi", "")
        # Bu bilgileri veritabanına kaydet
        models.OnayDefterKayitModel.objects.create(username         = request.user,
                                                   olurNo           = olurNo,
                                                   olurAciklama     = olurAciklama,
                                                   olurTarih        = olurTarih,
                                                   olurOdemeTutar   = olurOdemeTutar,
                                                   olurParaBirimi   = olurParaBirimi,)
        # return redirect(reverse('appmuhasebe:defterolur'))
        response = HttpResponse('<script>window.close(); window.opener.location.reload();</script>') #kayit butonuna tiklandiktan sonra pencere kapatma islemi ve yenileme
        return response
    else:
        return render(request, 'appmuhasebe/index.html')







