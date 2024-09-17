import { mapNode } from './mapNode';

export interface routeData {
  location: mapNode;
  action: string;
  distance_to_next: number;
  speed: number;
  travel_time_hours: number;
  charging_time_hours: number;
}
