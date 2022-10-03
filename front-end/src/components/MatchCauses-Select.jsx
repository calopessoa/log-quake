import { useContext } from "react";
import Context from "../context/Context";

function MatchCausesSelect() {
  const { deathCauses, setSelectedCauses } = useContext(Context);

  function handleChange({ target: { value } }) {
    setSelectedCauses(value);
  }

  return (
  <label className="select-right">Causes of Death

    <select name="select" onChange={ (t) => handleChange(t) }>
    { deathCauses?.map((obj, index) => (
      <option key={index} value={obj.game}>{obj.game}</option>
    )) }
    </select>

  </label>
  )
}

export default MatchCausesSelect
