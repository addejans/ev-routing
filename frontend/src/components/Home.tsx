import React, { useState } from 'react';

const Home = () => {

    [startPoint, setStartPoint] = useState();
    [endPoint, setStartPoint] = useState();
    [carPoint, setCarPoint] = useState();

    return (
    <>
        <Map
            startPoint={startPoint}
            endPoint={endPoint}
            carPoint={carPoint}
         />
    </>
    )
};

export default Home;