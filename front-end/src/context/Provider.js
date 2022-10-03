import { useState, useMemo } from 'react';
import PropTypes from 'prop-types';
import Context from './Context';

function Provider({ children }) {
  const [matches, setMatches] = useState([]);
  const [deathCauses, setDeathCauses] = useState([]);
  const [selected, setSelected] = useState(1);
  const [selectedCauses, setSelectedCauses] = useState(1);

  const value = useMemo(() => (
    {
      matches,
      setMatches,
      deathCauses,
      setDeathCauses,
      selected,
      setSelected,
      selectedCauses,
      setSelectedCauses,
    }
  ), [
      deathCauses, setDeathCauses,
      matches, setMatches,
      selected, setSelected,
      selectedCauses, setSelectedCauses
    ]);

  return (
    <Context.Provider value={ value }>
      { children }
    </Context.Provider>
  );
}

Provider.propTypes = {
  children: PropTypes.objectOf(PropTypes.any),
}.isRequired;

export default Provider;
