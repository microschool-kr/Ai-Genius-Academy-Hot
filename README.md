# Ai-Genius-Academy-Spicy
### AI 지니어스 아카데미 매운맛 실습

1. Python 3.7.9 버전 설치 [https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe](https://www.python.org/ftp/python/3.7.9/python-3.7.9-amd64.exe)
2. [https://github.com/microschool-kr/Ai-Genius-Academy-Spicy](https://github.com/microschool-kr/Ai-Genius-Academy-Spicy) 에서 코드 다운로드
3. 압축풀고 파일탐색기에서 google_images_download 폴더 들어간 후 주소창에 cmd 입력해서 터미널 켜고 `pip install .`
4. `googleImg -k 검색어 -l 개수` 으로 실행
> -k 옵션은 검색어(keyword, 키워드)
> -l 옵션은 개수(limit)
5. `pip install labelImg`
6. 터미널에 `labelImg` 입력해서 실행
7. Open Dir 버튼 눌러서 사진 크롤링된 폴더 열기
8. 단축키(바운딩 박스 그리기(w), 라벨 이름 쓰기, 저장(ctrl+s), 이전 이미지(a), 다음 이미지(d)) 이용하여 라벨링 실시
> 이미지 1개마다 xml 파일 1개씩 저장.
> 이미지 파일과 xml 파일의 이름이 같아야함.
9. `pip install numpy=1.18.5 protobuf==3.20 tensorflow==1.15`
10. models/research 폴더 들어가서 주소창 cmd 입력해서 터미널 켜고 `pip install .`
11. `pip install tqdm requests`
12. tensorflow_object_detection_helper_tool 폴더로 이동 후 주소창에 cmd 입력해서 터미널 켜고 `python tfgenerator.py`
13. `python main.py -n 50`
14. model : 4 입력(faster_rcnn_inception_v2_coco), step: 500 입력
15. `python object_detection_test.py` object detection 모델 테스트
16. `cd eval_dir/faster_rcnn_inception_v2_coco`
17. `tensorboard --logdir=./`
18. 인터넷 브라우저 켜고 주소창에 `localhost:6006` 입력
