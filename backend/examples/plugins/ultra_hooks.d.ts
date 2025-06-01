// Déclaration de types pour ultra_hooks (TypeScript)
export declare function useUser(): any;
export declare function useTenant(): string;
export declare function useRole(): string;
export declare function useA11y(): { announce: (msg: string) => void };
export declare function useFallbackAI(): { fallbackSuggest: (context: string, error: string, lang: string) => string };
export declare function useMonitoring(): { logEvent: (event: string, details: any) => void };
