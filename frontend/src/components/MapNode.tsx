import React from 'react';

interface MapNodeProps {
  latitude: number;
  longitude: number;
}

const MapNode = ({ latitude, longitude }: MapNodeProps) => {
  return <div>[longitude, latitude]</div>;
};

export default MapNode;
