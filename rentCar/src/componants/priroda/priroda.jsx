import React from 'react';
import { Link } from 'react-router-dom';
import './priroda.css';
import png1 from './car-photo.png'
import png2 from './car-photo1.png'
import png3 from './car-photo2.png'

const RoutesSection = () => {
  const routes = [
    { id: 'blue-lakes', title: "Голубые озёра", img: png1 },
    { id: 'chemal', title: "Чемал", img: png2 },
    { id: 'manzherok', title: "Озеро манжерок", img: png3 }
  ];

  return (
    <section className="routes-wrapper">
      <header className="hero-banner">
        <div className="hero-content">
          <h1>Заповедная Бурятия</h1>
          <p>Список маршрутов</p>
          
          <Link to="/route-details">
            <button className="hero-button">Перейти в галерею маршрутов</button>
          </Link>
        </div>
      </header>

      <div className="routes-grid">
        {routes.map((route) => (
          <Link to={`/route-details`} key={route.id} className="route-card">
            <figure>
              <img src={route.img} alt={route.title} />
              <figcaption>{route.title}</figcaption>
            </figure>
          </Link>
        ))}
      </div>
    </section>
  );
};

export default RoutesSection;