# Ludi İş Simülasyonu Web Paneli

Bu proje, Ludi iş simülasyonu platformu vaka çalışması için yapılmıştır. `users.json` ve `simulations.json` dosyalarındaki verilerle Python ve Flask kullanılarak oluşturulan bir web panelini içerir.

## İçerik
1. **Her Şirketin Toplam Kullanıcı Sayısını Gösteren Bir Tablo**
2. **Ludi'deki Toplam Kullanıcı Sayısının Günlük Gelişimini Gösteren Bir Grafik**

## Dosya ve Klasörler
- **static:** CSS kodu ve fonksiyon tarafından oluşturulan, analiz edilmiş verinin grafik görseli
- **templates:** HTML kodu
- **app.py:** pandas kullanılarak veri analizinin yapıldığı, grafiğin oluşturulduğu ve Flask kodunu içeren dosya

## Notlar
1. Verilen vakada basit bir panel tasarlamamız istendiği için projenin görselliği basit seviyede tutuldu.
2. Unix epoch timestamp formatında verildiğini düşündüğüm zamanları çeşitli şekillerde YYYY-AA-GG formatına çevirmeyi denedim, veriler rastgele olduğu için sanıyorum, en makul tarihleri (yaklaşık 2100 yılı civarları) küsuratı belirttiğini düşündüğüm noktayı kaldırıp ilk 10 haneyi çevirerek elde edebildim. Dolayısıyla projede bu formülle elde edilen tarihler kullanıldı.
3. Üst tablodaki şirket sıralaması için özel bir tarif verilmediğinden ötürü sıralama ID numaralarına göre yapıldı.
4. Python kodu içinde ayrıca açıklamalar yer almakta, CSS ve HTML dosyaları kısa ve Python dosyasına göre daha basit yapıda oldukları için onlara yorum eklenmedi.
