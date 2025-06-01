import React, { useEffect, useState } from "react";
import { Search, Star, Download, PlusCircle, Loader2 } from "lucide-react";

const API_URL = "https://api.dihyacoding.com/marketplace/templates"; // À adapter selon backend

export default function Marketplace() {
  const [templates, setTemplates] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        setTemplates(data.templates || []);
        setLoading(false);
      })
      .catch(() => {
        setError("Impossible de charger la marketplace.");
        setLoading(false);
      });
  }, []);

  const filtered = templates.filter((tpl) =>
    tpl.name.toLowerCase().includes(search.toLowerCase()) ||
    (tpl.tags || []).some(tag => tag.toLowerCase().includes(search.toLowerCase()))
  );

  return (
    <div className="w-full max-w-6xl mx-auto py-8">
      <div className="flex items-center gap-3 mb-8">
        <PlusCircle className="w-8 h-8 text-yellow-500" />
        <h1 className="text-3xl font-bold text-gray-900 tracking-wide">
          Marketplace de Templates & Plugins
        </h1>
      </div>
      <div className="flex flex-col md:flex-row md:items-center gap-4 mb-6">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-2.5 text-gray-400 w-5 h-5" />
          <input
            type="text"
            placeholder="Rechercher un template (ex: sport, tourisme, IA, logistique...)"
            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-200 focus:border-yellow-400 focus:ring-2 focus:ring-yellow-100 outline-none transition"
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
        </div>
        <a
          href="https://github.com/DihyaCoding/templates"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition"
        >
          <PlusCircle className="w-5 h-5" />
          Proposer un template
        </a>
      </div>
      {loading ? (
        <div className="flex justify-center items-center py-16">
          <Loader2 className="animate-spin w-8 h-8 text-yellow-400" />
          <span className="ml-3 text-gray-500">Chargement...</span>
        </div>
      ) : error ? (
        <div className="text-red-600 text-center py-8">{error}</div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filtered.length === 0 && (
            <div className="col-span-full text-center text-gray-400 py-12">
              Aucun template trouvé.
            </div>
          )}
          {filtered.map((tpl) => (
            <div
              key={tpl.id}
              className={`bg-white/90 rounded-xl shadow-lg border border-gray-100 p-6 flex flex-col justify-between hover:shadow-2xl transition cursor-pointer ${
                selected && selected.id === tpl.id ? "ring-2 ring-yellow-400" : ""
              }`}
              onClick={() => setSelected(tpl)}
            >
              <div>
                <div className="flex items-center gap-2 mb-2">
                  <img
                    src={tpl.icon || "/assets/template-default.svg"}
                    alt={tpl.name}
                    className="w-8 h-8 rounded"
                  />
                  <span className="text-xl font-bold text-gray-900">{tpl.name}</span>
                  {tpl.rating && (
                    <span className="flex items-center ml-2 text-yellow-500">
                      <Star className="w-4 h-4 mr-1" />
                      {tpl.rating.toFixed(1)}
                    </span>
                  )}
                </div>
                <p className="text-gray-700 mb-3 line-clamp-3">{tpl.description}</p>
                <div className="flex flex-wrap gap-2 mb-2">
                  {(tpl.tags || []).map((tag) => (
                    <span
                      key={tag}
                      className="bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded text-xs font-medium"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
              <div className="flex items-center justify-between mt-4">
                <a
                  href={tpl.demo || "#"}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-sm text-yellow-600 hover:underline"
                >
                  Voir démo
                </a>
                <a
                  href={tpl.download || "#"}
                  download
                  className="inline-flex items-center gap-1 px-3 py-1.5 rounded bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition"
                >
                  <Download className="w-4 h-4" />
                  Télécharger
                </a>
              </div>
            </div>
          ))}
        </div>
      )}
      {selected && (
        <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">
          <div className="bg-white rounded-xl shadow-2xl max-w-lg w-full p-8 relative">
            <button
              className="absolute top-3 right-3 text-gray-400 hover:text-yellow-500 text-2xl"
              onClick={() => setSelected(null)}
              aria-label="Fermer"
            >
              ×
            </button>
            <div className="flex items-center gap-3 mb-4">
              <img
                src={selected.icon || "/assets/template-default.svg"}
                alt={selected.name}
                className="w-10 h-10 rounded"
              />
              <h2 className="text-2xl font-bold text-gray-900">{selected.name}</h2>
            </div>
            <p className="text-gray-700 mb-4">{selected.description}</p>
            <div className="flex flex-wrap gap-2 mb-4">
              {(selected.tags || []).map((tag) => (
                <span
                  key={tag}
                  className="bg-yellow-100 text-yellow-700 px-2 py-0.5 rounded text-xs font-medium"
                >
                  {tag}
                </span>
              ))}
            </div>
            <div className="mb-4">
              <span className="font-semibold text-gray-800">Stack : </span>
              <span className="text-gray-600">{selected.stack?.join(", ")}</span>
            </div>
            <div className="flex items-center justify-between">
              <a
                href={selected.demo || "#"}
                target="_blank"
                rel="noopener noreferrer"
                className="text-sm text-yellow-600 hover:underline"
              >
                Voir la démo
              </a>
              <a
                href={selected.download || "#"}
                download
                className="inline-flex items-center gap-1 px-3 py-1.5 rounded bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition"
              >
                <Download className="w-4 h-4" />
                Télécharger
              </a>
            </div>
          </div>
        </div>
      )}
      <div className="mt-12 text-xs text-gray-400 text-center">
        <span>
          Vous souhaitez contribuer ? <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">Proposez un template ou plugin</a>
        </span>
      </div>
    </div>
  );
}