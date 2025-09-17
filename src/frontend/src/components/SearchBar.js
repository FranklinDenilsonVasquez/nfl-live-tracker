import React from "react";
import { FaSearch } from "react-icons/fa";
import "./Header.css"

function SearchBar({placeholder, onChange}){

    return (
        <div className="search-wrapper">
            <FaSearch className="search-icon"/>
            <input 
                
                type="search"
                placeholder={placeholder || 'Search'}    
                className="search-input"
                onChange={(e) => onChange(e.target.value)}
            >
            </input>
        </div>
    )
}

export default SearchBar