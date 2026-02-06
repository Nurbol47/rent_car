// import "./style.css";

// function CarCard({ carName, carPrice }) {
//   return (
//     <div className="car-card">
//       <div className="car-content">
//         <h3 className="car-title">{carName}</h3>
//         <div className="car-price">{carPrice}</div>
//       </div>
//       <button className="car-book-button">Забронировать</button>
//     </div>
//   );
// }

// export default CarCard;

import "./style.css";
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
            <button className="arrow left">‹</button>
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
         <div className="car-card">
          <div className="image">
            <img src={image2} alt="" />
            <button className="arrow left">‹</button>
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
            <h3>Toyota Land Cruiser 200</h3>
            <p className="car-price">16 000 ₽ /сут. </p>
            <button className="car-btn">Забронировать</button>
          </div>
        </div>
       </div>
       <a href="#" className="show">Показать больше ▼</a>
      </div>
    </section>
  );
}

export default CarCard;
