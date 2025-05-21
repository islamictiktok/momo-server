import os

try:
    exec(open("momo_core.py").read(), globals())
except Exception as e:
    print(f"❌ Error: {e}")
