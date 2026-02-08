import "./style.css";
import { Link } from 'react-router-dom';
import image from "../assets/image/card.jpg";
import image2 from "../assets/image/card2.jpg"

function CarCard() {
  return (
    <section>
      <div className="containerCard">
        <h1>Прокат автомобилей в Улан-Удэ</h1>
       <div className="carCards">
         <div className="car-card">
          <div className="image">
            <img src={image} alt="" />
            <div className="yellow">
              <span>🔥</span>
              <p>-25%</p>
            </div>
            <div className="yellow1">
              <p>30.12 - 05.01</p>
            </div>
            <button className="arrow left" >‹</button>
            <div className="dots">
              <span></span>
              <p></p>
              <span></span>
              <span></span>
              <span></span>
            </div>
            <button className="arrow right">›</button>
          </div>
          <div className="car-title">
            <h3>BMW X5 xDrive30D</h3>
            <p className="car-price">
              16 000 ₽ /сут. <span>22 000 ₽ / сут.</span>
            </p>
            <button className="car-btn">Забронировать</button>
          </div>
        </div>
       </div>
       <div className="swov">
                  <Link to="/car-details">
            <button>Показать больше ▼</button>
          </Link>
       </div>
      </div>
    </section>
  );
}

export default CarCard;
