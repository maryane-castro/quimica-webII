(function () {
  'use strict'
//----------------

var dados = [
  { x: 1, y: 3 },
  { x: 2, y: 4 },
  { x: 3, y: 5 },
  // Adicione mais pontos de dados de dispersão conforme necessário
]

var regressao = [
  { x: 1, y: 2 },
  { x: 2, y: 3 },
  { x: 3, y: 4 },
  // Adicione mais pontos de dados de linha conforme necessário
]


// Obtenha a referência do elemento de gráfico no HTML
const ctx = document.getElementById('myChart').getContext('2d');

// Dados para o gráfico
const data = {
  datasets: [
    {
      label: 'Dispersão',
      data: dados,
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      type: 'scatter',
    },
    {
      label: 'Linha',
      data: regressao,
      borderColor: 'rgba(54, 162, 235, 1)',
      fill: false,
      type: 'line',
    },
  ],
};

// Crie o gráfico
new Chart(ctx, {
  type: 'scatter', // Use o tipo de gráfico que desejar (scatter, line, etc.)
  data: data,
  options: {
    // Personalize as opções conforme necessário
  },
});




//----

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




