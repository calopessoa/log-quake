import { useContext } from 'react';
import Context from '../context/Context';

function MatchCard() {
  const { selected, matches } = useContext(Context);

  const playerKillValues = matches[selected-1] && Object.entries((matches[selected-1]?.kills));

  const formatKills = playerKillValues?.reduce((acc, element, index) => {
    return index === playerKillValues.length-1
    ? acc += `${element[0]}: ${element[1]} `
    : acc += `${element[0]}: ${element[1]}, `
  }, '')

  const topPlayers = matches[selected-1] && Object.keys((matches[selected-1]?.kills)).slice(0, 3).join(', ')

  return (
    <>
        <section key={selected}>
          <div className="card">
              <h4 className="title-card"><span className='card-key'>Game:</span> {matches[selected-1]?.game}</h4>

              <article
                className="all-kills"><span className='card-key'>Total Kills:</span> {matches[selected-1]?.total_kills}
              </article>

              <span className="bigshots">
                <article
                  className="card-info"><span className='card-key'>Players:</span> {matches[selected-1]?.players.join(', ')}
                </article>
                <article
                  className="card-info"><span className='card-key'>Kills:</span> {formatKills}
                </article>
                <article className="card-info"><span className='card-key'>Top Players:</span> {topPlayers}</article>
              </span>

            </div>
        </section>
    </>
  )
}

export default MatchCard;
