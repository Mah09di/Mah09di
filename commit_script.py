import os
import datetime

# لیست تاریخ‌هایی که باید برای حفظ الگوی "MAHDI" کامیت زده بشه
commit_dates = [
    "2025-03-10", "2025-03-12", "2025-03-14",  # تاریخ‌های الگوی خودت رو وارد کن
]

for date in commit_dates:
    os.system(f'git commit --allow-empty -m "Auto commit for streak" --date "{date} 12:00:00"')
    os.system('git push')
