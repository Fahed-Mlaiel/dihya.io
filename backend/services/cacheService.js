/**
 * 🚀 DIHYA.IO - SERVICE DE CACHE REDIS
 * Cache intelligent avec fallback en mémoire pour le développement
 */

const redis = require('redis');

class CacheService {
  constructor() {
    this.client = null;
    this.isConnected = false;
    this.defaultTTL = 300; // 5 minutes par défaut
    this.memoryCache = new Map(); // Fallback en développement
    this.memoryTimers = new Map(); // Timers pour TTL en mémoire
    this.connect();
  }

  /**
   * Initialise la connexion Redis
   */
  async connect() {
    try {
      // En développement sans Redis, utilise le cache mémoire
      if (process.env.NODE_ENV === 'development' && !process.env.REDIS_URL) {
        console.log('🔧 Mode développement: Cache en mémoire activé');
        this.isConnected = false;
        return true;
      }

      this.client = redis.createClient({
        url: process.env.REDIS_URL || 'redis://localhost:6379',
        password: process.env.REDIS_PASSWORD,
        socket: {
          reconnectStrategy: (retries) => Math.min(retries * 50, 1000)
        }
      });

      this.client.on('error', (err) => {
        console.warn('⚠️ Redis Error, using memory cache:', err.message);
        this.isConnected = false;
      });

      this.client.on('connect', () => {
        console.log('✅ Redis connecté');
        this.isConnected = true;
      });

      await this.client.connect();
      this.isConnected = true;
      return true;

    } catch (error) {
      console.warn('⚠️ Redis non disponible, cache mémoire:', error.message);
      this.isConnected = false;
      return false;
    }
  }

  /**
   * Stockage avec fallback mémoire
   */
  async set(key, value, ttl = this.defaultTTL) {
    try {
      if (this.isConnected && this.client) {
        await this.client.setEx(key, ttl, JSON.stringify(value));
      } else {
        // Cache mémoire avec TTL
        this.memoryCache.set(key, value);

        // Gestion TTL en mémoire
        if (this.memoryTimers.has(key)) {
          clearTimeout(this.memoryTimers.get(key));
        }

        const timer = setTimeout(() => {
          this.memoryCache.delete(key);
          this.memoryTimers.delete(key);
        }, ttl * 1000);

        this.memoryTimers.set(key, timer);
      }
      return true;
    } catch (error) {
      console.warn('Erreur cache set:', error.message);
      return false;
    }
  }

  /**
   * Récupération avec fallback mémoire
   */
  async get(key) {
    try {
      if (this.isConnected && this.client) {
        const result = await this.client.get(key);
        return result ? JSON.parse(result) : null;
      } else {
        // Cache mémoire
        return this.memoryCache.get(key) || null;
      }
    } catch (error) {
      console.warn('Erreur cache get:', error.message);
      return null;
    }
  }

  /**
   * Suppression
   */
  async delete(key) {
    try {
      if (this.isConnected && this.client) {
        await this.client.del(key);
      } else {
        this.memoryCache.delete(key);
        if (this.memoryTimers.has(key)) {
          clearTimeout(this.memoryTimers.get(key));
          this.memoryTimers.delete(key);
        }
      }
      return true;
    } catch (error) {
      console.warn('Erreur cache delete:', error.message);
      return false;
    }
  }

  /**
   * Test de connexion
   */
  async ping() {
    try {
      if (this.isConnected && this.client) {
        await this.client.ping();
        return true;
      } else {
        // Le cache mémoire est toujours "disponible"
        return true;
      }
    } catch (error) {
      return false;
    }
  }

  // ===============================================================================
  // 🎯 MÉTHODES SPÉCIALISÉES
  // ===============================================================================

  /**
   * Sessions utilisateur
   */
  async setSession(userId, sessionData, ttl = 3600) {
    return this.set(`session:${userId}`, sessionData, ttl);
  }

  async getSession(userId) {
    return this.get(`session:${userId}`);
  }

  async deleteSession(userId) {
    return this.delete(`session:${userId}`);
  }

  /**
   * Données de projets
   */
  async setProject(projectId, projectData, ttl = 600) {
    return this.set(`project:${projectId}`, projectData, ttl);
  }

  async getProject(projectId) {
    return this.get(`project:${projectId}`);
  }

  /**
   * Templates
   */
  async setTemplate(templateId, templateData, ttl = 1800) {
    return this.set(`template:${templateId}`, templateData, ttl);
  }

  async getTemplate(templateId) {
    return this.get(`template:${templateId}`);
  }

  /**
   * Statistiques simples
   */
  async getActiveSessionsCount() {
    try {
      if (this.isConnected && this.client) {
        const keys = await this.client.keys('session:*');
        return keys.length;
      } else {
        // Compter les sessions en mémoire
        let count = 0;
        for (const key of this.memoryCache.keys()) {
          if (key.startsWith('session:')) count++;
        }
        return count;
      }
    } catch (error) {
      return 0;
    }
  }

  async getCacheStats() {
    try {
      if (this.isConnected && this.client) {
        const info = await this.client.info('stats');
        return {
          type: 'redis',
          connected: true,
          info: info
        };
      } else {
        return {
          type: 'memory',
          connected: false,
          size: this.memoryCache.size,
          keys: Array.from(this.memoryCache.keys())
        };
      }
    } catch (error) {
      return { error: error.message };
    }
  }

  /**
   * Fermeture propre
   */
  async disconnect() {
    try {
      if (this.client) {
        await this.client.disconnect();
      }

      // Nettoyage cache mémoire
      this.memoryCache.clear();
      for (const timer of this.memoryTimers.values()) {
        clearTimeout(timer);
      }
      this.memoryTimers.clear();

      console.log('✅ Cache service fermé proprement');
    } catch (error) {
      console.warn('Erreur fermeture cache:', error.message);
    }
  }
}

// Instance singleton
const cacheService = new CacheService();

module.exports = cacheService;
