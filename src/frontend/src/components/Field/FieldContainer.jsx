import "./FieldContainer.css";
import PlayerContainer from "../Player/PlayerContainer";
import Field from "./Field"
import {useEffect} from "react";
import useGameStore from "../../store/useGameStore";
import usePlayerStore from "../../store/usePlayersStore";
import seasonSelector from "../SeasonSelector/SeasonSelector";
import {useSeasonStore} from "../../store/seasonStore";


function FieldContainer({game}){
    const homeLogo = game?.home_team?.logo;
    const awayLogo = game?.away_team?.logo;

    const { selectedGameId } = useGameStore();
    const { fetchGamePlayers, fetchGameRoster, players } = usePlayerStore();
    const { selectedSeason } = useSeasonStore();

    useEffect(() => {
        if (selectedGameId) {
            fetchGamePlayers(selectedGameId);
        }
    }, [selectedGameId]);

    //Debugging
    // console.log("Home team QB: ", players?.home_team?.filter(p => p.position === "QB"))
    // console.log("Away QB: ", players?.away_team?.filter(p => p.position === "QB"));
    //
    // console.log("Home team RB: ", players?.home_team?.filter(p => p.position === "RB"))
    // console.log("Away RB: ", players?.away_team?.filter(p => p.position === "RB"));

    return(
        <div className="field-container">

            <div className="top-endzone">

                {awayLogo ? (
                    <div className="endzone-content">
                        <img src={awayLogo} className="endzone-logo" alt={game?.away_team?.team_name}/>
                        <p className="endzone-name">{game.away_team.team_name}</p>
                        <img src={awayLogo} className="endzone-logo" alt={game?.away_team?.team_name}/>
                    </div>
                ) : (<p>NFL</p>)}
            </div>
                    <div className="field-container-padding"></div>
                        <Field/>
                    <div>
                        <div className="field-container-padding">
                            <PlayerContainer players={players} game={game}/>
                        </div>
                        <div className="bottom-endzone">
                            {homeLogo ? (
                                <div className="endzone-content">
                                    <img src={homeLogo} className="endzone-logo" alt={game?.home_team?.team_name}/>
                                    <p className="endzone-name">{game.home_team.team_name}</p>
                                    <img src={homeLogo} className="endzone-logo" alt={game?.home_team?.team_name}/>
                                </div>
                            ) : (<p>NFL</p>)}
                        </div>
                </div>
        </div>
    )

}

export default FieldContainer

