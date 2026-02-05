import { useState, useEffect } from 'react';
import './style.css';
import CarCard from '../carCard/carCard';

function CarsList() {
  const [cars, setCars] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Заглушка для API - позже заменить на реальный запрос
    const fetchCars = async () => {
      try {
        // Симуляция загрузки данных
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Заглушка данных
        const mockCars = [
          { id: 1, name: "BMW X5 xDrive30D", price: "16 000 ₽ /сут." },
          { id: 2, name: "Toyota Land Cruiser 200", price: "16 000 ₽ /сут." },
          { id: 3, name: "LiXiang L7", price: "16 000 ₽ /сут." }
        ];
        
        setCars(mockCars);
        setLoading(false);
      } catch (err) {
        setError('Не удалось загрузить список автомобилей');
        setLoading(false);
      }
    };

    fetchCars();
  }, []);

  // Показываем состояние загрузки
  if (loading) {
    return (
      <div className="cars-list loading">
        <div className="spinner"></div>
        <p>Загружаем список автомобилей...</p>
      </div>
    );
  }

  // Показываем ошибку
  if (error) {
    return (
      <div className="cars-list error">
        <p>{error}</p>
        <button onClick={() => window.location.reload()}>Повторить попытку</button>
      </div>
    );
  }

  // Показываем список автомобилей
  return (
    <div className="cars-list">
      <h2>Наш автопарк</h2>
      <div className="cars-container">
        {cars.map(car => (
          <CarCard 
            key={car.id}
            carName={car.name}
            carPrice={car.price}
          />
        ))}
      </div>
    </div>
  );
}

export default CarsList;