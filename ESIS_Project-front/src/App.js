import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Prediction from './components/prediction';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Prediction />} />
      </Routes>
    </Router>
  );
}

export default App;
