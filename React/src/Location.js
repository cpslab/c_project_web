import React from 'react'

const Location = ({loc,handleDeleteButton,className}) => {
const deleteLocation = () =>{
    handleDeleteButton(loc.id);
}
  return (
    <li className={className}>
        <button type="button"className="btn btn-info"onClick={deleteLocation}>削除</button>
        {"latitude: "+loc.location.latitude+" " + "longitude: "+loc.location.longitude}
    </li>
  )
}

export default Location
