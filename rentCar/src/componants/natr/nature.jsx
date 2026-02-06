import "./nature.css";
import photo from "../pages/car-photo.svg";
import photo1 from "../pages/car-photo1.svg";
import photo2 from "../pages/car-photo2.svg";
import arrows from "../pages/arrows.svg";

function Nature() {
  return (
    <section>
      <div className="nature">
        <div className="hero-content">
          <h1>Заповедная Бурятия</h1>
          <p>Список маршрутов</p>
          <button>Перейти в галерею маршрутов</button>
        </div>

        <div className="cardsNat">
          <div className="cardNat">
            <img src={photo} alt="" />
            <h3>Голубые озёра</h3>
          </div>

          <div className="cardNat">
            <img src={photo1} alt="" />
            <h3>Чемал</h3>
          </div>

          <div className="cardNat">
            <img src={photo2} alt="" />
            <h3>Озеро Манжерок</h3>
          </div>
        </div>
      </div>
      <div className="sliderNav">
        <button>‹</button>
        <div className="dots">
          <span></span>
          <p></p>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <button>›</button>
      </div>
    </section>
  );
}

export default Nature;
