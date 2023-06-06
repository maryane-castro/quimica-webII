const config = {
    type: 'scatter',
    data: data,
    options: {
        scales: {
        x: {
            type: 'linear',
            position: 'bottom'
        }
        
        }
    }
};



const labels = [6, 2, 4, 5, 6, 7, 10];
const data = {
  datasets: [{
    label: 'Scatter Dataset',
    data: [{
      x: -10,
      y: 0
    }, {
      x: 0,
      y: 10
    }, {
      x: 10,
      y: 5
    }, {
      x: 0.5,
      y: 5.5
    }],
    backgroundColor: 'rgb(100, 99, 132)',
    borderColor: 'rgb(75, 192, 192)',
    
  }],
};