import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home";
import MarkerInfo from "./pages/MarkerInfo";
import Layout from "./layouts/Layout";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="/marker/:markerId" element={<MarkerInfo />} />
      </Route>
    </Routes>
  );
}

export default App;
