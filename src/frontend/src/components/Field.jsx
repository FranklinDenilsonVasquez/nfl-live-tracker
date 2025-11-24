import React from "react";
import YardLine from "./YardLine";
import "./Field.css"

const Field = () => {
    const lines = Array.from({length: 10}, (_, i) => i);

    return (
        <div className="field">
            {lines.map((lines, idx) => (
                <YardLine key={idx}/>
            ))}
        </div>
    )
}

export  default Field