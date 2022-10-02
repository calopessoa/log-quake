import { useContext } from "react";
import Context from "../context/Context";

function MatchPlayersSelect(key, game, totalkills, players, kills) {
  const { matches } = useContext(Context);

  return (
  <label>Kills per player

    <select name="select">
    { matches.map((obj) => (
      <option value={obj.game}>{obj.game}</option>
    )) }
    </select>

  </label>
  )
}

export default MatchPlayersSelect;
