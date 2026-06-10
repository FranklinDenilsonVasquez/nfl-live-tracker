// Function that takes in standings data and groups team by division and conference
export function groupStandings(standings) {
  return standings.reduce((acc, team) => {
    const conf = team.conference;
    const div = team.division;

    if (!acc[conf]) {
      acc[conf] = {};
    }

    if (!acc[conf][div]) {
      acc[conf][div] = [];
    }

    acc[conf][div].push(team);

    return acc;
  }, {});
}
