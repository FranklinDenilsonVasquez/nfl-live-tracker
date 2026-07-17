import "./Header.css";
import SearchBar from "../SearchBar/SearchBar";
import { FaGithub, FaLinkedin } from "react-icons/fa";

function Header() {
  const handleSearch = (text) => console.log("User typed: %s", text);
  return (
    <div className="main-div">
      <div className="header">
        <h1 className="h1-header">GridironHQ</h1>
        {/* <SearchBar onChange={handleSearch} /> */}
        <div className="right-buttons">
          <a
            className="info-button"
            href="https://www.linkedin.com/in/franklin-vasquez-5b831333a/"
          >
            <FaLinkedin />
          </a>
          <a
            className="info-button"
            href="https://github.com/FranklinDenilsonVasquez"
          >
            <FaGithub />
          </a>
        </div>
      </div>
    </div>
  );
}

export default Header;
