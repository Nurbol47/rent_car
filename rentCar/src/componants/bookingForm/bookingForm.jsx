import "./style.css";
import { IoHelpCircleOutline } from "react-icons/io5";
import { FaCalendarAlt } from "react-icons/fa";

function BookingForm() {
  return (
    <>
      <div className="form">
        <h1>Бронирование автомобиля</h1>
        <h2>Выберите автомобиль:</h2>
        <select>
          <option>Alfa Romeo (универсал) </option>
        </select>
        <h6>
          стоимость суток: <span>5 400₽</span>
        </h6>
        <h2>Длительность аренды:</h2>
        <div>
          <div className="inputDate">
            <FaCalendarAlt className="icon2" />
            <input type="date" />
          </div>
          <div className="inputDate">
            <FaCalendarAlt className="icon2" />
            <input type="date" />
          </div>
        </div>
        <h2>Дополнительные услуги</h2>
        <div>
          <h6>детское кресло</h6>
          <h6>бесплатно</h6>
          <input type="checkbox" />
        </div>
        <div>
          <h6>мойка авто</h6>{" "}
          <select>
            <option>1300 ₽</option>
          </select>
          <input type="checkbox" className="check" />
        </div>
        <div className="Avtoo">
          <h6>подача авто</h6> <IoHelpCircleOutline className="icon1" />{" "}
          <input type="checkbox" />
        </div>
        <div>
          <div className="inputDate1">
            <input type="time" />
          </div>{" "}
          <h6>город</h6> <input type="radio" /> <h6>аэропорт</h6>{" "}
          <input className="custom-radio" type="radio" />
        </div>
        <div>
          <h3>28.800 ₽</h3> <button>Забронировать</button>
        </div>
      </div>
    </>
  );
}

export default BookingForm;
