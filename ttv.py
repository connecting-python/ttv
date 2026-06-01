import subprocess
import os
import winsound

# --- Paths Configuration ---
# --- تنظیم مسیرها ---

# If piper.exe is in the same folder, just use its name
# اگر piper.exe در همین پوشه قرار دارد، فقط نام آن کافی است
PIPER_EXE = r"piper/piper.exe"

# If models are stored inside the "models" folder
# اگر مدل‌ها داخل پوشه models قرار دارند
MODEL_ONNX = r"models/fa_IR-amir-medium.onnx"
MODEL_JSON = r"models/fa_IR-amir-medium.onnx.json"  # Piper model settings / تنظیمات مدل پایپر

# Output audio file
# فایل صوتی خروجی
OUTPUT_WAV = "output.wav"


def speak_farsi(text_to_speak):
    """
    Convert Persian text to speech using Piper and play it.
    تبدیل متن فارسی به صدا با استفاده از Piper و پخش آن
    """

    print(f"Converting text to speech: '{text_to_speak[:30]}...'")
    # نمایش بخشی از متن در حال تبدیل

    # Piper execution command
    # دستور اجرای Piper
    command = [
        PIPER_EXE,
        "--model", MODEL_ONNX,
        "--output_file", OUTPUT_WAV
    ]

    try:
        # Start Piper process and send text through stdin
        # اجرای پایپر و ارسال متن از طریق stdin
        process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8"
        )

        # Send text to Piper
        # ارسال متن به Piper
        stdout, stderr = process.communicate(input=text_to_speak)

        # Check if Piper returned an error
        # بررسی خطاهای Piper
        if process.returncode != 0:
            print(f"Piper execution failed (Error code: {process.returncode})")
            print(stderr)
            return

        # Verify that the output file exists
        # بررسی وجود فایل خروجی
        if os.path.exists(OUTPUT_WAV):

            print("Speech generated successfully. Playing audio...")
            # تولید صدا موفق بود، در حال پخش

            # Play WAV file asynchronously
            # پخش فایل WAV به صورت ناهمزمان
            winsound.PlaySound(
                OUTPUT_WAV,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )

            print("Audio playback started.")
            # پخش صدا آغاز شد

        else:
            print(f"Error: Audio file '{OUTPUT_WAV}' was not created.")
            # فایل صوتی تولید نشد

            if stdout:
                print("Piper standard output:", stdout)

    except FileNotFoundError:

        print(
            f"Error: Piper executable not found. "
            f"Please check the path: '{PIPER_EXE}'"
        )

        # فایل اجرایی Piper پیدا نشد

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        # یک خطای غیرمنتظره رخ داد


# --- Main Program ---
# --- برنامه اصلی ---

if __name__ == "__main__":

    print("--- Offline Persian Text-to-Speech with Piper ---")
    # مبدل آفلاین متن فارسی به گفتار با Piper

    # Check required files before starting
    # بررسی فایل‌های موردنیاز قبل از شروع
    if not os.path.exists(PIPER_EXE):

        print(
            f"Error: '{PIPER_EXE}' was not found. "
            f"Please verify the path."
        )

    elif not os.path.exists(MODEL_ONNX):

        print(
            f"Error: Model file '{MODEL_ONNX}' was not found. "
            f"Please verify the path."
        )

    else:

        # Get input text from user
        # دریافت متن از کاربر
        user_text = input("Enter Persian text / متن فارسی را وارد کنید: ")

        # Check if user entered any text
        # بررسی خالی نبودن متن
        if user_text:

            speak_farsi(user_text)

            # The program exits after playback starts
            # برنامه پس از شروع پخش به پایان می‌رسد
            print("Program finished. / برنامه به پایان رسید.")

        else:

            print("No text was entered. / هیچ متنی وارد نشد.")
