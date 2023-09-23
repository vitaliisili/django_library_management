const barrowChart = document.getElementById('barrow-chart');
const libraryChat = document.getElementById('library-chart')
const lentChat = document.getElementById('lent-chart')

new Chart(barrowChart, {
    type: 'bar',
    data: {
        labels: ["January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"],
        datasets: [{
            label: 'Borrowed Books',
            data: [12, 19, 3, 5, 2, 3, 7, 9, 10, 21, 3, 5],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    color: '#26BCFFFF',
                    font: {
                        family: 'Itim, cursive',
                        size: 20
                    }
                }
            }
        },
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#26BCFFFF'
                }
            },
            x: {
                ticks: {
                    color: '#26BCFFFF'
                }
            },
        }
    }
});

new Chart(libraryChat, {
    type: 'doughnut',
    data: {
        labels: ['Borrowed Books', 'Lent Books', 'Library Books'],
        datasets: [{
            label: 'Books',
            data: [12, 19, 5],
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            legend: {
                labels: {
                    color: '#26BCFFFF',
                    font: {
                        family: 'Itim, cursive',
                        size: 16
                    }
                }
            }
        },
        responsive: true,
        maintainAspectRatio: false,
    }
})

new Chart(lentChat, {
    type: 'line',
    data: {
        labels: ["January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"],
        datasets: [{
            label: 'Lent Books Income',
            data: [12, 19, 3, 5, 2, 3, 7, 9, 10, 21, 3, 5],
            // fill: true,
            pointRadius: 4,
            // backgroundColor: '#26BCFFFF',
            // borderColor: 'rgba(255, 148, 132)',
            // borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                labels: {
                    color: '#26BCFFFF',
                    font: {
                        family: 'Itim, cursive',
                        size: 20
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    color: '#26BCFFFF'
                }
            },
            x: {
                ticks: {
                    color: '#26BCFFFF'
                }
            },
        }
    },

})