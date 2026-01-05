# 네이버 뉴스 모니터링 v2

이 프로젝트는 기존 뉴스 모니터링 기능에 **집합 검색(AND/OR)** 로직과 **심플한 UX**를 추가한 개선 버전입니다.

## 변경 사항 (v2)
- **AND/OR 검색 모드**:
    - **OR (기본)**: 선택한 각 키워드별로 독립적인 섹션에 결과를 출력합니다.
    - **AND**: 선택한 모든 키워드가 포함된 기사만 하나의 섹션에 결합하여 출력합니다.
- **UX 심플화**:
    - 뉴스 검색 완료 시, 복잡한 설정창을 숨기고 검색 조건 요약 문구와 결과만 노출합니다.
    - `선택 해제` 버튼을 통해 즉시 초기 검색 설정 화면으로 돌아갈 수 있습니다.
- **요약 문구**: `"a", "b", "c" 키워드가 포함된 언제부터 언제까지의 뉴스 기사입니다.` 형태의 안내 문구를 제공합니다.

## 로컬 실행 방법
1. **의존성 설치**
   ```bash
   pip install -r requirements.txt
   ```
2. **API 키 설정**
   부모 폴더의 `.env`를 그대로 활용하거나, 현재 폴더에 생성합니다.
3. **서버 실행**
   ```bash
   python local_server.py
   ```

## Vercel 배포 방법 (상세 단계)

사내 URL 공유를 위해 Vercel에 배포하는 구체적인 방법입니다.

### 1단계: 프로젝트 업로드
- 작성된 소스 코드를 GitHub, GitLab 또는 Bitbucket 저장소에 Push합니다.
- (참고) `news_dashboard_v2` 폴더가 저장소의 루트이거나, 전체 폴더를 올린 후 Vercel 설정에서 폴더를 지정할 수 있습니다.

### 2단계: Vercel에서 프로젝트 가져오기
1. [Vercel Dashboard](https://vercel.com/dashboard)에 접속하여 **[+ New Project]** 버튼을 클릭합니다.
2. 코드가 올라간 저장소(Repository)를 연결하고 **[Import]**를 클릭합니다.

### 3단계: 프로젝트 설정 (중요)
1. **Root Directory**: 
   - 만약 전체 `naver_api` 폴더를 통째로 올렸다면, `Edit` 버튼을 눌러 `news_dashboard_v2` 폴더를 선택해야 합니다.
   - 해당 폴더 내에 `index.html`과 `api/` 폴더가 있어야 정상 작동합니다.
2. **Environment Variables**:
   - `Environment Variables` 섹션을 확장합니다.
   - **Key**: `NAVER_CLIENT_ID`, **Value**: (본인의 클라이언트 ID) 입력 후 `[Add]`
   - **Key**: `NAVER_CLIENT_SECRET`, **Value**: (본인의 클라이언트 시크릿) 입력 후 `[Add]`

### 4단계: 배포 실행
- 하단의 **[Deploy]** 버튼을 클릭합니다.
- 배포가 완료되면 생성된 `https://...vercel.app` 형태의 URL을 복사하여 사내에 공유하면 됩니다.
