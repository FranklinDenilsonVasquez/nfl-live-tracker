import "./FieldContainer.css";
import PlayerContainer from "./PlayerContainer";
import Field from "./Field"

function FieldContainer({team}){
    const teamSelected = team;

    return(
        <div className="field-container">

            <div className="top-endzone">

                {teamSelected ? (<p>Logo Here {teamSelected}</p>):(<p>NFL</p>)}
                </div>
                <Field/>
                    <div>


                        <div className="field-container-defense">
                            {/*<PlayerContainer/>*/}
                        </div>
                        <div className="bottom-endzone">
                            {teamSelected ? (<p>Logo Here {teamSelected}</p>):(<p>NFL</p>)}
                        </div>

                </div>
        </div>
    )

}

export default FieldContainer

