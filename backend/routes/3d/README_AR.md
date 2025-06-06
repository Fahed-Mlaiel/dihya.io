<!-- README متقدم للغاية – وحدة 3D (Dihya Coding) – العربية -->

[![تغطية الاختبارات](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/dihya-coding/dihya.io)
[![متوافق مع GDPR](https://img.shields.io/badge/GDPR-متوافق-blue)](https://github.com/dihya-coding/dihya.io)
[![SEO Audit](https://img.shields.io/badge/SEO-AAA-success)](https://github.com/dihya-coding/dihya.io)

# Dihya 3D Backend – متقدم، آمن، متعدد اللغات، قابل للتوسعة

**وحدة متكاملة لإدارة وأتمتة وتوسعة مشاريع 3D وVR وAR وAI والأصول والإضافات والامتثال للـGDPR والتدقيق وSEO وإمكانية الوصول وتعدد المستأجرين والاختبارات وCI/CD والسيادة الرقمية.**

---

## 🚀 الميزات الرئيسية
- واجهة برمجة تطبيقات REST وGraphQL (المشاريع، الأصول، الإضافات، التدقيق، GDPR، SEO)
- أمان أقصى: CORS، JWT، WAF، مكافحة DDOS، تحقق صارم، RBAC، سجلات منظمة، مراقبة
- دعم ديناميكي للغات (fr، en، ar، tzm، de، zh، ja، ko، nl، he، fa، hi، es)
- تعدد المستأجرين، إدارة أدوار متقدمة (admin، user، guest)
- نظام إضافات أعمال قابل للتوسعة (API، CLI، hot reload، تدقيق، استرجاع)
- امتثال GDPR: تصدير، إخفاء الهوية، حذف، سجلات قابلة للتصدير، قابلية التدقيق
- SEO backend: robots.txt، sitemap.xml، سجلات منظمة، إمكانية وصول WCAG 2.2
- دعم AI مفتوح المصدر (LLaMA، Mixtral، Mistral)
- اختبارات شاملة (وحدات، تكامل، e2e، إمكانية وصول، أداء، SEO، GDPR، إضافات)
- نشر GitHub Actions، Docker، K8s، Codespaces، fallback محلي
- توثيق مدمج، أدلة متعددة اللغات، سكريبتات CLI، شارات الامتثال

---

## 📦 هيكل الوحدة
- `routes.py`: نقاط النهاية REST/GraphQL، الأمان، i18n، GDPR، الإضافات الديناميكية
- `views.py`: ViewSets متقدمة، تدقيق، تصدير/حذف GDPR، إمكانية وصول، SEO
- `models.py`: نماذج 3D متعددة اللغات، GDPR، تدقيق، إضافات، تعدد المستأجرين
- `plugins/`: الأساس، أمثلة الأعمال، التوسعة الديناميكية، اختبارات، API/CLI
- `tests/`: اختبارات وحدات، تكامل، e2e، إمكانية وصول، أداء، SEO، GDPR، إضافات
- `templates/`: قوالب Jinja2/HTML/JSON متعددة اللغات، جاهزة لـGDPR، SEO، إمكانية وصول
- `cli_3d.py`: سكريبت CLI لاستيراد/تصدير مشاريع 3D
- `export_audit_logs.py`: نقطة نهاية لتصدير سجلات التدقيق
- `QUICKSTART_API.md`: دليل البدء السريع، متعدد اللغات، جاهز لـCI/CD

---

## 🔒 الأمان وGDPR
- CORS صارم، JWT إلزامي، WAF، مكافحة DDOS، تحقق، تدقيق، سجلات منظمة
- تصدير/حذف GDPR، إخفاء الهوية، قابلية التدقيق، سجلات قابلة للتصدير، توافق CI/CD
- اختبارات اختراق آلية (XSS، حقن، brute-force، مكافحة الروبوتات، CSRF)

## 🌍 التدويل وإمكانية الوصول
- 13+ لغة ديناميكية، نقطة نهاية `/3d/i18n/locales`، سجلات متعددة اللغات
- إمكانية وصول WCAG 2.2، اختبارات ARIA، رؤوس، متعدد اللغات، API/HTML

## 🧩 الإضافات والتوسعة
- إضافات أعمال (صناعة، صحة، AI، إلخ)، توسعة ديناميكية (API/CLI)، hot reload، استرجاع، تدقيق
- نقاط النهاية `/3d/plugins/list`، `/3d/plugins/run`، اختبارات التوسعة الديناميكية

## 📈 SEO والأداء
- robots.txt، sitemap.xml، سجلات SEO منظمة، نقطة نهاية `/3d/seo/structured-logs`
- اختبارات أداء (ضغط، مكافحة DDOS، زمن الاستجابة)

## 🛠️ DevEx والتوثيق
- دليل البدء السريع، شارات التغطية/GDPR/SEO، سكريبتات CLI، docstring/type hints، أدلة متعددة اللغات

## 🕵️ المراقبة والتدقيق
- تصدير سجلات التدقيق (تصفية حسب المستخدم/المستأجر/التاريخ)، مراقبة Prometheus/Grafana

## ✅ الاختبارات وCI/CD
- تغطية 100% (وحدات، تكامل، e2e، إمكانية وصول، SEO، GDPR، إضافات، أداء)
- نشر GitHub Actions، Docker، K8s، Codespaces، fallback محلي

---

## 🏁 أمثلة API وCLI
- `POST /threedprojects/`: إنشاء مشروع 3D
- `GET /threedprojects/`: قائمة مشاريع 3D
- `GET /threedprojects/{id}/export_rgpd/`: تصدير GDPR
- `DELETE /threedprojects/{id}/delete_rgpd/`: حذف GDPR
- `GET /3d/i18n/locales`: اللغات المدعومة ديناميكياً
- `GET /3d/plugins/list`: قائمة الإضافات الديناميكية
- `POST /3d/plugins/run`: تشغيل إضافة أعمال
- `python cli_3d.py export --id 1`: تصدير مشروع 3D عبر CLI
- `python cli_3d.py import --file export.json`: استيراد مشروع 3D عبر CLI

---

## 🧪 اختبارات متقدمة
- `pytest tests/test_security_e2e.py`: الأمان، الاختراق، مكافحة الروبوتات، brute-force
- `pytest tests/test_accessibility_e2e.py`: إمكانية الوصول، رؤوس، ARIA، متعدد اللغات
- `pytest tests/test_performance_e2e.py`: الأداء، مكافحة DDOS
- `pytest tests/test_seo_e2e.py`: SEO، robots، sitemap، سجلات منظمة
- `pytest tests/test_fallback_ai.py`: fallback AI مفتوح المصدر
- `pytest tests/test_industrie_plugin.py`: توسعة إضافة أعمال ديناميكية

---

## 🌐 متعدد اللغات، GDPR، SEO، إمكانية وصول، سيادة
- متوافق 100%، جاهز للإنتاج، قابل للتوسعة، سيادي، CI/CD، تدقيق، مراقبة، توثيق مدمج، شارات الامتثال

---

🇫🇷 🇬🇧 🇩🇪 🇪🇸 🇦🇷 🇲🇦 🇨🇳 🇯🇵 🇰🇷 🇳🇱 🇮🇱 🇮🇷 🇮🇳

*للمساهمة، راجع PLUGINS_GUIDE.md، TEST_STRATEGY.md، ومتطلبات Dihya.*
