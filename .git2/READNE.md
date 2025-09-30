# Python Print Examples - Quick Guide

이 저장소는 Python의 다양한 `print()` 사용법을 담은 예제입니다. VS Code(터미널) 및 Jupyter에서 실행하는 방법은 간단히 정리했습니다.

---

### 파일 목록

1.  **main_print_v1.py**
    -   **설명**: 가장 기본적인 `print()` 함수 활용 예제.
    -   **기능**:
        -   기본 출력, 여러 값 출력
        -   f-string / .format() / % 스타일
        -   줄바꿈, end, sep 옵션
        -   간단한 계산 및 함수를 포함한 f-string 활용
    -   **실행 방법**:
        -   Windows: `python main_print_v1.py` (또는 `py main_print_v1.py`)
        -   Mac/Linux: `python3 main_print_v1.py`

2.  **main_print_v2.py**
    -   **설명**: 텍스트를 보기 좋게 출력하기 위해 `rich` 라이브러리를 사용하는 예제.
    -   **기능**:
        -   컬러 및 스타일 출력 (f-string)
        -   패널(박스)을 활용한 멀티라인 출력
        -   테이블 출력 (딕셔너리/리스트 보기 좋게)
    -   **실행 방법**:
        -   `rich` 라이브러리 설치 필요: `pip install rich`
        -   Windows: `python main_print_v2.py`
        -   Mac/Linux: `python3 main_print_v2.py`