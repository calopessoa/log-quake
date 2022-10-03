import { useContext } from 'react';
import Context from '../context/Context';

function MatchCausesCard() {
  const { selectedCauses, deathCauses } = useContext(Context);

  const playerKillValues = deathCauses[selectedCauses-1] && Object.entries((deathCauses[selectedCauses-1]?.kills_by_means));

  const formatKills = playerKillValues?.reduce((acc, element, index) => {
    return index === playerKillValues.length-1
    ? acc += `${element[0]}: ${element[1]} `
    : acc += `${element[0]}: ${element[1]}, `
  }, '')

  // const topPlayers = deathCauses[selectedCauses-1] && Object.keys((deathCauses[selectedCauses-1]?.kills)).slice(0, 3).join(', ')

  return (
    <>
        <section key={selectedCauses}>
          <div className="card">
              <h4 className="title-card"><span className='card-key'>Game:</span> {deathCauses[selectedCauses-1]?.game}</h4>

              <span className="bigshots">
                <article
                  className="card-info"><span className='card-key'>Kills:</span> {formatKills}
                </article>
              </span>

            </div>
        </section>
    </>
  )
}

export default MatchCausesCard;