from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| HTML sayfalarını görüntüleme
def index(request):
    return render(request, "appmuhasebe/index.html")



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| Defterlere veri kaydetme
# ------------------------------------------------------------------------ Olur defterine veri kaydetme
def defterolur(request):
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
        print("Form başarıyla kaydedildi.")
        return render(request, 'appmuhasebe/defterolur.html', {"basarili": True})  # İstersen context de ver
    else:
        # GET isteği geldiğinde formu göstermek için:
        return render(request, 'appmuhasebe/defterolur.html')






