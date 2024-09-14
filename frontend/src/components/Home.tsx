import React, { useState } from 'react';
import { useEffect } from 'react';
import MapNode from './MapNode';
import MapNodeProps from './MapNode';

const Home = () => {
  const [startPoint, setStartPoint] = useState<MapNodeProps>({});
  const [endPoint, setEndPoint] = useState<typeof MapNode>();
  const [carPoint, setCarPoint] = useState<typeof MapNode>();

  useEffect(() => {
    setStartPoint();
    setEndPoint();
    setCarPoint();
  }, [startPoint, endPoint, carPoint]);

  return (
    <>
      <header>HELLO</header>
    </>
  );
};

export default Home;
