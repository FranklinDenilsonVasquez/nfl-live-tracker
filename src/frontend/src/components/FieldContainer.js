import "./FieldContainer.css";

function FieldContainer({team}){
    const teamSelected = team;

    return(
        <div className="field-container">
            {teamSelected ? (<p>Selected team {teamSelected}</p>):(<p>Select a team for their schedule</p>)}
        </div>
    )

}

export default FieldContainer

