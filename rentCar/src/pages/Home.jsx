import "./Home.css";
import RoutesSection from "../components/priroda/priroda";
import Privileges from "../components/privileg/privileges";
import RentSteps from "../components/navi/navi";
import TrustSection from "../components/rentSteps/rentSteps";

import Hero from "../components/hero/hero";
import CarCard from "../components/carCard/carCard";

function Home() {
  return (
    <>
      <Hero />
      <CarCard/>
      <TrustSection />
      <RoutesSection/>
      <RentSteps />
      <Privileges />
    </>
  );
}

export default Home;
