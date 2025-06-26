import ThemeSwitcher from '../components/atoms/Switch';
import Footer from '../components/organisms/Footer';
import LanguageSwitcher from '../components/organisms/LanguageSwitcher';
import Navbar from '../components/organisms/Navbar';

const Preview = () => (
  <>
    <Navbar />
    <main role="main" tabIndex={-1} aria-label="Aperçu du projet">
      <h1>Aperçu du projet généré</h1>
      {/* Affichage dynamique du projet généré, code, assets, documentation, etc. */}
      <section aria-label="Aperçu dynamique">
        <p>Votre projet métier est prêt !</p>
        {/* Zone d'affichage du code généré, assets, etc. */}
      </section>
      <div style={{ display: 'flex', gap: '1rem', margin: '1rem 0' }}>
        <ThemeSwitcher />
        <LanguageSwitcher />
      </div>
      <a href="/generate">Générer un autre projet</a>
    </main>
    <Footer />
  </>
);

export default Preview;
