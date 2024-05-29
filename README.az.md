# umico.az Scraper

Bu, Azərbaycanın ən populyar onlayn alış-veriş saytlarından biri olan umico.az-dan məhsul məlumatlarını çıxarmaq üçün hazırlanmış Python veb-sayt tarayıcısıdır.

## Xüsusiyyətlər

- Ad, qiymət, satıcı, şəkil url və məhsul url daxil olmaqla avtomobil təfərrüatlarını çıxarır.
- Məlumatlar CSV formatında saxlanılır.
- Veb-saytın HTML etiketlərində dəyişiklik ola biləcəyindən kod yenilənməsi tələb oluna bilər.
- Veb-skripinq üçün Requests və Beautiful Soup kitabxanaları istifadə olunmuşdur.

## Quraşdırılma

1. Bu repozitorini klon edin.
2. Terminalınızda `pip install -r requirements.txt` əmrini işlədərək lazımi tələbatları yükleyin.

## Pypi Üzerində Quraşdırılma

umico2csv-ni pip vasitəsilə quraşdıra bilərsiniz:

```bash
pip install umico2csv
```

## İstifadə

```python
from umico2csv import Scraper

scraper = Scraper()

scraper.scrape(output_file='umico.csv', start=1)

```

## Feragat

Bu tətbiq etmə, təhsil məqsədləri üçün nəzərdə tutulmuşdur və ticari məqsədlər üçün istifadə edilməməlidir. Müəllif, bu alətin səhv istifadəsinin yaradabilecəyi hüquqi məsələlərdən məsuliyyəti daşımayacaq.

## Lisenziya

Bu layihə MIT Lisenziyası ilə lisenziyalanmışdır - ətraflı məlumat üçün LICENSE faylını baxın.