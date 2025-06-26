import ThemeSwitcher from '../components/atoms/Switch';
import Footer from '../components/organisms/Footer';
import LanguageSwitcher from '../components/organisms/LanguageSwitcher';
import Navbar from '../components/organisms/Navbar';

const Login = () => (
  <>
    <Navbar />
    <main role="main" tabIndex={-1} aria-label="Connexion">
      <h1>Connexion</h1>
      <form aria-label="Formulaire de connexion" style={{ maxWidth: 400, margin: '2rem auto' }}>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" required autoFocus />
        <label htmlFor="password">Mot de passe</label>
        <input id="password" name="password" type="password" required />
        <button type="submit">Se connecter</button>
      </form>
      <div style={{ display: 'flex', gap: '1rem', margin: '1rem 0' }}>
        <ThemeSwitcher />
        <LanguageSwitcher />
      </div>
      <a href="/register">Créer un compte</a>
    </main>
    <Footer />
  </>
);

export default Login;
