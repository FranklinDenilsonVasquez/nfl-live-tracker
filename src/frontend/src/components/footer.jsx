
function Footer(){
    const CurrentYear = new Date().getFullYear();
    const CompanyName = "FootballMod" //Place holde

    return (<Footer>
        <p>&copy; {CurrentYear} {CompanyName}. All rights reserved.</p>
    </Footer>)
}

export default Footer