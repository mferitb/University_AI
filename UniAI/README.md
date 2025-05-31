# Üniversite Asistanı

Bu proje, üniversite öğrencileri için yapay zeka destekli bir asistan uygulamasıdır. Öğrencilere yemek menüsü, akademik takvim ve diğer üniversite bilgileri hakkında sorular sorma imkanı sunar.

## Özellikler

- 🤖 Yapay zeka destekli sohbet arayüzü
- 📅 Akademik takvim bilgileri
- 🍽️ Günlük yemek menüsü
- 💬 Doğal dil işleme ile soru-cevap
- 🌐 Modern ve kullanıcı dostu arayüz

## Teknolojiler

- Backend:
  - Python 3.11+
  - Flask
  - LangChain
  - Google Vertex AI (Gemini)
  - FAISS (Vector Store)
  - HuggingFace Embeddings

- Frontend:
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  - Marked.js (Markdown desteği)

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/uni-ai.git
cd uni-ai
```

2. Python sanal ortamı oluşturun ve aktifleştirin:
```bash
python -m venv venv
# Windows için:
venv\Scripts\activate
# Linux/Mac için:
source venv/bin/activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Google Cloud ayarları:
   - [Google Cloud Console](https://console.cloud.google.com)'a gidin
   - Yeni bir proje oluşturun
   - Vertex AI API'yi etkinleştirin
   - Servis hesabı oluşturun ve JSON formatında anahtar indirin
   - İndirdiğiniz JSON dosyasını `keys` klasörüne `your-credentials-file.json` olarak kaydedin

5. Çevre değişkenlerini ayarlayın:
   - `.env.example` dosyasını `.env` olarak kopyalayın
   - `.env` dosyasını düzenleyerek kendi Google Cloud proje bilgilerinizi ekleyin:
     ```
     GOOGLE_CLOUD_PROJECT=your-project-id
     GOOGLE_APPLICATION_CREDENTIALS=keys/your-credentials-file.json
     ```

6. Veri dosyalarını hazırlayın:
   - `docs` klasöründe gerekli JSON dosyalarını oluşturun:
     - `yemeks.json`: Yemek menüsü bilgileri
     - `akademik_takvim.json`: Akademik takvim bilgileri

## Çalıştırma

1. Flask uygulamasını başlatın:
```bash
python app.py
```

2. Tarayıcınızda `http://localhost:8080` adresine gidin

## Proje Yapısı

```
uni-ai/
├── app.py              # Ana Flask uygulaması
├── requirements.txt    # Python bağımlılıkları
├── .env               # Çevre değişkenleri (git'e eklenmez)
├── .env.example       # Örnek çevre değişkenleri
├── keys/              # API anahtarları (git'e eklenmez)
│   └── your-credentials-file.json
├── docs/              # Veri dosyaları
│   ├── yemeks.json
│   └── akademik_takvim.json
└── View/              # Frontend dosyaları
    ├── index.html
    ├── style.css
    └── script.js
```

## Güvenlik Notları

- `.env` dosyasını asla GitHub'a pushlamayın
- API anahtarlarınızı ve kimlik bilgilerinizi güvende tutun
- `keys` klasörünü `.gitignore` dosyasına ekleyin
- Üretim ortamında güvenli bir şekilde anahtarları yönetin

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir özellik dalı oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Dalınıza push yapın (`git push origin feature/amazing-feature`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## İletişim

Proje Sahibi - [@github_username](https://github.com/github_username)

Proje Linki: [https://github.com/github_username/uni-ai](https://github.com/github_username/uni-ai) 