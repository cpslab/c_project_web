import React from 'react'
import Location from './Location';
const LocationList = ({locations,handleDeleteButton}) => {
  return (
    <>
      <ul>
        {locations.map((loc, index) => (
          <div key={index}>
              <Location className="mt-2" loc={loc} handleDeleteButton={handleDeleteButton}></Location>
          </div>
        ))}
      </ul>
    </>
  );
};

export default LocationList
