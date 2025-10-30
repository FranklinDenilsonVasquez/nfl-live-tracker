import "./FieldContainer.css";

function FieldContainer({team}){
    const teamSelected = team;

    return(
        <div className="field-container">
            <div className="top-endzone">
                {teamSelected ? (<p>Logo Here {teamSelected}</p>):(<p>NFL</p>)}
            </div>
            <div className="bottom-endzone">
                {teamSelected ? (<p>Logo Here {teamSelected}</p>):(<p>NFL</p>)}
            </div>
        </div>
    )

}

export default FieldContainer

