# دليل نشر اللعبة / Game Deployment Guide

## نظرة عامة / Overview

هذا الدليل يشرح كيفية نشر لعبة "Echoes of Tomorrow" على منصات مختلفة.
This guide explains how to deploy "Echoes of Tomorrow" game on different platforms.

---

## 🌐 الخيار 1: GitHub Pages (مجاني / Free)

### الخطوات / Steps:

1. **تفعيل GitHub Pages:**
   - افتح إعدادات المستودع / Open repository settings
   - اذهب إلى قسم "Pages"
   - اختر Branch: `copilot/add-game-storyline-elements`
   - احفظ التغييرات / Save changes

2. **الوصول للعبة / Access the Game:**
   ```
   https://uyteytydeydey.github.io/acuity-scheduling-unlocked/
   ```

3. **الميزات / Features:**
   - ✅ استضافة مجانية / Free hosting
   - ✅ تحديثات تلقائية / Automatic updates
   - ✅ HTTPS آمن / Secure HTTPS
   - ✅ سهل الإعداد / Easy setup

---

## 🎮 الخيار 2: itch.io (منصة ألعاب / Gaming Platform)

### لماذا itch.io؟ / Why itch.io?

- منصة مخصصة للألعاب المستقلة
- سهولة النشر والتحديث
- مجتمع نشط من اللاعبين
- دعم التبرعات والمدفوعات الاختيارية

### خطوات النشر / Publishing Steps:

1. **إنشاء حساب:**
   - زر https://itch.io
   - سجل حساب جديد
   - تحقق من بريدك الإلكتروني

2. **إنشاء مشروع جديد:**
   - اضغط "Create new project"
   - املأ المعلومات:
     - Title: Echoes of Tomorrow - أصداء الغد
     - Classification: Game
     - Kind of project: HTML
     - Release status: Released

3. **رفع الملفات:**
   ```bash
   # أنشئ ملف مضغوط
   zip -r echoes-of-tomorrow.zip *.py *.md index.html
   ```
   - ارفع الملف المضغوط
   - ضع علامة على "This file will be played in the browser"

4. **الإعدادات:**
   - Visibility: Public
   - Pricing: Free or Pay what you want
   - Tags: text-adventure, sci-fi, time-travel, arabic

5. **النشر:**
   - راجع كل شيء
   - اضغط "Save & view page"

**رابط المشروع / Project URL:**
```
https://your-username.itch.io/echoes-of-tomorrow
```

---

## 🐍 الخيار 3: Replit (تشغيل مباشر / Direct Run)

### المميزات / Features:
- تشغيل Python مباشرة في المتصفح
- لا حاجة لتثبيت Python
- مشاركة سهلة

### الخطوات / Steps:

1. **إنشاء Repl:**
   - زر https://replit.com
   - اضغط "+ Create Repl"
   - اختر "Python"
   - سمّه "Echoes of Tomorrow"

2. **رفع الملفات:**
   - ارفع `echoes_of_tomorrow.py`
   - ارفع الملفات الداعمة

3. **تشغيل اللعبة:**
   - اضغط "Run"
   - شارك الرابط مع الآخرين

**رابط المشاركة / Share URL:**
```
https://replit.com/@your-username/Echoes-of-Tomorrow
```

---

## 📱 الخيار 4: PyInstaller (تطبيق قابل للتنفيذ / Executable)

### إنشاء ملف تنفيذي / Create Executable:

```bash
# تثبيت PyInstaller
pip install pyinstaller

# إنشاء ملف تنفيذي
pyinstaller --onefile --name "EchoesOfTomorrow" echoes_of_tomorrow.py

# الملف سيكون في مجلد dist/
```

### للويندوز / For Windows:
```bash
pyinstaller --onefile --windowed --name "EchoesOfTomorrow" echoes_of_tomorrow.py
```

### للماك / For macOS:
```bash
pyinstaller --onefile --windowed --name "EchoesOfTomorrow.app" echoes_of_tomorrow.py
```

### للينكس / For Linux:
```bash
pyinstaller --onefile --name "echoes-of-tomorrow" echoes_of_tomorrow.py
```

### توزيع الملف / Distributing:
- Windows: `EchoesOfTomorrow.exe`
- macOS: `EchoesOfTomorrow.app`
- Linux: `echoes-of-tomorrow`

---

## 🐳 الخيار 5: Docker Container

### إنشاء Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY echoes_of_tomorrow.py .
COPY *.md .

CMD ["python", "echoes_of_tomorrow.py"]
```

### البناء والتشغيل / Build and Run:

```bash
# بناء الصورة
docker build -t echoes-of-tomorrow .

# تشغيل الحاوية
docker run -it echoes-of-tomorrow

# نشر على Docker Hub
docker tag echoes-of-tomorrow your-username/echoes-of-tomorrow
docker push your-username/echoes-of-tomorrow
```

---

## ☁️ الخيار 6: Heroku (خدمة سحابية / Cloud Service)

### الإعداد / Setup:

1. **إنشاء ملفات التكوين:**

**requirements.txt:**
```
# No external dependencies needed
```

**Procfile:**
```
web: python echoes_of_tomorrow.py
```

**runtime.txt:**
```
python-3.9.16
```

2. **النشر / Deploy:**

```bash
# تسجيل الدخول
heroku login

# إنشاء تطبيق
heroku create echoes-of-tomorrow

# نشر
git push heroku copilot/add-game-storyline-elements:main

# فتح التطبيق
heroku open
```

---

## 📦 الخيار 7: GitHub Releases (للتحميل المباشر / Direct Download)

### إنشاء إصدار / Create Release:

1. **في GitHub:**
   - اذهب إلى "Releases"
   - اضغط "Create a new release"
   - Tag: v1.0.0
   - Title: Echoes of Tomorrow v1.0 - أصداء الغد

2. **إرفاق الملفات / Attach Files:**
   - `echoes_of_tomorrow.py`
   - `GAME_README.md`
   - `test_game.py`
   - `demo_game.py`
   - `verify_story.py`

3. **النشر / Publish:**
   - اكتب وصف الإصدار
   - اضغط "Publish release"

**رابط التحميل / Download URL:**
```
https://github.com/uyteytydeydey/acuity-scheduling-unlocked/releases/tag/v1.0.0
```

---

## 🎯 الخيار 8: Google Colab (تشغيل فوري / Instant Run)

### إنشاء Notebook:

1. **زر Google Colab:**
   - https://colab.research.google.com

2. **إنشاء Notebook جديد:**
   - File → New notebook

3. **أضف الكود:**

```python
# تحميل اللعبة
!wget https://raw.githubusercontent.com/uyteytydeydey/acuity-scheduling-unlocked/copilot/add-game-storyline-elements/echoes_of_tomorrow.py

# تشغيل اللعبة
!python echoes_of_tomorrow.py
```

4. **المشاركة:**
   - File → Share
   - Anyone with the link

---

## 🌍 الخيار 9: Web Version (نسخة ويب كاملة / Full Web Version)

### باستخدام Brython (Python في المتصفح):

**قريباً / Coming Soon:**
- نسخة HTML/JavaScript كاملة
- تعمل بدون Python
- واجهة رسومية جميلة
- حفظ التقدم في المتصفح

---

## 📱 الخيار 10: Mobile Version (نسخة الجوال)

### باستخدام Kivy/BeeWare:

**مخطط مستقبلي / Future Plan:**
- نسخة Android (APK)
- نسخة iOS (IPA)
- واجهة تعمل باللمس
- دعم الأجهزة اللوحية

---

## 🎨 الخيار الموصى به / Recommended Options

### للمشاركة السريعة / For Quick Sharing:
1. **GitHub Pages** - أسهل وأسرع
2. **Replit** - للتشغيل المباشر
3. **itch.io** - لمجتمع الألعاب

### للتوزيع الاحترافي / For Professional Distribution:
1. **PyInstaller** - ملفات تنفيذية
2. **GitHub Releases** - إدارة الإصدارات
3. **Docker** - توافق كامل

---

## 📊 مقارنة الخيارات / Options Comparison

| الخيار / Option | السهولة / Ease | التكلفة / Cost | الوصول / Reach |
|-----------------|----------------|----------------|-----------------|
| GitHub Pages | ⭐⭐⭐⭐⭐ | مجاني / Free | عالمي / Global |
| itch.io | ⭐⭐⭐⭐ | مجاني / Free | متوسط / Medium |
| Replit | ⭐⭐⭐⭐⭐ | مجاني / Free | متوسط / Medium |
| PyInstaller | ⭐⭐⭐ | مجاني / Free | محلي / Local |
| Docker | ⭐⭐ | مجاني / Free | تقني / Technical |
| Heroku | ⭐⭐⭐ | مجاني / Free | عالمي / Global |

---

## ✅ قائمة التحقق للنشر / Deployment Checklist

- [ ] اختبر اللعبة محلياً / Test game locally
- [ ] راجع جميع الملفات / Review all files
- [ ] حدّث التوثيق / Update documentation
- [ ] اختر منصة النشر / Choose platform
- [ ] ارفع الملفات / Upload files
- [ ] اختبر على المنصة / Test on platform
- [ ] شارك الرابط / Share link
- [ ] اجمع التغذية الراجعة / Collect feedback

---

## 🆘 الدعم / Support

إذا واجهت أي مشاكل في النشر:
If you encounter any deployment issues:

1. راجع التوثيق أعلاه / Check documentation above
2. ابحث عن المشكلة في Google
3. اسأل في مجتمع GitHub
4. افتح Issue في المستودع

---

## 📞 روابط مفيدة / Useful Links

- **GitHub Repository:** https://github.com/uyteytydeydey/acuity-scheduling-unlocked
- **Game README:** [GAME_README.md](GAME_README.md)
- **Implementation Summary:** [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)

---

## 🎉 التحديثات المستقبلية / Future Updates

- [ ] نسخة ويب تفاعلية كاملة / Full interactive web version
- [ ] دعم اللغات الإضافية / Additional language support
- [ ] واجهة رسومية GUI / Graphical user interface
- [ ] نسخة الجوال / Mobile version
- [ ] نظام حفظ سحابي / Cloud save system
- [ ] لوحة الإنجازات / Achievements board

---

**"في كل خط زمني، الأمل يستمر"**  
**"In every timeline, hope persists"**

© 2025 Echoes of Tomorrow - أصداء الغد
