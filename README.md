# Open API Practice

Streamlit으로 만든 두 가지 Open API 실습 앱입니다. 사이드바에서 서비스를 선택할 수 있습니다.

- **Explore Artworks**: MET Museum API로 작품을 검색하고 이미지와 작품 정보를 확인합니다.
- **Weather Map**: 지도에서 위치를 클릭하면 Open-Meteo API로 시간별 기온을 확인합니다.

## 로컬 실행

Python 3.12 환경을 권장합니다.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

각 서비스를 별도로 실행하려면 `streamlit run met_app.py` 또는 `streamlit run weather_map.py`를 사용하세요.

## Streamlit Community Cloud 배포

[Streamlit Cloud 배포 화면 열기](https://share.streamlit.io/deploy?repository=jjihh%2Fopen-api-practice&branch=main&mainModule=streamlit_app.py)

배포 화면에서 다음 값을 확인하고 **Deploy**를 클릭하세요.

| 항목 | 값 |
| --- | --- |
| Repository | `jjihh/open-api-practice` |
| Branch | `main` |
| Main file path | `streamlit_app.py` |
| Python version | `3.12` |

별도 API 키나 Secrets 설정은 필요하지 않습니다. 배포가 완료되면 Streamlit Cloud에서 실제 앱 URL을 확인할 수 있습니다.

## 데이터 출처

- [The Metropolitan Museum of Art Collection API](https://metmuseum.github.io/)
- [Open-Meteo](https://open-meteo.com/) — 비상업적 이용 기준
