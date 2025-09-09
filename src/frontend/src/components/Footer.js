import React from "react";
import "../pages/MainPage.css";

function Footer() {
  const CurrentYear = new Date().getFullYear();
  const CompanyName = "FootStats";

  return (
    <div className="copyright-footer">
      <p>
        &copy; {CurrentYear} {CompanyName}. All rights reserved
      </p>
    </div>
  );
}

export default Footer;
