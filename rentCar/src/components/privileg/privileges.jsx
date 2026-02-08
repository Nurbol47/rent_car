import './privileges.css';
import icon1 from './icjn1.svg';
import icon2 from './icjn2.svg';
import icon3 from './icjn3.svg';
import icon4 from './icjn4.svg';

const Privileges = () => {
  return (
    <section className="priv">
      <div className="priv-h">
        <h2>Привилегии для клиентов</h2>
        <p>Копите баллы и получайте скидку на аренду, а также дополнительные привилегии</p>
      </div>

      <div className="priv-grid">
        {/* Левая карточка с фоном */}
        <div className="p-card p-left">
          <div className="badge-y">Скидки на аренду до 15%</div>
          <p>Становится выше с повышением статуса:</p>
          <div className="p-val">от 5% до 15%</div>
            <div/>
        </div><div className='p-top'></div>

        {/* Правая синяя карточка */}
        <div className="p-card">
          <div className='p-top'>
          <div id='kesh'>
            <span>Кэшбек баллами</span>
            <div className='ball'>1 балл = 1р</div>
          </div>
          
          <p>
            Чем чаще арендуете - больше баллов копится на счету и растет статус. Начать их тратить можно СРАЗУ. Вот на что можно потратить бонусы: Аренда авто, детское кресло, Доп водитель, Доставка до места
          </p>

          <h3>На что можно потратить:</h3>

          </div>
          <div className="p-icons">
            <div className="p-item">
              <img src={icon1} alt="Аренда" />
              <span>Аренда авто</span>
            </div>
            <div className="p-item">
              <img src={icon2} alt="Кресло" />
              <span>Детское кресло</span>
            </div>
            <div className="p-item">
              <img src={icon3} alt="Мойка" />
              <span>Мойка авто</span>
            </div>
            <div className="p-item">
              <img src={icon4} alt="Доставка" />
              <span>Доставка</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Privileges;