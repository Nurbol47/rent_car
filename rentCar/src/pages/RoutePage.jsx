import React from 'react';
import Home from './Home';
import { Link } from 'react-router-dom';
import './RoutePage.css'; 

const RoutePage = () => {
  return (
    <main className="route-detail-page">
      <div className="container">
        <nav className="breadcrumbs">
          <Link to="/">Главная</Link>
          <span> &gt; </span>
          <span className="current">Заповедная Бурятия</span>
        </nav>

        <h1 className="page-title">Заповедная бурятия</h1>

        <section className="new-cards-grid">
          <div className="placeholder-card">Твоя новая карточка 1</div>
          <div className="placeholder-card">Твоя новая карточка 2</div>
          <div className="placeholder-card">Твоя новая карточка 3</div>
        </section>
      </div>
    </main>
  );
};

export default RoutePage;