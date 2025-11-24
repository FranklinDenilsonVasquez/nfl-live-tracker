import cjStroud from "../img/cj_stroud.jpg";

function PlayerButton({imgUrl, className}) {
    return(
        <button
            className={`player-button ${className}`}
            style={{
                backgroundImage: `url(${imgUrl || cjStroud})`,
                backgroundSize: "cover",
                backgroundPosition: "center",
                backgroundRepeat: "no-repeat"
            }}
        />
    );
}

export default PlayerButton
