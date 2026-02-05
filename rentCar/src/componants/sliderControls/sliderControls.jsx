import "./style.css";
import { MdOutlineArrowForwardIos } from "react-icons/md";
import { MdOutlineArrowBackIosNew } from "react-icons/md";

function SliderControls({ currentSlide, setCurrentSlide }) {
  return (
    <div className="slider-controls">
      <button
        onClick={() => setCurrentSlide(0)}
        className={currentSlide === 0 ? "active" : ""}
      >
        <MdOutlineArrowBackIosNew />
      </button>

      <button
        onClick={() => setCurrentSlide(1)}
        className={currentSlide === 1 ? "active" : ""}
      >
        <MdOutlineArrowForwardIos />
      </button>
    </div>
  );
}

export default SliderControls;
