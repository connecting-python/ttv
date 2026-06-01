import subprocess
import os
import winsound

# --- تنظیم مسیرها ---
# اگر piper.exe در همین پوشه است، کافیست نام آن را بنویسید
PIPER_EXE = r"piper/piper.exe"

# اگر مدل‌ها در پوشه 'models' در همین پوشه هستند
MODEL_ONNX = r"models/fa_IR-amir-medium.onnx"
MODEL_JSON = r"models/fa_IR-amir-medium.onnx.json" # پایتون به این فایل JSON برای تنظیمات مدل نیاز دارد

# فایل صوتی خروجی
OUTPUT_WAV = "output.wav"

def speak_farsi(text_to_speak):
    """
    تبدیل متن فارسی به صدا با استفاده از Piper و پخش آن.
    """
    print(f"تبدیل متن به صدا: '{text_to_speak[:30]}...'") # نمایش بخشی از متن
    
    # دستور اجرای Piper
    # ما مدل .onnx را به عنوان مدل اصلی معرفی می‌کنیم
    # piper.exe خودش فایل .json مربوطه را پیدا می‌کند اگر در همان پوشه باشد
    command = [
        PIPER_EXE,
        "--model", MODEL_ONNX,
        "--output_file", OUTPUT_WAV
    ]
    
    try:
        # اجرای Piper و ارسال متن به آن
        # encoding='utf-8' برای پشتیبانی از زبان فارسی ضروری است
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, # خروجی piper را هم می‌گیریم برای خطا یابی احتمالی
            stderr=subprocess.PIPE, # خطاهای piper را هم می‌گیریم
            encoding="utf-8"
        )
        
        # ارسال متن به stdin برنامه piper
        stdout, stderr = process.communicate(input=text_to_speak)
        
        # بررسی خطاها
        if process.returncode != 0:
            print(f"خطا در اجرای Piper (کد خطا: {process.returncode}):")
            print(stderr) # نمایش خطاهای piper
            return # خروج از تابع در صورت بروز خطا

        # بررسی وجود فایل صوتی
        if os.path.exists(OUTPUT_WAV):
            print("تولید صدا موفقیت‌آمیز بود. در حال پخش...")
            # پخش فایل صوتی با winsound
            # SND_FILENAME یعنی فایل را به عنوان نام فایل صدا در نظر بگیر
            # SND_ASYNC یعنی پخش صدا به صورت ناهمزمان باشد (برنامه منتظر تمام شدن صدا نماند)
            winsound.PlaySound(OUTPUT_WAV, winsound.SND_FILENAME | winsound.SND_ASYNC)
            print("پخش صدا آغاز شد.")
        else:
            print(f"خطا: فایل صوتی '{OUTPUT_WAV}' تولید نشد.")
            if stdout:
                print("خروجی استاندارد Piper:", stdout)

    except FileNotFoundError:
        print(f"خطا: فایل اجرایی Piper پیدا نشد. لطفاً مسیر '{PIPER_EXE}' را بررسی کنید.")
    except Exception as e:
        print(f"یک خطای غیرمنتظره رخ داد: {e}")

# --- بخش اصلی برنامه ---
if __name__ == "__main__":
    print("--- مبدل متن فارسی به صدا (آفلاین با Piper) ---")
    
    # بررسی اولیه وجود فایل‌های ضروری
    if not os.path.exists(PIPER_EXE):
        print(f"خطا: فایل '{PIPER_EXE}' پیدا نشد. لطفاً مسیر آن را در کد بررسی کنید.")
    elif not os.path.exists(MODEL_ONNX):
         print(f"خطا: فایل مدل '{MODEL_ONNX}' پیدا نشد. لطفاً مسیر آن را در کد بررسی کنید.")
    else:
        # دریافت متن از کاربر
        user_text = input("لطفاً متن فارسی مورد نظرتان را وارد کنید: ")
        if user_text: # اطمینان از اینکه کاربر متنی وارد کرده است
            speak_farsi(user_text)
            # اگر بخواهید بعد از اتمام پخش صدا کار دیگری انجام دهید،
            # باید از روش‌های پیشرفته‌تر برای مدیریت پخش ناهمزمان استفاده کنید.
            # برای سادگی، فعلا برنامه پس از شروع پخش تمام می‌شود.
            print("برنامه به پایان رسید.")
        else:
            print("شما هیچ متنی وارد نکردید.")
