[README.md](https://github.com/user-attachments/files/28462277/README.md)
# Persian Text-to-Speech with Piper 🎙️

## English

An offline Persian (Farsi) Text-to-Speech application powered by Piper.

### Features
- ✅ Fully offline
- ✅ Persian language support
- ✅ Fast speech generation
- ✅ Lightweight and easy to use
- ✅ Generates WAV audio files

### Requirements
- Python 3.8+
- Piper
- Persian Piper model (`fa_IR-amir-medium`)

### Project Structure

```text
project/
├── piper/
│   └── piper.exe
├── models/
│   ├── fa_IR-amir-medium.onnx
│   └── fa_IR-amir-medium.onnx.json
├── main.py
└── output.wav
```

### Installation

1. Download Piper.
2. Download a Persian model.
3. Place the files in the folders shown above.
4. Run:

```bash
python main.py
```

### Usage

When prompted, enter Persian text:

```text
سلام دنیا
```

The program will generate and play the audio automatically.

---

## فارسی

یک برنامه تبدیل متن فارسی به گفتار به صورت آفلاین با استفاده از Piper.

### ویژگی‌ها
- ✅ کاملاً آفلاین
- ✅ پشتیبانی از زبان فارسی
- ✅ تولید سریع صدا
- ✅ سبک و ساده
- ✅ تولید فایل صوتی WAV

### پیش‌نیازها
- Python 3.8 یا بالاتر
- Piper
- مدل فارسی `fa_IR-amir-medium`

### ساختار پروژه

```text
project/
├── piper/
│   └── piper.exe
├── models/
│   ├── fa_IR-amir-medium.onnx
│   └── fa_IR-amir-medium.onnx.json
├── main.py
└── output.wav
```

### نصب

1. Piper را دانلود کنید.
2. مدل فارسی را دانلود کنید.
3. فایل‌ها را در پوشه‌های مناسب قرار دهید.
4. دستور زیر را اجرا کنید:

```bash
python main.py
```

### نحوه استفاده

پس از اجرای برنامه، متن فارسی موردنظر را وارد کنید:

```text
سلام دنیا
```

برنامه فایل صوتی را تولید کرده و به صورت خودکار پخش می‌کند.

---

## License

MIT License

---

Made with ❤️ using Piper
