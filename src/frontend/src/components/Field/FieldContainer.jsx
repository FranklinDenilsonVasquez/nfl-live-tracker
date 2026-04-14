import "./FieldContainer.css";
import PlayerContainer from "../Player/PlayerContainer";
import Field from "./Field"

function FieldContainer({game}){
    const homeLogo = game?.home_team?.logo;
    const awayLogo = game?.away_team?.logo;

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
                            <PlayerContainer/>
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

