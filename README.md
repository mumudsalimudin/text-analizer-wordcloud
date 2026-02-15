# Text Analyzer (Advanced)

Program Python untuk menganalisis teks: membersihkan kata, menghapus stopwords (ID/EN dasar), menghitung frekuensi kata,
menampilkan peringkat kata teratas, menyimpan hasil ke file, dan menghasilkan visualisasi word cloud.

## Fitur
- Text cleaning & tokenization
- Stopwords removal (Indonesian + English basic list)
- Word frequency ranking (Top-N)
- Export ranking to a text file
- Word cloud visualization

## Prasyarat
- Python 3.10+ (disarankan)
- Dependensi: `wordcloud`, `matplotlib`

## Instalasi
```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Cara Menjalankan

**1) Input via terminal (interactive):**
```
python src/text_analyzer.py
```

**2) Input dari file (recommended untuk teks panjang):**
```
python src/text_analyzer.py --file data/sample_input.txt
```

**3) Ubah jumlah Top-N:**
```
python src/text_analyzer.py --file data/sample_input.txt --top 25
```

**4) Tanpa visualisasi (misalnya di server/CI):**
```
python src/text_analyzer.py --file data/sample_input.txt --no-viz
```

## Output
- Ringkasan di terminal:
  - jumlah karakter (termasuk spasi)
  - jumlah kata setelah cleaning & stopwords removal
  - Top-N kata dengan frekuensi tertinggi
- File output (default):
  - `outputs/word_frequency_top.txt`
- Visualisasi:
  - Jendela word cloud (matplotlib)

## Struktur Proyek
```
text-analyzer/
├─ src/
│  └─ text_analyzer.py
├─ data/
│  └─ sample_input.txt
├─ outputs/               # hasil run (di-ignore oleh git)
├─ tests/                 # (opsional)
├─ .gitignore
├─ README.md
└─ requirements.txt
```

## Kustomisasi
- Tambah/ubah stopwords: edit `DEFAULT_STOPWORDS` di `src/text_analyzer.py`
- Ubah lokasi output: gunakan argumen `--output outputs/nama_file.txt`
- Perluas analisis: tambah fitur (mis. n-grams, stemming, TF-IDF)

## Lisensi

GNU GENERAL PUBLIC LICENSE
