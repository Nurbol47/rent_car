import "./Home.css";
import RoutesSection from "../componants/priroda/priroda";
import Privileges from "../componants/privileg/privileges";
import RentSteps from "../componants/navi/navi";
import TrustSection from "../componants/rentSteps/rentSteps";

import Hero from "../componants/hero/hero";
import CarCard from "../componants/carCard/carCard";
import Company from "../componants/revСompany";

function Home() {
  return (
    <>
      <Hero />
      <CarCard/>
      <TrustSection />
      <Company/>
      <RoutesSection/>
      <RentSteps />
      <Privileges />
    </>
  );
}

export default Home;
