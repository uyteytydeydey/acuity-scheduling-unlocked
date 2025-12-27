# حل مشكلة "Please provide a title" / Fixing "Please provide a title" Error

## المشكلة / The Problem

إذا ظهرت لك رسالة الخطأ:
If you see the error message:
```
There was a problem saving your project
Please provide a title for your project before continuing
```

## الحل / The Solution

هذه المشكلة تحدث عند النشر على منصات مثل itch.io. إليك كيفية حلها:
This problem occurs when publishing to platforms like itch.io. Here's how to fix it:

---

## على itch.io / On itch.io

### الخطوة 1: املأ المعلومات المطلوبة / Step 1: Fill Required Information

عند إنشاء مشروع جديد على itch.io، تأكد من ملء:
When creating a new project on itch.io, make sure to fill:

1. **Title (العنوان - مطلوب/Required):**
   ```
   Echoes of Tomorrow - أصداء الغد
   ```

2. **Project URL (رابط المشروع):**
   ```
   echoes-of-tomorrow
   ```
   أو / or
   ```
   asda-alghad
   ```

3. **Short Description (وصف قصير - مطلوب/Required):**
   ```
   A text-based temporal adventure where you control time and decide the fate of humanity.
   لعبة مغامرة نصية زمنية حيث تتحكم في الزمن وتقرر مصير البشرية.
   ```

4. **Classification (التصنيف - مطلوب/Required):**
   - اختر: **Games** ✓
   - Choose: **Games** ✓

5. **Kind of project (نوع المشروع - مطلوب/Required):**
   - اختر: **Downloadable** ✓
   - Choose: **Downloadable** ✓

---

### الخطوة 2: معلومات إضافية / Step 2: Additional Information

**Tags (الوسوم - اختياري ولكن موصى به):**
```
text-adventure, sci-fi, time-travel, choices-matter, story-rich, 
multiple-endings, arabic, english, temporal, cyberpunk
```

**Genre (النوع):**
- Adventure
- Interactive Fiction

**Release Status (حالة الإصدار):**
- Released ✓

**Pricing (التسعير):**
- Free ✓
- أو / or
- Pay what you want (الدفع حسب الرغبة)

---

### الخطوة 3: رفع الملفات / Step 3: Upload Files

1. **قم بتغليف اللعبة أولاً:**
   ```bash
   cd /path/to/game
   python3 package_game.py
   ```

2. **ارفع الملف المضغوط:**
   - اذهب إلى قسم "Upload files"
   - اسحب ملف: `dist/echoes-of-tomorrow-v1.0.0-*.zip`
   - أو اضغط "Upload files" واختر الملف

3. **تفعيل الخيارات:**
   - ✓ This file will be played in the browser (إذا كان HTML)
   - ✓ This is a downloadable file (للملف المضغوط)

---

## قائمة التحقق الكاملة / Complete Checklist

قبل الضغط على "Save" تأكد من:
Before clicking "Save" make sure:

- [ ] **Title** مُعبأ / Title is filled
- [ ] **Short description** مُعبأ / Short description is filled
- [ ] **Classification** محدد (Games) / Classification is set (Games)
- [ ] **Kind of project** محدد / Kind of project is set
- [ ] **Cover image** مُرفقة (اختياري) / Cover image uploaded (optional)
- [ ] **Files** مُرفوعة / Files uploaded
- [ ] **Pricing** محدد / Pricing is set

---

## نموذج معلومات جاهز للنسخ / Ready-to-Copy Project Information

### English Version:

**Title:**
```
Echoes of Tomorrow
```

**Short Description:**
```
A text-based temporal adventure. Control time, fight enemies, collect logs, and choose one of four endings. Will you save humanity or become a timeless guardian?
```

**Description (Full):**
```
# Echoes of Tomorrow

A temporal research facility has suffered a catastrophic failure. You are Adam, a field operative equipped with the TimeBrace device, capable of manipulating time itself.

## Features
- 5 Time manipulation abilities
- 4 different endings (including 1 hidden ending)
- 6 facility sectors to explore
- 4 enemy types
- Collectible system: 12 logs + 5 temporal keys
- Ethical choices that affect the story

## Story
Navigate through temporal rifts, fight distorted enemies, collect hidden logs, and make choices that will determine the fate of time manipulation technology and humanity itself.

## How to Play
1. Download and extract the ZIP file
2. Run: python3 echoes_of_tomorrow.py
3. Follow the on-screen instructions
4. Make choices and explore

## Requirements
- Python 3.6 or newer

Playtime: 20-30 minutes per ending
```

### Arabic Version (النسخة العربية):

**العنوان / Title:**
```
أصداء الغد - Echoes of Tomorrow
```

**الوصف القصير / Short Description:**
```
مغامرة نصية زمنية. تحكم بالزمن، قاتل الأعداء، اجمع السجلات، واختر واحدة من أربع نهايات. هل ستنقذ البشرية أم تصبح حارساً أبدياً؟
```

**الوصف الكامل / Full Description:**
```
# أصداء الغد

منشأة بحث زمنية تعرضت لفشل كارثي. أنت آدم، عميل ميداني مجهز بجهاز TimeBrace، قادر على التلاعب بالزمن نفسه.

## المميزات
- 5 قدرات للتحكم بالزمن
- 4 نهايات مختلفة (منها نهاية مخفية)
- 6 قطاعات منشأة للاستكشاف
- 4 أنواع من الأعداء
- نظام جمع: 12 سجل + 5 مفاتيح زمنية
- خيارات أخلاقية تؤثر على القصة

## القصة
تنقل عبر التشققات الزمنية، قاتل الأعداء المشوهين، اجمع السجلات المخفية، واتخذ قرارات ستحدد مصير تقنية التلاعب بالزمن والبشرية.

## كيفية اللعب
1. حمّل واستخرج ملف ZIP
2. شغّل: python3 echoes_of_tomorrow.py
3. اتبع التعليمات على الشاشة
4. اتخذ القرارات واستكشف

## المتطلبات
- Python 3.6 أو أحدث

وقت اللعب: 20-30 دقيقة لكل نهاية
```

---

## صور الغلاف المقترحة / Suggested Cover Images

يُنصح بإنشاء صورة غلاف بالمواصفات:
Recommended cover image specifications:

- **حجم موصى به / Recommended size:** 630 x 500 pixels
- **حد أدنى / Minimum:** 315 x 250 pixels
- **نسبة العرض / Aspect ratio:** 5:4 or 16:9
- **صيغة / Format:** PNG or JPG

**عناصر الصورة / Image elements:**
- شعار اللعبة / Game logo
- ألوان سيبربانك (أزرق، سماوي، أرجواني) / Cyberpunk colors (blue, cyan, purple)
- رموز زمنية / Temporal symbols
- العنوان بالعربي والإنجليزي / Title in Arabic and English

---

## نصائح إضافية / Additional Tips

1. **احفظ كمسودة أولاً / Save as draft first:**
   - ضع Visibility على "Draft"
   - احفظ المشروع
   - راجع كل شيء
   - ثم غيّر إلى "Public"

2. **استخدم المعاينة / Use preview:**
   - قبل النشر، اضغط "View page"
   - تأكد أن كل شيء يظهر بشكل صحيح

3. **أضف Screenshots (لقطات شاشة):**
   - خذ لقطات من اللعبة أثناء التشغيل
   - ارفعها في قسم Screenshots
   - على الأقل 3-5 صور

---

## إذا استمرت المشكلة / If the Problem Persists

إذا ظهرت نفس الرسالة بعد ملء جميع الحقول:
If the same message appears after filling all fields:

1. **حاول متصفح آخر / Try another browser:**
   - Chrome, Firefox, Safari
   - امسح الكاش / Clear cache

2. **تأكد من الاتصال / Check connection:**
   - تأكد من استقرار الإنترنت
   - حاول مرة أخرى

3. **تواصل مع الدعم / Contact support:**
   - itch.io support: support@itch.io
   - أو استخدم نموذج المساعدة على الموقع

---

## بدائل النشر / Publishing Alternatives

إذا واجهت صعوبة مع itch.io، جرب:
If you have difficulty with itch.io, try:

### 1. GitHub Pages (أسهل / Easiest)
```
1. اذهب إلى إعدادات المستودع
2. فعّل GitHub Pages
3. شارك الرابط
```

### 2. GitHub Release
```
1. اذهب إلى Releases
2. Create new release
3. ارفع ملف ZIP
4. انشر
```

### 3. Google Drive
```
1. ارفع ملف ZIP
2. اضبط الخصوصية على "Anyone with link"
3. شارك الرابط
```

انظر [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) للمزيد من الخيارات.

---

## ملخص سريع / Quick Summary

**السبب الأساسي للخطأ:**
حقل "Title" فارغ أو حقول مطلوبة أخرى غير مُعبأة.

**الحل:**
1. املأ Title: "Echoes of Tomorrow - أصداء الغد"
2. املأ Short Description
3. اختر Classification: "Games"
4. اختر Kind: "Downloadable"
5. احفظ

---

**"في كل خط زمني، الأمل يستمر"**  
**"In every timeline, hope persists"**

© 2025 Echoes of Tomorrow
