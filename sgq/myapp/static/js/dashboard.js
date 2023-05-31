
(function () {
  'use strict'

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
      backgroundColor: 'rgb(255, 99, 132)'
    }],
  };

  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
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
  });
})()












/* other type
(function () {
  'use strict'

  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: 'pratico',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 3
      },


      {
        label: 'teorico',
        data: [89, 30, 3, 105, 1, 10],
        borderWidth: 3
      }
    ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
})()*/






