from flask import Flask, render_template, jsonify
import datetime
import json
import matplotlib.pyplot as plt
from collections import defaultdict
import os
import pandas as pd
from matplotlib.ticker import MaxNLocator



app = Flask(__name__)

# json dosyalarından veri okuma
with open('users.json', 'r', encoding='utf-8') as users_file:
    users_data = json.load(users_file)

with open('simulations.json', 'r', encoding='utf-8') as simulations_file:
    simulations_data = json.load(simulations_file)


# pandas kullanarak şirketlerin toplam kullanıcı sayılarını bulma
def process_company_users():
    users_df = pd.DataFrame(users_data['users'])
    simulations_df = pd.DataFrame(simulations_data['simulations'])

    
    users_df = users_df.drop_duplicates()
    simulations_df = simulations_df.drop_duplicates()

    # iki json dosyası yalnızca simulation_id ortaklığı taşıdığı için o bilgi üzerinden birleştirme
    merged_df = pd.merge(users_df, simulations_df, on='simulation_id', how='inner')

    # company id ve name aynı şirketler için aynı olduğundan ötürü user_id'lerin onlara göre unique gruplaması
    # nunique olmasının sebebi toplam kullanıcı girişi sayısını değil toplam kullanıcı sayısını istiyor olmamız
    company_users_df = merged_df.groupby(['company_id', 'company_name'])['user_id'].nunique().reset_index()
    company_users_df.columns = ['Şirket ID', 'Şirket Adı', 'Toplam Kullanıcı Sayısı']
    
    return company_users_df.to_html(index=False)

# kullanıcı verileri üzerinden iterate ederek günlere göre kullanıcı sayısını çıkarma
def process_daily_users_graph():
    daily_users = defaultdict(int)
    for user in users_data['users']:
        
        # unix epoch time formatında verilen zamanları YYYY-MM-DD formatına çevirme
        timestamp= user['signup_datetime']
        
        # aaaaa.bbbbbb... şeklinde verilen epoch time'ı noktayı kaldırıp ilk 10 haneyi alarak aaaaabbbbb şeklinde çevirdim
        # birkaç farklı çevirme yolu denedim ancak en mantıklı tarihleri veren yukarıdaki yol olduğu için onu baz aldım
        fraction_removed = str(timestamp).replace('.', '')
        formatted_epoch = int(fraction_removed[:10])
        date_string=(datetime.datetime.fromtimestamp(formatted_epoch).isoformat())
        
        # tarih formatlama
        datetime_obj = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')
        year_month_day = datetime_obj.strftime('%Y-%m-%d')
   
        daily_users[year_month_day] += 1
        
    
    # grafikte anlamlı görünmesi için küçükten büyüğe tarihlere göre sıralama    
    sorted_dates = dict(sorted(daily_users.items(), key=lambda item: item[0]))
    
    dates = list(sorted_dates.keys())
    values = list(sorted_dates.values())


    # grafik oluşturma
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, color='blue', marker='o', linestyle='-', linewidth=2, markersize=5)
    plt.xlabel('Tarih', fontsize=12, fontweight='bold', color='darkgray')
    plt.ylabel('Günlük Kullanıcı', fontsize=12, fontweight='bold', color='darkgray')
    plt.title("Ludi'nin Günlük Kullanıcı Sayısındaki Değişim", fontsize=14, fontweight='bold')
    
    # bütün tarihleri koyunca karmaşık görüneceği için yalnızca 20 tanesini koydum
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(MaxNLocator(20)) 
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend(['Günlük Kullanıcı'], loc='upper left')
    plt.tight_layout()
    
    # grafiğin dosya yolunu kaydederek fonksiyondan döndürme
    graph_path = 'static/daily_users_graph.png'
    plt.close()

    return graph_path


# Flask üzerinde uygulama çalıştırma
# HTML kodunda table ve graph olarak alınan kaynaklar yukarıdaki fonksiyonların çıktıları 
@app.route('/')
def index():
    return render_template('index.html', table=process_company_users(), graph=process_daily_users_graph())

if __name__ == '__main__':
      app.run(debug=True, use_reloader=False)