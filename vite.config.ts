import { defineConfig } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { componentTagger } from "lovable-tagger";

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  // Remove server config for production builds to work on Vercel
  ...(mode !== "production" && {
    server: {
      host: "::",
      port: 8080,
    }
  }),
  plugins: [react(), mode === "development" && componentTagger()].filter(Boolean),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  // Optimize for Vercel deployment
  build: {
    target: "esnext",
    cssCodeSplit: false,
    sourcemap: mode === "development",
    rollupOptions: {
      output: {
        manualChunks: {
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'ui-vendor': ['lucide-react'],
          'radix-vendor': ['@radix-ui/react-dialog', '@radix-ui/react-slot', '@radix-ui/react-label', '@radix-ui/react-separator'],
          'data-vendor': ['@tanstack/react-query'],
        }
      }
    }
  },
  // Base URL for Vercel deployment (empty string for root deployment)
  base: "/",
  // Optimize for production
  define: {
    global: "globalThis",
  }
}));
