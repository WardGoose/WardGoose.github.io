// 초기 차트 저장할 변수
let myChart = null;

// 데이터를 불러오는 함수
async function fetchData(filePath) {
    const response = await fetch(filePath);
    const text = await response.text();
    const lines = text.trim().split('\n');
    
    const labels = [];
    const dataPoints = [];
    
    lines.forEach(line => {
        const [date, time, value] = line.split(' ');
        labels.push(`${date} ${time}`);
        dataPoints.push(parseFloat(value));
    });
    
    return { labels, dataPoints };
}

// 차트를 생성하거나 업데이트하는 함수
function updateChart(labels, dataPoints) {
    const ctx = document.getElementById('myChart').getContext('2d');

    // 차트가 이미 있을 경우 삭제
    if (myChart) {
        myChart.destroy();
    }

    // 새로운 차트를 생성
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,  // X축 라벨 (날짜 + 시간)
            datasets: [{
                label: 'Value',
                data: dataPoints,  // Y축 데이터 (값)
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 2,
                fill: true,
                pointRadius: 5,
                pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                tension: 0.2  // 부드러운 곡선
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Date & Time'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Value'
                    },
                    beginAtZero: false
                }
            }
        }
    });
}

// 드롭다운 선택에 따라 차트를 업데이트하는 함수
document.getElementById('fileSelect').addEventListener('change', async function() {
    const selectedFile = this.value;  // 선택된 파일 경로
    const { labels, dataPoints } = await fetchData(selectedFile);  // 데이터를 가져옴
    updateChart(labels, dataPoints);  // 차트 업데이트
});

// 초기 로드 시 기본 파일로 차트 생성
window.onload = async function() {
    const defaultFile = document.getElementById('fileSelect').value;  // 기본 파일 (a.txt)
    const { labels, dataPoints } = await fetchData(defaultFile);  // 데이터를 가져옴
    updateChart(labels, dataPoints);  // 차트 생성
};
