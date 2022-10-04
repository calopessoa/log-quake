import { useContext } from 'react';
import Context from '../context/Context';

function MatchCausesCard() {
  const { selectedCauses, deathCauses } = useContext(Context);

  const anyMeans = deathCauses[selectedCauses-1] && Object.entries((deathCauses[selectedCauses-1]?.kills_by_means));

  const formatCauses = anyMeans?.reduce((acc, element, index) => {
    return index === anyMeans.length-1
    ? acc += `${element[0]}: ${element[1]} `
    : acc += `${element[0]}: ${element[1]}, `
  }, '')

  return (
    <>
        <section key={selectedCauses}>
          <div className="card">
              <h4 className="title-card"><span className='card-key'>Game:</span> {deathCauses[selectedCauses-1]?.game}</h4>

              <span className="bigshots">
                <article
                  className="card-info"><span className='card-key'>Kills:</span> {formatCauses}
                </article>
              </span>

            </div>
        </section>
    </>
  )
}

export default MatchCausesCard;