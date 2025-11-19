import "./Footer.css";

function Footer() {
  const CurrentYear = new Date().getFullYear();
  const CompanyName = "FootballMod"; // Placeholder

  return (
    <footer className="copyright-footer">
      <p>&copy; {CurrentYear} {CompanyName}. All rights reserved.</p>
    </footer>
  );
}

export default Footer;
