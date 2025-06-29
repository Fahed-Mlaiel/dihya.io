# Exemples d’intégration des layouts

## MainLayout
```jsx
import MainLayout from './MainLayout';

export default function HomePage() {
  return (
    <MainLayout>
      <h1>Bienvenue sur la plateforme !</h1>
    </MainLayout>
  );
}
```

## AuthLayout
```jsx
import AuthLayout from './AuthLayout';

export default function LoginPage() {
  return (
    <AuthLayout>
      <LoginForm />
    </AuthLayout>
  );
}
```

## DashboardLayout
```jsx
import DashboardLayout from './DashboardLayout';

export default function AdminPage() {
  return (
    <DashboardLayout>
      <DashboardContent />
    </DashboardLayout>
  );
}
```
