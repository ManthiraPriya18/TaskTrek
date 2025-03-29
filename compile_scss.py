import sass

try:
    sass.compile(dirname=('assets', 'static'), output_style='compressed')
    print("[SUCCESS] SCSS Compiled Successfully!")
except Exception as e:
    print(f"[ERROR] SCSS Compilation Failed: {e}")
