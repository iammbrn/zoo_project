# 🦁 Hayvanat Bahçesi Simülasyonu

## 📌 Proje Hakkında

Bu proje, Python ve FastAPI kullanılarak geliştirilmiş bir **hayvanat bahçesi simülasyonudur**.  
500x500 birimlik sınırlı alanda farklı türden hayvanlar ve bir avcı, **hareket eder, avlanır, çoğalır ve yok olabilir**.  
Simülasyon, hem **terminalde** çalıştırılabilir hem de FastAPI tabanlı bir **web arayüzü** üzerinden görselleştirilebilir.

---

## 🎮 Simülasyon Kuralları

### 🐾 Başlangıçta Alandaki Canlılar:
- 30 Koyun (15 erkek, 15 dişi)
- 10 İnek (5 erkek, 5 dişi)
- 10 Kurt (5 erkek, 5 dişi)
- 8 Aslan (4 erkek, 4 dişi)
- 10 Tavuk
- 10 Horoz
- 1 Avcı

### 🔄 Hareket Kuralları:
- Koyun ve İnek: 2 birim
- Kurt: 3 birim
- Tavuk ve Horoz: 1 birim
- Aslan: 4 birim
- Avcı: 1 birim  
Hayvanlar rastgele yönlere hareket eder; alan dışına çıkamazlar.

### ⚔️ Av Mekaniği:
- **Kurtlar:** 4 birim içindeki koyun, tavuk ve horozları avlayabilir.
- **Aslanlar:** 5 birim içindeki inek ve koyunları avlayabilir.
- **Avcı:** 8 birim içindeki tüm hayvanları avlayabilir.

### 💕 Üreme Kuralları:
- Aynı türden, zıt cinsiyette iki hayvan 3 birim yaklaştığında, rastgele cinsiyette bir yavru oluşur.

### ⏱️ Simülasyon Süresi:
- Toplamda **1000 birimlik hareket** gerçekleştirilir.
- Sonuçta, tüm türlerin popülasyonları konsola yazdırılır.

---

## 🖥️ Uygulama Kullanımı

### ✅ 1. Terminal Uygulaması

`zoo_application.py` dosyasını terminalde çalıştırarak simülasyonu başlatabilir ve sonuçları doğrudan konsolda görebilirsiniz:

```bash
python zoo_application.py


### ✅ 2. Web Servisi

FastAPI tabanlı web servisini çalıştırmak için terminalde aşağıdaki komutu kullanabilirsiniz:

```bash
uvicorn zoo_fastAPI_service:app --reload