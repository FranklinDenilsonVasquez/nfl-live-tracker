import './Header.css'
import SearchBar from './SearchBar';

function Header() {

  const handleSearch = (text) => console.log('User typed: %s', text)
  return (
    <div className="main-div">
      <div className="header">
        <h1 className="h1-header">FootyStats</h1>
        <SearchBar onChange={handleSearch}/>
        <div className="right-buttons">
          <button>About Us</button>
          <button>Gear</button>
        </div>
      </div>
    </div>
  );
}

export default Header;
