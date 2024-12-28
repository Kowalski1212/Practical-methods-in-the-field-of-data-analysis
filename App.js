import './App.css';
import { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

function App() {
  const [filters, setFilters] = useState({
    name: '',
    minPrice: '',
    maxPrice: '',
    availability: '',
    tag: '',
  });
  const [results, setResults] = useState([]);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFilters({ ...filters, [name]: value });
  };

  const handleSearch = () => {
    const query = Object.keys(filters)
      .filter((key) => filters[key])
      .map((key) => `${key}=${encodeURIComponent(filters[key])}`)
      .join('&');

    fetch(`http://127.0.0.1:8000/filter_models?${query}`, {
      method: 'GET',
    })
      .then((response) => response.json())
      .then((data) => setResults(data))
      .catch((error) => console.error('Error:', error));
  };

  return (
    <div className="App">
      <h1>Поиск языковых моделей</h1>

      <div className="filters">
        <TextField
          label="Название"
          name="name"
          value={filters.name}
          onChange={handleInputChange}
        />
        <TextField
          label="Минимальная цена"
          name="minPrice"
          type="number"
          value={filters.minPrice}
          onChange={handleInputChange}
        />
        <TextField
          label="Максимальная цена"
          name="maxPrice"
          type="number"
          value={filters.maxPrice}
          onChange={handleInputChange}
        />
        <TextField
          label="Доступность (true/false)"
          name="availability"
          value={filters.availability}
          onChange={handleInputChange}
        />
        <TextField
          label="Тег"
          name="tag"
          value={filters.tag}
          onChange={handleInputChange}
        />

        <Button variant="contained" onClick={handleSearch}>Искать</Button>
      </div>

      <div className="results">
        <h2>Результаты</h2>
        {results.map((result, index) => (
          <div key={index} className="result-item">
            <p><strong>Название:</strong> {result.name}</p>
            <p><strong>Описание:</strong> {result.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;

