Bu proje Ludi iş simülasyonu platformu vaka çalışması için yapılmıştır.

users.json ve simulations.json dosyalarında yer alan verilerle, Python ve Flask kullanılarak oluşturulan bir web paneli. 

İÇERİK
Her şirketin (company) toplam kullanıcı sayısını gösteren bir tablo
Ludi’deki toplam kullanıcı sayısının gelişimini günlük olarak gösteren bir grafik

static: CSS kodu ve fonksiyon tarafından oluşturulan, analiz edilmiş verinin grafik görseli
templates: HTML kodu
app.py: pandas kullanılarak veri analizinin yapıldığı, grafiğin oluşturulduğu ve Flask kodunu içeren dosya

NOTLAR: 
    1- Verilen vakada basit bir panel tasarlamamız istendiği için proje boyunca görselliği basit tuttum.
    2- Unix epoch timestamp formatında verildiğini düşündüğüm zamanları çeşitli şekillerde YYYY-AA-GG formatına çevirmeyi denedim, veriler rastgele olduğu için sanıyorum, en makul tarihleri (yaklaşık 2100 yılı civarları) küsuratı belirttiğini düşündüğüm noktayı kaldırıp ilk 10 haneyi çevirerek elde edebildim. Dolayısıyla projede bu formülle elde edilen tarihler kullanıldı.
    3- Üst tablodaki şirket sıralaması için özel bir tarif verilmediğinden ötürü sıralamayı ID numaralarına göre yaptım.
    4- Python kodu içinde ayrıca açıklamalar yer alıyor, CSS ve HTML dosyaları kısa ve Python dosyasına göre daha basit oldukları için onlara yorum bırakmadım.


Alperen Kars


