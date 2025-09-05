#HTML에서 요소 : <P> 내용 </P> 으로 구성
#HTML에서 속성 : 나타내고 싶진 않지만 추가적인 기능 원할때, <p class="editor-note"> my cat </p>
#<p> </p> ->텍스트 문단, <a> </a> -> 다른 페이지로 이동시킴, <img> </img> image의 약자로 src 에서 지정된 그림을 보여주는 태그 

#CSS
#인라인 스타일: HTML 요소 안에 style 속성 값으로 작성
#내부 스타일: head 태그 안에 style태그에 작성
#외부 스타일: 별도 CSS파일 생성 후 HTML link 태그를 사용 해 불러오기
#스타일 적용 우선순위는 인라인>내부>외부

# h1{
#     color: red;
#     font-size: 30px;
    
# }                           

#CSS선택자 종류
#전체 선택자(*): HTML 모든 요소를 선택
# * {
#     color: red;
# }

#요소선택자: 지정한 모든 태그를 선택
# h2{
#     color: orange;
# }
#클래스 선택자('.'(dot)): 주어진 클래스 속성을 가진 모든 요소 선택
#아이디 선택자('#'): 주어진 아이디 속성을 가진 요소 선택, 문서에는 주어진 아이디를 가진 요소가 하나만 있어야함 
#속성 선택자('[]'): 주어진 속성이나 속성값을 가진 모든 요소 선택 

#자손결합자(" "(space)): 첫 번째 요소의 자손요소들 선택: 첫 번째 요소의 자손 요소들 선택 EX)p span은 <p>안에 있는 모든 <span>를 선택 (하위레벨 상관 X)
#자식결합자(">"): 첫번째 요소의 직계 자식만 선택 EX) ul > li 은 <ul> 안에 있는 모든 <li>를 선택 ( 한단계 아래 자식들만)

#CSS 선언 : 어떤 스타일을 적용할지 구체적으로 명시하는 부분
#값의 단위-px,pt,cm 등 : 다른 요소의 영향을 받지 않고 고정된 크기 
#      -%,em,rem,vw,vh 등: 다른요소의 크기에 따라 상대적으로 결정 
#       EX) em은 부모 요소의 font-size를 기준으로 크기가 결정되지만, 부모 요소에 font-size가 없다면 그 상위 부모의 font-size를 상속 받음 
#       EX) rem(Root em)은 부모 요소가 아닌, 최상위 요소의 html의 font-size를 기준으로 크기가 결정됨 

#명시도 : 동일한 요소를 가리키는 2개 이상의 CSS규칙이 있는 경우, 가장 높은 명시도를 가진 selector가 승리하여 스타일이 적용됨 
#Cascade: 계단식/ 한 요소에 동일한 가중치를 가진 선택자가 적용될 때,CSS에서 마지막에 나오는 선언이 사용됨 
#명시도가 높은 순 
#Importance> in-line 스타일 > 선택자: id(#)> class(.class)>요소(p,div ... ) > 소스코드 선언 순서 

#CSS상속 : 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임 (상속O-> TEXT 관련) (상속X-> Box model 관련, Position 관련)
#CSS Box Model: 웹페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델 
# -> 박스 구성요소 : margin(외부 간격)> padding(안쪽 여백)> border(테두리)> content(내용), 실제 내용이 위치하는 영역

#standard CSS box model: 표준 상자 모델에서 width, height 설정하면 이 값은  content box 크기 조정 
#alternative CSS box model: 대체 상자 모델에서 width, height은 실제 상자의 너비, 실제 박스 크기 정하기위해 테두리와 패딩을 조정할 필요 없음 


#---------------------------------------------------------------------------------------------------
#CSS Layout
#CSS Box model -> display 속성 (박스의 화면 배치 방식) #박스 타입에 따라 페이지에서의 배치 흐름과 박스가 동작하는 방식이 달라짐
#Blocke 타입 (하나의 독립된 덩어리처럼 동작하는 요소) /.index{disply: block;} /EX) div
#inline 타입: 문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소  .index{display: inline;}
    #width와 height 속성을 사용할 수 없음 
    #수직방향으로는 다른 요소를 밀어낼 수 없고 수평방향으로는 padding,margin,border가 적용되어 다른 요소를 밀어낼 수 있음 
    #span: 자체적으로 시각적 변화 없고 텍스트 일부를 조작한다. 

#Normal flow: 일반적인 흐름을 변경하지 않은 경우 웹페이지 요소가 배치되는 방식 
#inline=block 타입: Block과 inline 의 특징을 합친 것 (줄 바꿈 없이, 크기를 지정 가능 )
#none 타입

#CSS Position
#CSS layout(각 요소의 위치와 ㄱ크기를 조정하여 웹페이지 디자인 결정)
#CSS Position: 요소를 Normal flow에서 제거하여 다른 위치로 배치하는 것 

#position유형
#1.static: 요소를 Normal Flow에 따라 배치 
#2.relative: 요소를 Normal Flow에 따라 배치, static을 기준으로 이동, top-right-left-bottom속성으로 위치를 조정 다른 요소의 레이아웃에 영향을 주지 않음 
#3.absoulte: 요소를 Normal FLow에서 제거, 가장 가까운 relative 부모 요소를 기준으로 이동(만족하는 부모 요소가 없다면 body태그를 기준으로 함), top-right-bottom-left 속성으로 위치 조정, 차지하는 공간 X
#4.fixed: 요소를 Normal Flow에서 제거, 현재 화면영영을 기준으로 이동, 스크롤 해도 항상 같은 위치에 유지됨 
#5.sticky: relative + fixed 특성을 결합한 속성

#z-index: 요소의 쌓임 순서를 정의하는 속성 z-index 숫자가 클수록 맨 뒤로 감 
#CSS flexbox
#박스 표시(disply)타입 -> outer disply 타입에는 block,inline 타입이 있고 Inner display 타입에는 CSS Flexbox가 있다. 
    #CSS flexbox: 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식 
    #Flexbox 구성요소 
    #1.main axis(주 축): flex item이 배치되는 기본 축
    #2.cross axis(교차 축)): main axis에 수직인 축 
    #3.flex container: 부모요소, 이 컨테이너의 1차 자식 요소들이 flex item이 됨 
    #4.flex item

#Flex Container 관련 속성 
    #display: flex; 로 설정하면 Flex container로 지정됨, flex-item은 주축의 시작선에서 시작되서 기본적으로 행으로 나열됨 
    #flex-direction: flex item이 나열되는 방향을 지정, row(기본 값), column(아이템을 세로 방향으로 위에서 아래로 배치 )

    #flex-wrap: flex item 목록이 flex container의 한 행에 들어가지 않을 경우 다른 행에 배치할 지 여부 설정 
    #         : no-wrap은 줄바꿈을 하지 않음, wrap은 여러 줄에 걸쳐 배치될 수 있게 설정 

    #jusify-content: 주축을 따라 flex item들을 정렬하고 간격을 조정 
    #              :flex-start(기본값)-주 축의 시작점으로 정렬, center, flex-end 

    #align-content: 컨테이너에 여러 줄의 flex item이 있을 때, 그 줄들 사이의 공간을 어떻게 분배할지 지정 
    #.container{
        # flex-wrap: wrap;
        # align-content: center;}

    #align-items: 컨테이너 안에 있는 flex item들의 교차축 정렬 방법을 지정 
        #stretch: 아이템을 교차 축 높이를 꽉 채우도록 늘어남 
        #center: 아이템을 교차 축의 중앙에 맞춰 정렬 

    #align-self: 컨테이너에 안에 있는 flex item들을 교차 축을 따라 "개별적으로" 정렬

#----------------------------------------------------------------------
#CDN: 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 
#   : 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달 
#<p class="mt-5"> Hello, world!</p>
#Semantic Web: 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식 : 요소의 목적과 역할에 집중한다
#외형보다는 요소 자체의 의미에 집중하는 것 Ex) header/nav/main

#OOCSS: 객체 지향적 접근법을 적용하여 CSS를 구성하는 방법론 
#1. 구조와 스킨을 분리-> 컨테이너와 콘텐츠를 분리(객체에 직접 적용하는 대신 객체를 둘러싸는 컨테이너에 스타일을 적용)

#Reset CSS: 모든 HTML 요소 스타일을 일관된 기준으로 재설정 /Normalize CSS: Reset CSS 중 가장 대표적인 방법 
#-----------------------------------------------------------------------------------
#Responsive Web
#Bootstrap Grid system: 웹페이지의 레이아웃을 조정하는 데 사용하는 12개의 칼럼으로 구성된 시스템
#반응형 웹 디자인: #Container,Column,Gutter -> 1개의 row 안에 12개의 column 영역이 구성 
#하나의 Column 안에 또 다른 row 를 넣어보자->Nesting
#Offset으로 Column을 생략해보자 -> offset

#Gutters: Grid system에서 column사이에 여백 영역 
#x축은 padding, y축은 margin으로 여배 생성 
#Grid system breakpoints:
#xs ,sm 576 / md 768 / lg 992 / xl 1200/ xxl 1400


