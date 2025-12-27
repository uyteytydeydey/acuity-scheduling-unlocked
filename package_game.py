#!/usr/bin/env python3
"""
Package the Echoes of Tomorrow game for distribution
تغليف لعبة أصداء الغد للتوزيع
"""

import os
import zipfile
import shutil
from datetime import datetime

def create_distribution_package():
    """Create a distribution package with all game files."""
    
    print("=" * 70)
    print("إنشاء حزمة التوزيع / Creating Distribution Package")
    print("=" * 70)
    print()
    
    # Package info
    version = "1.0.0"
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"echoes-of-tomorrow-v{version}-{timestamp}"
    
    # Files to include
    game_files = [
        "echoes_of_tomorrow.py",
        "test_game.py",
        "demo_game.py",
        "verify_story.py",
        "GAME_README.md",
        "IMPLEMENTATION_SUMMARY.md",
        "DEPLOYMENT_GUIDE.md",
        "README.md",
        "index.html",
        ".gitignore"
    ]
    
    # Create distribution directory
    dist_dir = f"dist/{package_name}"
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir, exist_ok=True)
    
    print(f"📦 إنشاء الحزمة / Creating package: {package_name}")
    print()
    
    # Copy files
    copied_files = []
    for file in game_files:
        if os.path.exists(file):
            dest = os.path.join(dist_dir, file)
            shutil.copy2(file, dest)
            size = os.path.getsize(file) / 1024  # KB
            print(f"  ✓ {file} ({size:.1f} KB)")
            copied_files.append(file)
        else:
            print(f"  ✗ {file} (not found)")
    
    print()
    print(f"عدد الملفات / Files copied: {len(copied_files)}/{len(game_files)}")
    print()
    
    # Create ZIP archive
    zip_filename = f"dist/{package_name}.zip"
    print(f"📦 إنشاء ملف مضغوط / Creating ZIP archive...")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in copied_files:
            file_path = os.path.join(dist_dir, file)
            zipf.write(file_path, file)
    
    zip_size = os.path.getsize(zip_filename) / 1024  # KB
    print(f"  ✓ {zip_filename} ({zip_size:.1f} KB)")
    print()
    
    # Create README for distribution
    readme_content = f"""# Echoes of Tomorrow - أصداء الغد
Version {version}

## محتويات الحزمة / Package Contents

### الملفات الأساسية / Core Files:
- echoes_of_tomorrow.py - اللعبة الرئيسية (Main game)
- test_game.py - اختبارات (Tests)
- demo_game.py - عرض توضيحي (Demo)
- verify_story.py - التحقق من القصة (Story verification)

### التوثيق / Documentation:
- GAME_README.md - دليل اللعب (Game guide)
- IMPLEMENTATION_SUMMARY.md - ملخص التطبيق (Implementation summary)
- DEPLOYMENT_GUIDE.md - دليل النشر (Deployment guide)
- README.md - نظرة عامة (Overview)

### الويب / Web:
- index.html - صفحة ويب للعبة (Game web page)

## كيفية اللعب / How to Play

### المتطلبات / Requirements:
- Python 3.6 أو أحدث / Python 3.6 or newer

### تشغيل اللعبة / Run the Game:
```bash
python3 echoes_of_tomorrow.py
```

### اختبار اللعبة / Test the Game:
```bash
python3 test_game.py
```

## الميزات / Features

✅ 4 شخصيات رئيسية / 4 main characters
✅ 4 أنواع أعداء / 4 enemy types
✅ 5 قدرات TimeBrace / 5 TimeBrace abilities
✅ 4 نهايات مختلفة / 4 different endings
✅ نهاية مخفية / Hidden ending
✅ 12 سجل لليان / 12 Lian's logs
✅ 5 مفاتيح زمنية / 5 temporal keys

## الدعم / Support

GitHub: https://github.com/uyteytydeydey/acuity-scheduling-unlocked

---

"في كل خط زمني، الأمل يستمر"
"In every timeline, hope persists"

© 2025 Echoes of Tomorrow
"""
    
    readme_path = os.path.join(dist_dir, "DISTRIBUTION_README.txt")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    
    print("✓ DISTRIBUTION_README.txt created")
    print()
    
    # Summary
    print("=" * 70)
    print("✅ تم إنشاء الحزمة بنجاح / Package created successfully!")
    print("=" * 70)
    print()
    print(f"📁 المجلد / Directory: dist/{package_name}/")
    print(f"📦 الملف المضغوط / ZIP file: {zip_filename}")
    print(f"📊 الحجم الإجمالي / Total size: {zip_size:.1f} KB")
    print()
    print("📋 الخطوات التالية / Next Steps:")
    print("  1. اختبر الحزمة / Test the package")
    print("  2. ارفعها على GitHub Releases")
    print("  3. شارك الرابط مع اللاعبين / Share with players")
    print()
    print("💡 نصيحة / Tip:")
    print("  يمكنك رفع الملف المضغوط على:")
    print("  - GitHub Releases")
    print("  - itch.io")
    print("  - Google Drive")
    print("  - Dropbox")
    print()
    print("=" * 70)
    
    return zip_filename

def main():
    """Main function."""
    try:
        # Create dist directory
        os.makedirs("dist", exist_ok=True)
        
        # Create package
        package = create_distribution_package()
        
        print(f"\n✓ الحزمة جاهزة للتوزيع / Package ready for distribution!")
        print(f"  {package}")
        
    except Exception as e:
        print(f"\n✗ خطأ / Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
