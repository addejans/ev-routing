import React from 'react';

export interface MapNodeProps {
  latitude: number;
  longitude: number;
}

const MapNode = ({ latitude, longitude }: MapNodeProps) => {
  return (
    <div>
      {' '}
      <blockquote>
        Lat = {latitude}; Lon = {longitude}{' '}
      </blockquote>
    </div>
  );
};

export default MapNode;
