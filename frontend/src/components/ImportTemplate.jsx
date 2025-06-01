import React, { useRef, useState } from "react";
import { CloudUpload, FileText, CheckCircle, AlertCircle } from "lucide-react";

const allowedTypes = [
  "application/json",
  "application/x-yaml",
  "text/yaml",
  "application/javascript",
  "text/javascript"
];

export default function ImportTemplate({ onImport }) {
  const fileInput = useRef();
  const [fileName, setFileName] = useState("");
  const [status, setStatus] = useState(null); // null | "success" | "error"
  const [error, setError] = useState("");

  const handleFileChange = async (e) => {
    setStatus(null);
    setError("");
    const file = e.target.files[0];
    if (!file) return;
    setFileName(file.name);

    if (!allowedTypes.includes(file.type) && !file.name.endsWith(".yaml") && !file.name.endsWith(".yml") && !file.name.endsWith(".json") && !file.name.endsWith(".js")) {
      setStatus("error");
      setError("Format non supporté. Formats acceptés : JSON, YAML, JS.");
      return;
    }

    const reader = new FileReader();
    reader.onload = (evt) => {
      try {
        const content = evt.target.result;
        onImport && onImport(content, file.name);
        setStatus("success");
      } catch (err) {
        setStatus("error");
        setError("Erreur lors de l'import du template.");
      }
    };
    reader.onerror = () => {
      setStatus("error");
      setError("Impossible de lire le fichier.");
    };
    reader.readAsText(file);
  };

  return (
    <div className="w-full max-w-xl mx-auto bg-white/80 rounded-xl shadow-lg p-8 flex flex-col items-center border border-gray-200">
      <div className="flex items-center gap-3 mb-4">
        <CloudUpload className="w-8 h-8 text-yellow-500" />
        <h2 className="text-2xl font-bold text-gray-900 tracking-wide">Importer un template métier</h2>
      </div>
      <p className="text-gray-600 mb-6 text-center">
        Importez un template métier au format <span className="font-semibold">JSON</span>, <span className="font-semibold">YAML</span> ou <span className="font-semibold">JS</span>.<br />
        <span className="text-xs text-gray-400">Exemple : sport, tourisme, transport, etc.</span>
      </p>
      <label
        htmlFor="import-template"
        className="cursor-pointer flex flex-col items-center justify-center border-2 border-dashed border-yellow-400 rounded-lg p-8 hover:bg-yellow-50 transition mb-4 w-full"
      >
        <FileText className="w-10 h-10 text-gray-400 mb-2" />
        <span className="text-gray-700 font-medium">
          {fileName ? fileName : "Cliquez ou glissez un fichier ici"}
        </span>
        <input
          id="import-template"
          type="file"
          accept=".json,.yaml,.yml,.js"
          className="hidden"
          ref={fileInput}
          onChange={handleFileChange}
        />
      </label>
      {status === "success" && (
        <div className="flex items-center text-green-600 mt-2">
          <CheckCircle className="w-5 h-5 mr-1" />
          Import réussi !
        </div>
      )}
      {status === "error" && (
        <div className="flex items-center text-red-600 mt-2">
          <AlertCircle className="w-5 h-5 mr-1" />
          {error}
        </div>
      )}
      <button
        type="button"
        onClick={() => fileInput.current && fileInput.current.click()}
        className="mt-6 px-6 py-2 rounded-lg bg-yellow-400 hover:bg-yellow-500 text-gray-900 font-semibold shadow transition"
      >
        Sélectionner un fichier
      </button>
      <div className="mt-8 text-xs text-gray-400 text-center">
        <span>
          Besoin d’un exemple ? <a href="https://github.com/DihyaCoding/templates" target="_blank" rel="noopener noreferrer" className="underline hover:text-yellow-600">Voir la galerie</a>
        </span>
      </div>
    </div>
  );
}