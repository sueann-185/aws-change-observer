import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { QueryClient, QueryClientProvider } from "react-query";
import { Toaster } from "sonner";
import { BrowserRouter } from "react-router-dom";
const queryClient = new QueryClient({
  defaultOptions: {},
});

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <App />
        <Toaster visibleToasts={1} position="bottom-right" richColors />
      </BrowserRouter>
    </QueryClientProvider>
  </StrictMode>
);
