import { useState, useEffect } from 'react';
import './App.css';
import LocationList from './LocationList';

function App() {

  const [locations, setLocation] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://c-term.onrender.com/simple/location");
        const datas = await response.json();
        setLocation([...datas])
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, [])

  const handlebuttonClick = async () => {
    try {
      const position = await getCurrentpostion();
      await fetch("https://c-term.onrender.com/simple/location", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ latitude: position.coords.latitude, longitude: position.coords.longitude })
      });
      setLocation((prevLocation) => {
        return [...prevLocation, { location: { latitude: position.coords.latitude, longitude: position.coords.longitude }, id: undefined }];
      });
      reloadPage();
    } catch (error) {
      console.error("位置情報の取得に失敗しました", error);
    }
  }

  const reloadPage = () => {
    window.location.reload();
  }

  const getCurrentpostion = () => {
    return new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject)
    })
  }

  const handleDeleteButton = async (id) => {
    const response = await fetch(`https://c-term.onrender.com/simple/location/${id}`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
    });
    console.log(response.ok)
    if (response.ok) {
      const newLocations = locations.filter((location) => location.id !== id);
      setLocation(newLocations);
    } else {
      console.error("削除に失敗しました: ", response.status);
    }
  };

  return (
    <div>
      <div className='text-center'>
        <button type="button"className="btn btn-info"onClick={handlebuttonClick}>追加</button>
      </div>
      <div className="container" style={{backgroundColor:'#dcdcdc'}}>
        <LocationList locations={locations} handleDeleteButton={handleDeleteButton} />
      </div>
    </div>
  );
}

export default App;
