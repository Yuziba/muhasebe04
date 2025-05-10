from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

class OnayDefterKayitModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    olurNo = models.CharField(max_length=4)
    olurAciklama = models.CharField(max_length=2500, default='my_default_value')
    olurTarih = models.DateField()  #auto_now_add ile kullanci deger girmese bile otomatik tarih atamasi yapar. defter_onay_list.html icinde ise {{bilgi.onay_tarih|date:"d.m.Y"}} seklinde formatladik
    olurOdemeTutar = models.CharField(max_length=20)
    olurParaBirimi = models.CharField(max_length=20)
    olurOdemeYolu= models.CharField(max_length=20)
    olurSGBBelgeNo = models.CharField(max_length=10)

    def clean(self):
        if not self.olurTarih:
            raise ValidationError({'onayTarih': 'Tarih alanı boş bırakılamaz.'})

    def __str__(self):
        return f"Kullanıcı: {self.username} Belge Numarası: {self.olurNo} Acıklama: {self.olurAciklama} Tarih: {self.olurTarih} Ödemem Tutarı: {self.olurOdemeTutar} Para Birimi: {self.olurParaBirimi} Ödeme Yolu: {self.olurOdemeYolu} SGB Belge No: {self.olurSGBBelgeNo}"

   