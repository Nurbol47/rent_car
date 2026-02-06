import "./reviews.css"
import ico from "../pages/ico.svg";
import ico1 from "../pages/ico1.svg";
import ico2 from "../pages/ico2.svg";
import ico3 from "../pages/ico3.svg";
import ico4 from "../pages/ico4.svg";
import ico5 from "../pages/ico5.svg";

function Reviews() {
  return (
    <div className="container">
      <h1>Почему нам доверяют?</h1>

      <div className="cards">
        <div className="cardRev">
          <div>
            <img src={ico} alt="" />
          </div>
          <h3>Путешествуйте <br /> без ограничений</h3>
          <p>
            Откройте для себя все туристические жемчужины Иркутской области,
            Республики Бурятии и Монголии
          </p>
        </div>

        <div className="cardRev">
          <div>
            <img src={ico1} alt="" />
          </div>
          <h3>Большой суточный <br /> пробег - 250 км</h3>
          <p>
            Максимальная свобода в передвижении без лишних опасений и переплат.
            Фиксированная цена за перепробег
          </p>
        </div>

        <div className="cardRev">
          <div>
            <img src={ico2} alt="" />
          </div>
          <h3>Первый прокат <br /> с кэшбэком</h3>
          <p>
            Получайте реальный кэшбэк за поездки и тратьте его на следующую
            аренду или дополнительные услуги в полном объёме
          </p>
        </div>

        <div className="cardRev">
          <div>
            <img src={ico3} alt="" />
          </div>
          <h3>Надежные авто = ваша <br /> безопасность</h3>
          <p>
            Все автомобили проходят регулярное техническое обслуживание, парк
            постоянно пополняют новинки
          </p>
        </div>

        <div className="cardRev">
          <div>
            <img src={ico4} alt="" />
          </div>
          <h3>Расширенная <br /> страховка</h3>
          <p>
            Наши авто застрахованы по ОСАГО, есть расширенные пакеты
            страхования, для вашей защищённости
          </p>
        </div>

        <div className="cardRev">
          <div>
            <img src={ico5} alt="" />
          </div>
          <h3>Любая форма <br /> оплаты</h3>
          <p>
            Платите удобным для вас способом: наличные, банковской картой, на
            рас. счёт Оф. договор, отчетные документы и чеки
          </p>
        </div>
      </div>
    </div>
  );
}

export default Reviews;
