from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from . import models
from django.contrib.auth.decorators import login_required

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| HTML sayfalarını görüntüleme
def index(request):
    return render(request, "appmuhasebe/index.html")
    


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| Olur Defter
# ------------------------------------------------------------------------ Olur defterine veri kaydetme
def defterolur(request):
    if request.method == "POST":
        olurNo          = request.POST.get("olurNo", "")
        olurAciklama    = request.POST.get("olurAciklama", "")
        olurTarih       = request.POST.get("olurTarih", "")
        olurOdemeTutar  = request.POST.get("olurOdemeTutar", "")
        olurParaBirimi  = request.POST.get("olurParaBirimi", "")
        olurOdemeYolu   = request.POST.get("olurOdemeYolu", "")
        olurSGBBelgeNo  = request.POST.get("olurSGBBelgeNo", "")
        # Bu bilgileri veritabanına kaydet
        models.OnayDefterKayitModel.objects.create(username         = request.user,
                                                   olurNo           = olurNo,
                                                   olurAciklama     = olurAciklama,
                                                   olurTarih        = olurTarih,
                                                   olurOdemeTutar   = olurOdemeTutar,
                                                   olurParaBirimi   = olurParaBirimi,
                                                   olurOdemeYolu    = olurOdemeYolu,
                                                   olurSGBBelgeNo   = olurSGBBelgeNo,)
        # return redirect(reverse('appmuhasebe:defterolur'))
        print("Form başarıyla kaydedildi.")
        #return render(request, 'appmuhasebe/defterolur.html', {"basarili": True})  # İstersen context de ver
        return redirect(reverse('appmuhasebe:defterolur'))
    else:
        # GET isteği geldiğinde formu göstermek için:
        defterolur_goster = models.OnayDefterKayitModel.objects.all()
        return render(request, 'appmuhasebe/defterolur.html', {'defterolur_goster': defterolur_goster})

# ------------------------------------------------------------------------ Olur defterinden kayıt silme
@login_required
def defterolur_delete_view(request, id):
    onay_bilgi = models.OnayDefterKayitModel.objects.get(pk=id)
    if request.user == onay_bilgi.username:                      #kontrol
        models.OnayDefterKayitModel.objects.filter(id=id).delete() #silme kodu
        return redirect('appmuhasebe:defterolur')


# ------------------------------------------------------------------------ Olur defterinde kayıt güncelleme
def defterolur_edit_view(request, id):
    onay_bilgi = get_object_or_404(models.OnayDefterKayitModel, pk=id)
    if request.method == 'POST':
        # POST verilerini al
        olurAciklama = request.POST.get('olurAciklama')
        olurTarih = request.POST.get('olurTarih')
        olurOdemeTutar = request.POST.get('olurOdemeTutar')
        olurParaBirimi = request.POST.get('olurParaBirimi')
        olurOdemeYolu = request.POST.get('olurOdemeYolu')
        olurSGBBelgeNo = request.POST.get('olurSGBBelgeNo')
        # Modeli güncelle
        onay_bilgi.olurAciklama = olurAciklama
        onay_bilgi.olurTarih = olurTarih
        onay_bilgi.olurOdemeTutar = olurOdemeTutar
        onay_bilgi.olurParaBirimi = olurParaBirimi
        onay_bilgi.olurOdemeYolu = olurOdemeYolu
        onay_bilgi.olurSGBBelgeNo = olurSGBBelgeNo
        onay_bilgi.save()
        return redirect('appmuhasebe:defterolur')

    return render(request, 'appmuhasebe/editolur.html', {'onay_bilgi': onay_bilgi})



# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| Ziraat Defter

def defterziraat(request):
    return render(request, "appmuhasebe/defterziraat.html")

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| DemirDuz Defter

def defterdemirduz(request):
    return render(request, "appmuhasebe/defterdemirduz.html")

# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||| DemirYF Defter

def defterdemiryf(request):
    return render(request, "appmuhasebe/defterdemiryf.html")