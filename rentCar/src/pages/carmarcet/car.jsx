
import "./car.css";
import { Link } from 'react-router-dom';





function CarDetails() {
  return (
    <div>
      <Link to="/">Главная</Link>
      <h1>Детали автомобиля</h1>
      <p>Здесь будет отображаться подробная информация о выбранном автомобиле.</p>
    </div>
  );
}

export default CarDetails;