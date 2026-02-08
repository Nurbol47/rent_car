import "./company.css";
import logo from "../pages/logo-otzivi.svg";
import logo1 from "../pages/logo-otzivi1.svg";
import logo2 from "../pages/logo-otzivi2.svg";
import face1 from "../pages/face1.svg";
import face2 from "../pages/dmit.svg";
import face3 from "../pages/face.svg";
import stars from "../pages/stars.svg";

function Company() {
  return (
    <section>
      <div className="reviews">
        <h1>Отзывы о нашей компании</h1>

        <div className="sources">
          <div className="source">
            <img src={logo} alt="2gis" />
            <span>2gis</span>
            <span>5,0</span>
            <button>88 отзывов</button>
          </div>

          <div className="source">
            <img src={logo1} alt="Яндекс карты" />
            <span>Яндекс карты</span>
            <span>5,0</span>
            <button>88 отзывов</button>
          </div>

          <div className="source">
            <img src={logo2} alt="Google maps" />
            <span>Google maps</span>
            <span>5,0</span>
            <button>88 отзывов</button>
          </div>
        </div>

        <div className="filtr">
          <button>Все отзывы</button>
          <button>Яндекс карты</button>
          <button>Google maps</button>
        </div>

        <div className="cards">
          <div className="card">
            <div className="stars">
              <img src={face1} alt="Дмитрий Салтаев" />
              <div>
                <img src={stars} alt="" />
                <h3>Дмитрий Салтаев</h3>
              </div>
            </div>
            <div className="textRev">
              <p className="god">22 дек. 2025 г.</p>
              <p className="textCar">
                Честность и доверие. Получил ровно ту машину, которую выбрал на
                фото. В идеальном чистом и заправленном состоянии. Прогретая,
                садись и езжай. Она ждала меня возле аэропорта в назначенное
                время ровно как и договаривались. Причём до этого момента я
                ничего не платил и никаких документов не подписывал. Всё на
                доверии. Смело рекомендую!
              </p>
              <button>Показать целиком</button>
              <a href="#">Отзыв из Яндекс карт</a>
            </div>
          </div>

          <div className="card">
            <div className="stars">
              <img src={face2} alt="Дмитрий Салтаев" />
              <div>
                <img src={stars} alt="" />
                <h3>Дмитрий Салтаев</h3>
              </div>
            </div>
            <div className="textRev">
              <p className="god">22 дек. 2025 г.</p>
              <p className="textCar">
                Честность и доверие. Получил ровно ту машину, которую выбрал на
                фото. В идеальном чистом и заправленном состоянии. Прогретая,
                садись и езжай. Она ждала меня возле аэропорта в назначенное
                время ровно как и договаривались. Причём до этого момента я
                ничего не платил и никаких документов не подписывал. Всё на
                доверии. Смело рекомендую!
              </p>
              <button>Показать целиком</button>
              <a href="#">Отзыв из Яндекс карт</a>
            </div>
          </div>

          <div className="card">
            <div className="stars">
              <img src={face3} alt="Дмитрий Салтаев" />
              <div>
                <img src={stars} alt="" />
                <h3>Дмитрий Салтаев</h3>
              </div>
            </div>
            <div className="textRev">
              <p className="god">22 дек. 2025 г.</p>
              <p className="textCar">
                Честность и доверие. Получил ровно ту машину, которую выбрал на
                фото. В идеальном чистом и заправленном состоянии. Прогретая,
                садись и езжай. Она ждала меня возле аэропорта в назначенное
                время ровно как и договаривались. Причём до этого момента я
                ничего не платил и никаких документов не подписывал. Всё на
                доверии. Смело рекомендую!
              </p>
              <button>Показать целиком</button>
              <a href="#">Отзыв из Яндекс карт</a>
            </div>
          </div>
        </div>
      </div>
      <div className="slider">
        <button>‹</button>
        <div className="dots">
          <span></span>
          <p></p>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <button>›</button>
      </div>
    </section>
  );
}

export default Company;
