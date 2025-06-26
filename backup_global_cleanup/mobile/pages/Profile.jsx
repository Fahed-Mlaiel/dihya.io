import ThemeSwitcher from '../components/atoms/Switch';
import Footer from '../components/organisms/Footer';
import LanguageSwitcher from '../components/organisms/LanguageSwitcher';
import Navbar from '../components/organisms/Navbar';

const Profile = () => (
  <>
    <Navbar />
    <main role="main" tabIndex={-1} aria-label="Profil utilisateur">
      <h1>Mon Profil</h1>
      <section aria-label="Informations utilisateur">
        {/* Affichage des infos utilisateur, avatar, email, rôles, etc. */}
        <p>Nom : <strong>Utilisateur Démo</strong></p>
        <p>Email : demo@dihya.io</p>
        <p>Rôle : Admin</p>
      </section>
      <div style={{ display: 'flex', gap: '1rem', margin: '1rem 0' }}>
        <ThemeSwitcher />
        <LanguageSwitcher />
      </div>
      <a href="/logout">Se déconnecter</a>
    </main>
    <Footer />
  </>
);

export default Profile;
