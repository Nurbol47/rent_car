import './style.css';

function CarCard({ carName, carPrice }) {
  return (
    <div className="car-card">
      <div className="car-content">
        <h3 className="car-title">{carName}</h3>
        <div className="car-price">{carPrice}</div>
      </div>
      <button className="car-book-button">Забронировать</button>
    </div>
  );
}

export default CarCard;