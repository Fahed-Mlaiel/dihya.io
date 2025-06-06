# دليل الوصول 3D – Dihya (AR)

هذا الدليل يوضح جميع أفضل الممارسات والاختبارات والأدوات والمتطلبات لإمكانية الوصول في وحدة 3D (الخلفية، API، الإضافات، القوالب، الاختبارات، CI/CD).

## المتطلبات
- الامتثال لـ WCAG 2.2 AA/AAA
- API والقوالب متوافقة مع ARIA، تنقل عبر لوحة المفاتيح/الصوت
- متعدد اللغات (fr، en، ar، tzm، de، zh، ja، ko، nl، he، fa، hi، es)
- اختبارات آلية (axe، pa11y، Lighthouse)
- رؤوس HTTP: Content-Language، Content-Type، ARIA
- إمكانية الوصول لـ CLI والوثائق (Markdown، HTML، PDF)

## الاختبارات
- `pytest tests/test_accessibility_e2e.py`
- تحقق ARIA، رؤوس، متعدد اللغات، API/HTML

## المساهمة
- يجب اختبار كل مسار أو قالب أو إضافة جديدة لإمكانية الوصول.
- راجع ACCESSIBILITY_GUIDE.md العام لمنهجية Dihya.
