import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import RoutePage from "./pages/RoutePage";
import Footer from "./componants/footer/footer copy";
import Header from "./componants/header/header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/route-details" element={<RoutePage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;