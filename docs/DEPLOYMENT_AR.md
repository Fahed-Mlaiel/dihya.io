# دليل النشر لمشروع Dihya Coding

## ١. المتطلبات
- Docker, Docker Compose، Kubernetes
- CI/CD (GitHub Actions)
- إعداد متغيرات البيئة (ENV)

## ٢. خطوات النشر
1. بناء الحاويات:
```bash
docker-compose build
```
2. تشغيل الخدمات:
```bash
docker-compose up -d
```
3. نشر على Kubernetes:
```bash
kubectl apply -f k8s/
```
4. تحقق من الصحة والأمان (CORS، JWT، WAF، مراقبة)

## ٣. الأمان والامتثال
- تفعيل الجدران النارية (WAF)
- مراقبة السجلات والتنبيهات
- الامتثال لـ RGPD (تصدير، حذف، تدقيق)

## ٤. النسخ الاحتياطي والاستعادة
- راجع [DB_BACKUP_GUIDE.md](./DB_BACKUP_GUIDE.md)
- راجع [DB_RESTORE_GUIDE.md](./DB_RESTORE_GUIDE.md)

## ٥. موارد إضافية
- [README_AR.md](./README_AR.md)
- [securite_GUIDE_AR.md](./securite_GUIDE_AR.md)
