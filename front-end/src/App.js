import { useContext, useEffect } from 'react';
import './App.scss';
import MatchCard from './components/MatchCard';
import MatchCausesSelect from './components/MatchCauses-Select';
import MatchPlayersSelect from './components/MatchPlayers-Select';
import MatchCausesCard from './components/MatchCausesCard';
import Context from './context/Context';

import matches from './dataJson/matches';
import meansOfDeath from './dataJson/meansRedudancy';

function App() {
  const {
    setMatches, setDeathCauses,
    setSelected, setSelectedCauses } = useContext(Context)

  useEffect(() => {
    setMatches(matches);
    setDeathCauses(meansOfDeath);
    setSelected(1);
    setSelectedCauses(1);
  }, [setDeathCauses, setMatches, setSelected, setSelectedCauses]);

  return (
    <main className='main-container'>
      <header>
        <h1>Quake 3 Arena</h1>
        <h2>Match Log Viewer</h2>
      </header>
      <h3>Select which data to show (per match):</h3>

      <section className='box-container'>
        <aside className='content-left'>
          <MatchPlayersSelect />
          <MatchCard />
        </aside>

        <aside className='content-right'>
          <MatchCausesSelect />
          <MatchCausesCard />
        </aside>
      </section>
    </main>
  );
}

export default App;
