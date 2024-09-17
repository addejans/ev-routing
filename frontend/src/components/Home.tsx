import React, { useState } from 'react';
import { useEffect } from 'react';
import type { MapNodeProps } from './MapNode';
import MapNode from './MapNode'

const Home = () => {
  const [startPoint, setStartPoint] = useState<MapNodeProps>({
    latitude: 0,
    longitude: 0,
  });
  const [endPoint, setEndPoint] = useState<MapNodeProps>({
    latitude: 0,
    longitude: 0,
  });
  const [carPoint, setCarPoint] = useState<MapNodeProps>({
    latitude: 0,
    longitude: 0,
  });

  useEffect(() => {
    setStartPoint(startPoint);
    setEndPoint(endPoint);
    setCarPoint(carPoint);
  }, [startPoint, endPoint, carPoint]);

  return (
    <>
      <header>
        <h1>This is a map placeholder.</h1>
        <p>Start Location: <MapNode latitude={startPoint.latitude} longitude={startPoint.longitude}/></p>
        <p>End Location: <MapNode latitude={endPoint.latitude} longitude={endPoint.longitude}/></p>
        <p>Car Location: <MapNode latitude={carPoint.latitude} longitude={carPoint.longitude}/></p>
      </header>
    </>
  );
};

export default Home;