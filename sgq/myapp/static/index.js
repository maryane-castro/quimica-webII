//bugado
(() => {
'use strict'

feather.replace({ 'aria-hidden': 'true' })

// Graphs
const ctx = document.getElementById('myChart')
// eslint-disable-next-line no-unused-vars

const myChart = new Chart(ctx, {
    type: 'line', //line
    data: {
    labels: nm,
    datasets: [{
        data: dt,
        lineTension: 0,
        backgroundColor: '#fff',
        borderColor: '#007bff',
        borderWidth: 3,
        pointBackgroundColor: '#007bff'
    }]
    },
    options: {
    plugins: {
        legend: {
        display: false
        },
        tooltip: {
        boxPadding: 3
        }
    }
    }
})
})()




const DATA_COUNT = 7;
const NUMBER_CFG = {count: DATA_COUNT, min: -100, max: 100};
const data = {
  labels: Utils.months({count: DATA_COUNT}),
  datasets: [
    {
      label: 'Dataset 1',
      data: Utils.numbers(NUMBER_CFG),
      fill: false,
      borderColor: Utils.CHART_COLORS.red,
      backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
    },
  ]
};


const config = {
    type: 'line',
    data: data,
    options: {
      plugins: {
        legend: {
          title: {
            display: true,
            text: 'Legend Title',
          }
        }
      }
    }
  };
