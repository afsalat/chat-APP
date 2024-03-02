// ProductList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios'; 


const ProductList = () => {

  const [cts, setCts] = useState([]);

  const click = () => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/database_sy/');
        setCts(response.data);
        console.log(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
        console.log('fatching problem')
      }
    };

    fetchData();
  };

  return (
    <div>
      <h1>Products</h1>
      <button onClick={click}>click</button>
      <ul>
        {cts.map(pro => {
          return(
          <li key={pro.name}>
            Name :  {pro}
            <h1>test passed</h1>
          </li>

          
          )
        })}

      {/* <p>username : {cts.username}</p>
      <p>passward : {cts.passward}</p> */}
      </ul>
    </div>
  );
};

export default ProductList;
