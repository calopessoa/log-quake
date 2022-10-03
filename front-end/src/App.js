import { useContext, useEffect } from 'react';
import './App.scss';
import MatchCard from './components/MatchCard';
import MatchCausesSelect from './components/MatchCauses-Select';
import MatchPlayersSelect from './components/MatchPlayers-Select';
import MatchCausesCard from './components/MatchCausesCard';
import Context from './context/Context';

import allMatches from './dataJson/allMatches';
import meansOfDeath from './dataJson/meansOfDeath';

function App() {
  const {
    setMatches, setDeathCauses,
    setSelected, setSelectedCauses } = useContext(Context)

  useEffect(() => {
    setMatches(allMatches);
    setSelected(1);
    setDeathCauses(meansOfDeath);
    setSelectedCauses(1);
  }, []);

  return (
    <main className='main-container'>
      <header>
        <h1>Quake 3 Arena</h1>
        <h2>Match Log Viewer</h2>
      </header>
      <h3>Select which data to show (per match):</h3>

        <MatchPlayersSelect />
        <MatchCard />

        <MatchCausesSelect />
        <MatchCausesCard />

    </main>
  );
}

export default App;
