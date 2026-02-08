import './rentSteps.css';
import React from 'react';
import carLineSvg from './car.svg'; // Ваш SVG с машиной и линией

const RentSteps = () => {
  return (
    <section className="steps">
      <h2 className="steps-h">Как происходит аренда автомобиля</h2>
      
      <div className="steps-container">
        {/* Верхний ряд: Карточка 1, Линия-Машина, Карточка 2, Карточка 3 */}
        <div className="steps-row top-row">
          <div className="step-card">
            <div className="step-num">1</div>
            <h3>Бронирование</h3>
            <p>Нужно оформить заявку на аренду через сайт компании или позвонив напрямую</p>
          </div>

          <div className="car-separator">
            <img src={carLineSvg} alt="car line" />
          </div>

          <div className="step-card">
            <div className="step-num">2</div>
            <h3>Доставка авто либо выдача в офисе</h3>
          </div>

          <div className="step-card">
            <div className="step-num">3</div>
            <h3>Заключение договора аренды</h3>
            <p>Для оформления понадобятся паспорт и водительское удостоверение</p>
          </div>
        </div>

        {/* Нижний ряд: Карточки 4, 5, 6 */}
        <div className="steps-row bottom-row">
          <div className="step-card">
            <div className="step-num">4</div>
            <h3>Передача автомобиля</h3>
            <p>Для оформления понадобятся паспорт и водительское удостоверение</p>
          </div>

          <div className="step-card">
            <div className="step-num">5</div>
            <h3>Получение ключей и документов</h3>
          </div>

          <div className="step-card">
            <div className="step-num">6</div>
            <h3>Возврат автомобиля</h3>
            <p>При возврате автомобиля в акте приёма-передачи также фиксируется состояние автомобиля...</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default RentSteps;