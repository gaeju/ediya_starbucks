# 스타벅스와 이디야 위치 분석

## 프로젝트 개요
![image](https://github.com/gaeju/-/assets/100760127/93c88c18-924e-42a0-8b57-fce28730811c)
'이디야는 스타벅스 옆에 있다'라는 말이 있다 이디야 측에서는 아니라고 이야기 했지만 믿지 않는 사람들이 대다수이다.
*그렇다면 정말로 이디야는 스타벅스 옆에 입지를 선정할까?*
저는 그렇지 않다고 생각합니다. 그래서 이를 증명하기 위한 프로젝트를 진행하였습니다.

## 데이터 수집
데이터 수집은 스타벅스와 이디야 페이지에서 직접 셀레니움을 이용하여 수집하였습니다.
- 스타벅스, 이디야 데이터:
  - 데이터프레임: 스타벅스, 이디야
  -  생성한 컬럼: 'store_name', 'address', 'gu_name', 'lat' ,'lng
  - 스타벅스
  
  ![image](https://github.com/gaeju/-/assets/100760127/abaa8586-3a8d-481d-b401-7a7eb214e870)
  - 이디야
    
  ![image](https://github.com/gaeju/-/assets/100760127/f4cbfa9b-5384-48e0-909f-80bb1370e31a)

- 지하철 위치 데이터: https://observablehq.com/@taekie/seoul_subway_station_coordinate
- 상업 부동산 가격 데이터: http://rtdown.molit.go.kr/
- 유동인구 데이터: https://data.seoul.go.kr/dataList/3/literacyView.do

## eda
부동산 가격에 대한 이디야, 스벅 매장 시각화
![image](https://github.com/gaeju/-/assets/100760127/e108670b-90c5-4017-a594-b11288b37e64)

starbucks와 ediya 구별 매장 개수 비교
![image](https://github.com/gaeju/-/assets/100760127/dc09ffa8-1423-4814-8080-20b8a19815e1)
![image](https://github.com/gaeju/-/assets/100760127/5cd90bc4-4cef-49d8-b2c0-ae356dc2962f)
![image](https://github.com/gaeju/-/assets/100760127/264c0f47-4e37-436d-98c7-41b91ddcf356)

유동인구별 이디야, 스벅 비교
![image](https://github.com/gaeju/-/assets/100760127/101386c7-b3cc-4a0b-938c-a7ed1161d427)
유동인구별 이디야, 스벅 비교 + 지하철
![image](https://github.com/gaeju/-/assets/100760127/fc52eaed-0aea-454c-a8a9-fc6b5bc416bc)


## 결과
folium으로 스벅과 이디야 위치 확인 
1. 이디야는 대체로 골고루 분포되어 있으나 이디야는 대체로 외곽에 더 많이 집중되어 있다.
2. 스타벅스 또한 대체로 골고루 분포되어 있으나 중심지나 서울 중심지에 더욱 집중되어 있었다. 
<br><br><br>
부동산 가격에 대한 이디야와 스벅의 분포
1. 대체로 가격대가 높은 부동산에 경우 육안으로 봤을 때 이디야보다 스타벅스의 분포가 더 높음
2. 스타벅스가 중심지에 더 몰려있는 것과 비슷한 맥락이라고 생각함.
    -> 이디야는 가맹점 운영이 대다수라 금전적인 영향이 꽤 있으나 스타벅스는 모두 직영점 운영이기 때문에 금전적인 영향을 덜 받는 경향이 있을 것이라 추측
    <br><br><br>
barplot과 line plot을 이용한 starbucks와 ediya의 구별 매장 수
- barplot을 확인하였을 때는 강남, 서초, 중구를 제외하고 비슷하다는 생각을 하지 못함
- 더 정확히 비교하기 위해 같은 그래프 안에 starbucks와 ediya에 대한 그래프를 그려주었음
    -> 확실하게 비슷한 양상을 띄긴 했음, 하지만 상권이 활발한 곳에 가게를 냈을뿐이라면 
        스타벅스가 있는 곳에 굳이 이디야가 매장을 냈다고 하기에는 근거가 불충분
        <br><br><br>
유동인구별 이디야, 스벅 비교_folium
- 유동인구가 집중되어 있는 곳에는 이디야와 스벅이 모두 함께 많이 분포 되어 있음
- 하지만 유동인구가 비교적 집중이 되어있지 않은 곳에는 오히려 스타벅스보다 이디야가 좀 더 분포 되어 있는 경향이 있음

<br><br><br>

## 결론
스타벅스 근처에 이디야가 생긴다는 소문의 경우 상권이 좋은 곳에 카페들이 몰리기 때문이라는 결론을 내렸습니다.
만약 스타벅스 근처에 이디야가 생긴다는 소문이 맞을 경우에 스벅이 있는 곳마다 이디야가, 혹은 이디야가 있는 곳마다 스벅이 있어야 맞는데 꼭 그렇지만도 않았습니다. 유동인구가 많은 곳과 역 주변을 제외한 곳의 경우 스벅보다 이디야의 분포가 더 많은 것을 확인하였습니다.
    -> 즉, 이디야는 스타벅스 주변에 매장을 오픈한 것이 아닌 그저 상권이 활발한 곳에 매장을 냈을 뿐
