import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './prediction.css'; // Import the CSS file

const Prediction = () => {
  const [receivedData, setReceivedData] = useState('');

  const initialFormData = {
    bedrooms: '',
    bathrooms: '',
    sqft_living: '',
    floors: '',
    yr_built: '',
  };

  const [formData, setFormData] = useState(initialFormData);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Send the form data using Axios
      const response = await axios.post('http://127.0.0.1:5000/predict_home_price', formData);
      setReceivedData(response.data);
      // Handle the response as needed
    } catch (error) {
      console.error('Error sending form data:', error);
      // Handle errors here
    }
  };

  const handleReset = () => {
    setFormData(initialFormData); // Reset form data to its initial state
  };

  return (
    <div>
      <div className='grid-container'>
        <div className="result-box-container">
            <div>
              <h1 className='blue-hedding'>House price predictor</h1>
            </div>
            <div className='input-container-item'>
            <form onSubmit={handleSubmit}>
                <div className="form-group row">
                    <label htmlFor="bedrooms" className="col-sm-4 col-form-label">Number of bedrooms</label>
                    <div className="col-sm-8">
                    <input
                        type="number"
                        className="form-control"
                        id="bedrooms"
                        name="bedrooms"
                        placeholder="Enter The number of bedrooms"
                        value={formData.bedrooms}
                        onChange={handleChange}
                        required 
                    />
                    </div>
                </div>
                {/* Repeat similar code for other input fields */}
                <div className="form-group row">
                    <label htmlFor="bathrooms" className="col-sm-4 col-form-label">Number of bathrooms</label>
                    <div className="col-sm-8">
                    <input
                        type="number"
                        className="form-control"
                        id="bathrooms"
                        name="bathrooms"
                        placeholder="Enter The number of bathrooms"
                        value={formData.bathrooms}
                        onChange={handleChange}
                        required 
                    />
                    </div>
                </div>
                <div className="form-group row">
                    <label htmlFor="sqft_living" className="col-sm-4 col-form-label">sqft of living room</label>
                    <div className="col-sm-8">
                    <input
                        type="number"
                        className="form-control"
                        id="sqft_living"
                        name="sqft_living"
                        placeholder="Enter The sqft of living room"
                        value={formData.sqft_living}
                        onChange={handleChange}
                        required 
                    />
                    </div>
                </div>
                <div className="form-group row">
                    <label htmlFor="floors" className="col-sm-4 col-form-label">Number of floors</label>
                    <div className="col-sm-8">
                    <input
                        type="number"
                        className="form-control"
                        id="floors"
                        name="floors"
                        placeholder="Enter The number of floors"
                        value={formData.floors}
                        onChange={handleChange}
                        required 
                    />
                    </div>
                </div>
                <div className="form-group row">
                    <label htmlFor="yr_built" className="col-sm-4 col-form-label">Year built</label>
                    <div className="col-sm-8">
                    <input
                        type="number"
                        className="form-control"
                        id="yr_built"
                        name="yr_built"
                        placeholder="Enter The year built"
                        value={formData.yr_built}
                        onChange={handleChange}
                        required 
                    />
                    </div>
                </div>
                {receivedData && 
                    <div className="classification">
                        <h5>Estimated Home Price : </h5>
                        <p>${receivedData.estimated_price}</p>
                    </div>    
                }
                <button type="submit" className="btn btn-primary add-btn">
                    Submit
                </button>
                <button type="button" className="btn btn-outline-primary clear-btn" onClick={handleReset}>
                    Reset
                </button>
            </form>
            </div>

        </div>
      </div>
    </div>
    
  );
};

export default Prediction;
