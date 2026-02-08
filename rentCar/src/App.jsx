import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import RoutePage from "./pages/RoutePage";
import Footer from "./components/footer/Footer";
import Header from "./components/header/Header";
import CarDetails from "./pages/carmarcet/car";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/route-details" element={<RoutePage />} />
        <Route path="/car-details" element={<CarDetails />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;