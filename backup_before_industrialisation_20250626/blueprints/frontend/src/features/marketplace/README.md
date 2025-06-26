# Marketplace – Feature métier

Ce dossier gère la marketplace (listing, achat, publication, admin, etc.).

## Composants
- MarketplaceList.jsx
- MarketplaceItem.jsx
- MarketplaceAdmin.jsx

## Cas d’usage
- Affichage des items disponibles
- Achat d’un item
- Publication d’un item (admin)

## Flux utilisateur
1. L’utilisateur consulte la marketplace
2. Achète ou publie un item

## Exemples d’intégration
```jsx
import MarketplaceList from './MarketplaceList';
<MarketplaceList />
```

## Schéma d’architecture
[MarketplaceList] → [MarketplaceItem] → [MarketplaceAdmin]
