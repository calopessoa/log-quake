import { useEffect, useState } from 'react';
import './App.scss';
import MatchCausesSelect from './components/MatchCauses-Select';
import MatchPlayersSelect from './components/MatchPlayers-Select';

import allMatches from './dataJson/allMatches';
import meansOfDeath from './dataJson/meansOfDeath';

function App() {
  const [matches, setMatches] = useState();
  const [deathCauses, setDeathCauses] = useState()

  useEffect(() => {
    setMatches(allMatches);
    setDeathCauses(meansOfDeath);
  }, []);

  return (
    <main className='main-container'>
      <header>
        <h1>Quake 3 Arena</h1>
        <h2>Match Log Viewer</h2>
      </header>
      <h3>Select which data to show (per match):</h3>

      { matches.map((games) => (
        <MatchPlayersSelect
          key={ games.game }
          game={ games.game }
          total-kills={ games.total_kills }
          players={ games.players }
          kills={ games.kills }
        />
      )) }

      { deathCauses.map((causes) => (
        <MatchCausesSelect
          key={ causes.game }
          game={ causes.game }
          deathCauses={ causes.kill_by_means }
        />
      )) }

    </main>
  );
}

export default App;
