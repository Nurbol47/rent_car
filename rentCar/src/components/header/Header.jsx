import "./style.css";
import Img from "./logo1.svg";
import Img2 from "./phoneico.svg";
import Tg from "./tg.svg";
import Wa from "./wa.svg";
import Sun from "./Vector.svg";

export default function Header() {
  return (
    <>
      <header>
        <div className="header">
          <img src={Img} alt="logo" className="logo"/>
          <nav>
            <a href="/">Автопарк</a>
            <select>
              <option>Услуги</option>
            </select>
            <select>
              <option>О нас</option>
            </select>
            <a href="#">Акции</a>
            <a href="#">Достопримечательности</a>
          </nav>
          <div className="tel">
            <a href="#">
              <img src={Img2} alt="tel" />
            </a>
            <a href="#" className="numb">+7(924)3543333</a>
            <a href="#">
              <img src={Tg} alt="Tg" />
            </a>
            <a href="#">
              <img src={Wa} alt="Wats" className="wats"/>
            </a>
          </div>
          <div className="btn">
            <button>
              <img src={Sun} alt="sun" />
              Светлая тема
            </button>
          </div>
        </div>
      </header>
    </>
  );
}
