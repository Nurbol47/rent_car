import "./style.css";
import carImg1 from "../assets/image/carImg1.png";
import carImg2 from "../assets/image/carImg2.png";

function BackgroundSlider({ currentSlide }) {
  const backgrounds = [carImg1, carImg2];

  return (
    <div className="background-slider">
      {backgrounds.map((img, index) => (
        <div
          key={index}
          className={`slider-image ${index === currentSlide ? "active" : ""}`}
          style={{ backgroundImage: `url(${img})` }}
        />
      ))}
    </div>
  );
}

export default BackgroundSlider;
