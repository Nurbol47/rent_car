import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import RoutePage from "./pages/RoutePage";
import Footer from "./componants/footer/footer copy";
import Header from "./componants/header/header";
import Reviews from "./componants/reviews";
import Company from "./componants/revСompany";
import Nature from "./componants/natr/nature";
import Card from "./componants/carCard/carCard"

function App() {
  return (
    <Router>
      <Header />
      <Reviews/>
      <Company/>
      <Nature/>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/route-details" element={<RoutePage />} />
      </Routes>
      <Card/>
      <Footer />
    </Router>
  );
}

export default App;