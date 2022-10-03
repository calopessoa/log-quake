import { useContext } from "react";
import Context from "../context/Context";

function MatchPlayersSelect() {
  const { matches, setSelected } = useContext(Context);

  function handleChange({ target: { value } }) {
    setSelected(value);
  }

  return (
  <label className="select-left">Kills per player

    <select name="select" onChange={ (t) => handleChange(t) }>
    { matches?.map((obj, index) => (
      <option key={index} value={obj.game}>{obj.game}</option>
    )) }
    </select>

  </label>
  )
}

export default MatchPlayersSelect;
