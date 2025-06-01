# GUIDE.md - Gestion des secrets Dihya

## Bonnes pratiques
- Utilisez des variables d’environnement, jamais de secrets en dur.
- Chiffrez les secrets au repos et en transit.
- Limitez l’accès aux secrets (RBAC, audit logs).
- Mettez en place une rotation régulière des secrets.
- Documentez chaque variable dans `.env.example`.

## Best Practices (English)
- Use environment variables, never hardcode secrets.
- Encrypt secrets at rest and in transit.
- Restrict access (RBAC, audit logs).
- Rotate secrets regularly.
- Document each variable in `.env.example`.

## الممارسات الجيدة (العربية)
- استخدم متغيرات البيئة، لا تضع الأسرار مباشرة في الكود.
- شفر الأسرار أثناء التخزين والنقل.
- حد من الوصول (RBAC، سجلات التدقيق).
- قم بتدوير الأسرار بانتظام.
- وثق كل متغير في `.env.example`.

## ⵜⴰⵎⴰⵣⵉⵖⵜ (amazigh)
- Seqdec variables n environment, ur tzemreḍ ara isirran di code.
- Sdukel isirran di tazwart d tazwart n tutlayin.
- Sers ayen i d-yettwasen (RBAC, audit logs).
- Sers rotation n isirran.
- Sers documentation di `.env.example`.

---

### Outils recommandés
- HashiCorp Vault, AWS Secrets Manager, Azure Key Vault
- Audit et monitoring automatisés

### Contribution
Respectez ce guide pour toute gestion ou modification de secrets.
