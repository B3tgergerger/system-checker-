# System Checker

## English Version

### Description
System Checker is a tool designed to provide detailed information about your system's health and performance. It includes features to check disk usage, memory usage, CPU usage, SMART status, GPU status, network speed, battery status, system uptime, CPU and GPU temperatures, system information, audio devices, and installed software.

### Features
- **Disk Usage**: Displays the percentage of disk space used.
- **Memory Usage**: Shows the percentage of memory usage.
- **CPU Usage**: Indicates the current CPU usage percentage.
- **SMART Status**: Checks the SMART status of your hard drive.
- **GPU Status**: Provides information on GPU utilization.
- **Network Speed**: Tests and displays your network download and upload speeds.
- **Battery Status**: Shows battery percentage and whether it's plugged in.
- **System Uptime**: Displays how long the system has been running since the last boot.
- **CPU Temperature**: Displays the current CPU temperature.
- **GPU Temperature**: Shows the current GPU temperature.
- **System Information**: Displays basic system information such as OS and machine name.
- **Audio Devices**: Lists the audio devices connected to your system.
- **Installed Software**: Lists all installed software on your system.

### How to Use
1. Clone the repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Run the `main.py` file to launch the application.
4. Click the "Check System" button to start the system check.

### Known Issues and Errors
- **SMART Status Error (WinError 50)**: This error occurs if the SMART status request is not supported by your hardware or OS.
- **GPU Status Error (NVML shared library not found)**: This error indicates that the NVML library required to check GPU status is not installed or found.
- **Network Speed Error (urlopen error)**: This error occurs if there is a network issue or the Speedtest server cannot be reached.
- **CPU Temperature Error (module Psutil has no attribute sensors_temperatures)**: This error indicates that the version of Psutil installed does not support temperature readings.
- **GPU Temperature Error (NVML shared library not found)**: Similar to the GPU status error, this indicates the absence of the NVML library.
- **Installed Software Error (WinError 50)**: This error occurs if the request to list installed software is not supported by your hardware or OS.

---

## النسخة العربية

### الوصف
برنامج System Checker هو أداة مصممة لتوفير معلومات تفصيلية عن صحة وأداء النظام لديك. تتضمن الميزات فحص استخدام القرص، استخدام الذاكرة، استخدام وحدة المعالجة المركزية، حالة SMART، حالة وحدة معالجة الرسوميات، سرعة الشبكة، حالة البطارية، وقت تشغيل النظام، درجات حرارة وحدة المعالجة المركزية ووحدة معالجة الرسوميات، معلومات النظام، الأجهزة الصوتية، والبرامج المثبتة.

### الميزات
- **استخدام القرص**: يعرض نسبة مساحة القرص المستخدمة.
- **استخدام الذاكرة**: يظهر نسبة استخدام الذاكرة.
- **استخدام وحدة المعالجة المركزية**: يشير إلى نسبة استخدام وحدة المعالجة المركزية الحالية.
- **حالة SMART**: يفحص حالة SMART للقرص الصلب.
- **حالة وحدة معالجة الرسوميات**: يوفر معلومات حول استخدام وحدة معالجة الرسوميات.
- **سرعة الشبكة**: يختبر ويعرض سرعات تنزيل ورفع الشبكة.
- **حالة البطارية**: يظهر نسبة البطارية وما إذا كانت موصولة بالكهرباء.
- **وقت تشغيل النظام**: يعرض مدة تشغيل النظام منذ آخر تشغيل.
- **درجة حرارة وحدة المعالجة المركزية**: يعرض درجة حرارة وحدة المعالجة المركزية الحالية.
- **درجة حرارة وحدة معالجة الرسوميات**: يظهر درجة حرارة وحدة معالجة الرسوميات الحالية.
- **معلومات النظام**: يعرض معلومات أساسية عن النظام مثل نظام التشغيل واسم الجهاز.
- **الأجهزة الصوتية**: يسرد الأجهزة الصوتية المتصلة بالنظام.
- **البرامج المثبتة**: يسرد جميع البرامج المثبتة على النظام.

### كيفية الاستخدام
1. قم باستنساخ المستودع إلى جهازك المحلي.
2. تأكد من تثبيت Python والمكتبات المطلوبة.
3. قم بتشغيل ملف `main.py` لبدء التطبيق.
4. انقر على زر "Check System" لبدء فحص النظام.

### المشكلات والأخطاء المعروفة
- **خطأ حالة SMART (WinError 50)**: يحدث هذا الخطأ إذا لم يكن طلب حالة SMART مدعومًا من قبل الجهاز أو نظام التشغيل لديك.
- **خطأ حالة وحدة معالجة الرسوميات (NVML shared library not found)**: يشير هذا الخطأ إلى أن مكتبة NVML المطلوبة لفحص حالة وحدة معالجة الرسوميات غير مثبتة أو لم يتم العثور عليها.
- **خطأ سرعة الشبكة (urlopen error)**: يحدث هذا الخطأ إذا كانت هناك مشكلة في الشبكة أو لم يتمكن من الوصول إلى خادم Speedtest.
- **خطأ درجة حرارة وحدة المعالجة المركزية (module Psutil has no attribute sensors_temperatures)**: يشير هذا الخطأ إلى أن الإصدار المثبت من Psutil لا يدعم قراءات درجة الحرارة.
- **خطأ درجة حرارة وحدة معالجة الرسوميات (NVML shared library not found)**: يشير هذا إلى عدم وجود مكتبة NVML المطلوبة.
- **خطأ البرامج المثبتة (WinError 50)**: يحدث هذا الخطأ إذا لم يكن الطلب للحصول على قائمة البرامج المثبتة مدعومًا من قبل الجهاز أو نظام التشغيل لديك.
