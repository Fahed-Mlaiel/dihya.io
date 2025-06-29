import ThemeSwitcher from '../components/atoms/Switch';
import Footer from '../components/organisms/Footer';
import LanguageSwitcher from '../components/organisms/LanguageSwitcher';
import Navbar from '../components/organisms/Navbar';

const Marketplace = () => (
  <>
    <Navbar />
    <main role="main" tabIndex={-1} aria-label="Marketplace">
      <h1>Marketplace</h1>
      {/* Liste dynamique des plugins et templates disponibles */}
      <section aria-label="Plugins et templates">
        <p>Découvrez et installez des plugins, templates métiers, extensions IA, etc.</p>
        {/* Zone d'affichage dynamique */}
      </section>
      <div style={{ display: 'flex', gap: '1rem', margin: '1rem 0' }}>
        <ThemeSwitcher />
        <LanguageSwitcher />
      </div>
    </main>
    <Footer />
  </>
);

export default Marketplace;
