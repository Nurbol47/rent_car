import BackgroundSlider from "../backgroundSlider/backgroundSlider"
import BookingForm from "../bookingForm/bookingForm"
import SliderControls from "../sliderControls/sliderControls"
import { useState } from "react";
import "./style.css"

export default function Hero() {
      const [currentSlide, setCurrentSlide] = useState(0);
    
    return (
        <>
       <div className="home-page">

        <div className="fon">
          <BackgroundSlider currentSlide={currentSlide} />

          <main className="main-content">
            <h1 className="h1">
              Прокат <br /> автомобилей <br /> в Улан-Удэ
            </h1>

            <BookingForm />

            <SliderControls
              currentSlide={currentSlide}
              setCurrentSlide={setCurrentSlide}
            />
          </main>
        </div>
      </div>
        </>
    )
}