// src/App.jsx
import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import RoutePage from "./pages/RoutePage"; // Импортируем новую страницу
import Footer from "./componants/footer/footer copy";
import Header from "./componants/header/header";

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        {/* Главная страница (Home) */}
        <Route path="/" element={<Home />} />
        
        {/* Чистая страница для карточек */}
        <Route path="/route-details" element={<RoutePage />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;