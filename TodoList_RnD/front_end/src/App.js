// ProductList.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProductList = () => {
  const [cts, setCts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('/api/products/');
        setCts(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {cts.map(product => (
          <li key={product.username}>
            {product.map(pro => (
              <s>{pro.usernam}</s>
            ))}
          </li>
              
        ))}
      </ul>
    </div>
  );
};

export default ProductList;
