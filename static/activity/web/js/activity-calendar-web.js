// 달력을 가져오는 jquery
function initializeDatepicker() {
    // 오늘 날짜 가져오기
    const today = moment().format("MM/DD/YYYY");

    // 날짜 범위 선택기 설정 및 초기화
    $(".relative-date").daterangepicker(
        {
            opens: "left",
            startDate: today, // 시작 날짜를 오늘 날짜로 설정
            endDate: today, // 종료 날짜도 오늘 날짜로 설정하고 싶다면 여기에도 today 변수를 전달합니다.
        },
        async function (start, end, label) {
            // console.log("A new date selection was made: " + start.format("YYYY-MM-DD") + " to " + end.format("YYYY-MM-DD"));
            date = `${start.format('MM/DD/YYYY')} - ${end.format('MM/DD/YYYY')}`;
            page = 1;
            await getList('', page, date, region, categories, showFinished, ordering, showList);
        }
    );
}

// 페이지 호출 시 초기화 함수 호출
initializeDatepicker();

// 필터 초기화 버튼 클릭 시 날짜 선택기 초기화 및 오늘 날짜로 설정
$(".filter-reset").click(function () {
    // 날짜 선택기 다시 초기화
    initializeDatepicker();
});

// 모든날, 오늘, 이번주, 이번달 선택 시 다시 오늘 초기 세팅으로 돌아가는 설정
$(".date-box").click(function () {
    // 날짜 선택기 다시 초기화
    initializeDatepicker();
});
