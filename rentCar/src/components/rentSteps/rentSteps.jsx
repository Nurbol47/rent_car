import React from 'react';
import './rentSteps.css';
import icon1 from './icon1.svg';
import icon2 from './icon2.svg';
import icon3 from './icon3.svg';
import icon4 from './icon4.svg';
import icon5 from './icon5.svg';
import icon6 from './icon6.svg';



const TrustSection = () => {
  const benefits = [
    {
      icon: <img src={icon1} alt="Путешествуйте без ограничений" />, 
      title: "Путешествуйте без ограничений",
      text: "Откройте для себя все туристические жемчужины Иркутской области, Республики Бурятии и Монголии"
    },
    {
      icon: <img src={icon2} alt="Большой суточный пробег" />, 
      title: "Большой суточный пробег – 250 км",
      text: "Максимальная свобода в передвижении без лишних опасений и переплат. Фиксированная цена за перепробег"
    },
    {
      icon: <img src={icon3} alt="Первый прокат с кэшбэком" />,
      title: "Первый прокат с кэшбэком",
      text: "Получайте реальный кэшбэк за поездки и тратьте его на следующую аренду или дополнительные услуги в полном объёме"
    },
    {
      icon: <img src={icon4} alt="Надежные авто" />,
      title: "Надежные авто = ваша безопасность",
      text: "Все автомобили проходят регулярное техническое обслуживание, парк постоянно пополняют новинки"
    },
    {
      icon: <img src={icon5} alt="Расширенная страховка" />,
      title: "Расширенная страховка",
      text: "Наши авто застрахованы по ОСАГО, есть расширенные пакеты страхования для вашей защищённости"
    },
    {
      icon: <img src={icon6} alt="Любая форма оплаты" />,
      title: "Любая форма оплаты",
      text: "Платите удобным для вас способом: наличные, банковской картой, на рас. счёт. Оф. договор, отчетные документы и чеки"
    }
  ];

  return (
    <section className="trust-section">
      <div className="container">
        <h2>Почему нам доверяют?</h2>
        <div className="trust-grid">
          {benefits.map((item, index) => (
            <article key={index} className="trust-card">
              <div className="icon-box">
                {item.icon}
              </div>
              <div className="card-content">
                <h3>{item.title}</h3>
                <p>{item.text}</p>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
};

export default TrustSection;