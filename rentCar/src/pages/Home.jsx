import "./Home.css";
import Privileges from "../componants/privileg/privileges";
import RentSteps from "../componants/navi/navi";
import TrustSection from "../componants/rentSteps/rentSteps";

import Hero from "../componants/hero/hero";

function Home() {
  return (
    <>
      <Hero />
      <TrustSection />
      <RentSteps />
      <Privileges />
    </>
  );
}

export default Home;
