'''
Inflearn, 파이썬 무료 강의 (기본편) - 6시간 뒤면 나도 개발자
Section10. 모듈과 패키지(Module&Package)
6강. pip install
구글에서 pypi에서 만들어진 패키지를 사용해본다.
1)Terminal에서 pip install beautifulsoup4 입력해서 다운로드
2)pip list를 치면 깔려있는 pip list를 보여준다.
3)pip show package명을 치면 패키지 정보를 보여준다.
4)pip install --upgrade package명을 통해 최신 package를 다운할 수 있다.
5)pip uninstall package명을 통해 삭제할 수 있다.
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
