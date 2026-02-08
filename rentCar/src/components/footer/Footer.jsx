import './footer.css';
import logo from './logo.svg';
import icon2gis from './2gis.svg';
import yandexMaps from './yandex.svg';
import googleMaps from './maps.svg';
import tgIcon from './tg.svg';
import whatsappIcon from './what.svg';

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-logo">
          <img src={logo} alt="СОЛ-АВТО" />
        </div>

        <div className="footer-ratings">
          <div className="rating-badge">
            <img src={icon2gis} alt="2gis" />
            <span>2gis</span>
          </div>
          <div className="rating-badge">
            <img src={yandexMaps} alt="Яндекс" />
            <span>Яндекс карты </span>
          </div>
          <div className="rating-badge">
            <img src={googleMaps} alt="Google" />
            <span>Google maps</span>
          </div>
        </div>

        <div className="footer-contacts">
          <a href="tel:+79243543333" className="phone">+7 (924) 354-33-33</a>
          <div className="social-icons">
            <a href="#"><img src={tgIcon} alt="Telegram" /></a>
            <a href="#"><img src={whatsappIcon} alt="WhatsApp" /></a>
          </div>
          <button className="call-button">Заказать звонок</button>
        </div>
      </div>
      <div className='hav'>
        <div className='nav'>Автопарк</div>
        <select className='nav'><option>Услуги</option></select>
        <select className='nav'><option>Онас</option></select>
        <div className='nav'>Акции</div>
<div className='nav'>Достопримичательности</div>
      </div>
    </footer>
  );
}

export default Footer;