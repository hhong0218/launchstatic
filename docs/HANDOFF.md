# LaunchStatic — Handoff (2026-06-19)

인수인계 문서. 다음 담당자가 바로 운영·배포·분석 설정을 이어갈 수 있도록 현재 상태와 미완료 항목을 정리했습니다.

---

## 1. 한 줄 요약

**LaunchStatic**은 indie hacker용 정적 랜딩 템플릿·가이드 사이트입니다. 빌드 없이 HTML/CSS/JS만으로 Cloudflare Pages에 배포됩니다. **프로덕션은 이미 라이브**이며, GitHub `main`과 동기화되어 있습니다.

---

## 2. 라이브 URL

| 항목 | URL |
|------|-----|
| 프로덕션 (Pages) | https://launchstatic.pages.dev |
| 커스텀 도메인 (설정 중) | https://launchstatic.matchiq.co.kr |
| GitHub | https://github.com/hhong0218/launchstatic |
| Cloudflare Pages 대시보드 | https://dash.cloudflare.com/75c4898a1b8e3213936e24322485e741/pages/view/launchstatic |
| Web Analytics 설정 | https://dash.cloudflare.com/75c4898a1b8e3213936e24322485e741/pages/view/launchstatic/metrics |

---

## 3. Git / GitHub 상태

- **기본 브랜치:** `main` (원격과 동기화 완료)
- **최신 커밋:** `0ce6abe` — `fix: analytics works without GA4 account`
- **머지 필요 여부:** 없음 (다른 브랜치·열린 PR 없음)
- **원격 `scripts/` 폴더:** 아래 파일 포함해 푸시됨
  - `enable-web-analytics.ps1` — Web Analytics 원클릭 설정 + 폴링
  - `enable-web-analytics.py` — 동일 기능 Python 버전
  - `inject-analytics.py` — GA4/쿠키 배너 HTML 주입
  - 기타 콘텐츠 빌드·검증 스크립트

```bash
git clone https://github.com/hhong0218/launchstatic.git
cd launchstatic
git pull origin main
```

---

## 4. 배포 방법

### A. 로컬에서 즉시 배포 (현재 동작 중)

Wrangler OAuth 로그인이 되어 있으면:

```bash
npx wrangler pages deploy . --project-name=launchstatic --branch=main
```

### B. GitHub Actions 자동 배포 (현재 실패)

워크플로: `.github/workflows/deploy.yml`  
`push` → `main` 시 Cloudflare Pages 배포 시도.

**실패 원인:** GitHub Secrets에 `CLOUDFLARE_ACCOUNT_ID`만 있고 **`CLOUDFLARE_API_TOKEN`이 없음**.

**수정 방법:**

1. Cloudflare → My Profile → API Tokens → Create Token
2. 템플릿: **Edit Cloudflare Workers** 또는 Custom → **Cloudflare Pages: Edit**
3. GitHub repo → Settings → Secrets → Actions:
   - `CLOUDFLARE_API_TOKEN` = 위 토큰
   - `CLOUDFLARE_ACCOUNT_ID` = `75c4898a1b8e3213936e24322485e741`
4. Actions에서 **Deploy to Cloudflare Pages** 워크플로 재실행

### C. Cloudflare Git 연동 (선택)

대시보드에서 repo 연결 시 `main` 푸시마다 자동 배포. 빌드 명령 **비움**, 출력 디렉터리 **`/`**.

---

## 5. Analytics (2026-06-19 기준)

### 현재 동작

| 항목 | 상태 |
|------|------|
| Google Analytics 4 | **비활성** — `assets/js/analytics-config.js`에 ID 없음 |
| 쿠키 배너 | GA4 미설정 시 **숨김** (`main.js`) |
| Cloudflare Pages Metrics | 대시보드에서 **즉시 확인 가능** (별도 GA 불필요) |
| Cloudflare Web Analytics (상세) | **미활성** — Metrics 탭에서 Enable 필요 |

### GA4 없이 트래픽 보기

Cloudflare 대시보드 → **launchstatic** → **Metrics**  
요청 수·고유 방문 등 기본 지표 확인.

### Web Analytics 상세 통계 켜기 (권장, 1분)

```powershell
powershell -ExecutionPolicy Bypass -File scripts\enable-web-analytics.ps1
npx wrangler pages deploy . --project-name=launchstatic --branch=main
```

또는 Metrics URL에서 **Enable** 클릭 후 재배포.  
Enable 후 HTML `</body>` 직전에 Cloudflare beacon이 자동 삽입됩니다.

### GA4를 나중에 쓸 때

1. https://analytics.google.com 에서 속성·웹 스트림 생성
2. Measurement ID (`G-...`) 복사
3. `assets/js/analytics-config.js`:

```javascript
window.LS_GA_MEASUREMENT_ID = 'G-YOUR_REAL_ID';
```

4. 배포 → 쿠키 배너 표시 → Accept 후 GA4 수집

상세: `docs/GOOGLE-ANALYTICS-SETUP.md`

### 관련 파일

| 파일 | 역할 |
|------|------|
| `assets/js/analytics-config.js` | CF 토큰·GA4 ID 설정 |
| `assets/js/analytics.js` | CF Web Analytics + GA4(동의 후) 로더 |
| `assets/js/main.js` | 쿠키 배너 (GA4 있을 때만 표시) |
| `scripts/enable-web-analytics.ps1` | Web Analytics API/대시보드 설정 |
| `scripts/inject-analytics.py` | HTML에 analytics 스크립트·배너 일괄 주입 |

---

## 6. Cloudflare 계정 정보

| 항목 | 값 |
|------|-----|
| Account ID | `75c4898a1b8e3213936e24322485e741` |
| Pages 프로젝트 | `launchstatic` |
| Production branch | `main` |
| GitHub owner/repo | `hhong0218/launchstatic` |

로컬 Wrangler OAuth: `%USERPROFILE%\.wrangler\config\default.toml`  
(RUM/Web Analytics API는 OAuth 스코프 부족 시 403 — 대시보드 Enable 사용)

---

## 7. 사이트 구조 (핵심)

```
launchstatic/
├── index.html              # 마케팅 홈
├── templates/              # 템플릿 카탈로그
├── demos/                  # 라이브 프리뷰
├── downloads/              # 단일 HTML 다운로드
├── deploy-guides/          # 배포 가이드
├── guides/, how-to/, blog/ # 콘텐츠 허브
├── assets/js|css/          # 공통 리소스
├── scripts/                # 빌드·배포·analytics 스크립트
├── docs/                   # 운영·정책·핸드오프 문서
└── .github/workflows/      # CI (Pages deploy, DNS setup)
```

콘텐츠 재생성: `python scripts/build-content.py`  
링크 검사: `python scripts/check-links.py`  
로컬 미리보기: `python -m http.server 8080`

---

## 8. 완료된 작업 (이번 세션)

- [x] GA4 없이도 사이트·배포 정상 동작
- [x] 쿠키 배너 — GA4 설정 전 숨김
- [x] Cloudflare Web Analytics 연동 코드·설정 스크립트 추가
- [x] `scripts/` 폴더 GitHub 푸시
- [x] Wrangler로 프로덕션 재배포
- [x] `.wrangler/` gitignore

---

## 9. 미완료 / 다음 담당자 TODO

| 우선순위 | 작업 | 참고 |
|----------|------|------|
| **P0** | GitHub Secret `CLOUDFLARE_API_TOKEN` 등록 | Actions 배포 복구 |
| **P1** | Metrics → Web Analytics **Enable** + 재배포 | `scripts/enable-web-analytics.ps1` |
| **P1** | `launchstatic.matchiq.co.kr` DNS·SSL 최종 확인 | `docs/CUSTOM-DOMAIN-GUIDE.md` |
| **P2** | Google Search Console 속성·sitemap 제출 | `docs/GSC-SUBMISSION.md` |
| **P2** | GA4 속성 생성 (선택) | `docs/GOOGLE-ANALYTICS-SETUP.md` |
| **P3** | Formspree 실 ID 연결 (뉴스레터 폼) | `how-to/add-formspree-to-static-site.html` |
| **P3** | AdSense 사전 점검 | `docs/ADSENSE-PRE-APPLICATION.md` |

30일 운영 플랜: `docs/30-DAY-OPERATIONS.md`  
마스터 리포트: `docs/LS-MASTER-REPORT.md`

---

## 10. 자주 쓰는 명령어

```bash
# 배포
npx wrangler pages deploy . --project-name=launchstatic --branch=main

# Web Analytics 설정 시도
powershell -File scripts/enable-web-analytics.ps1

# 사이트 검증
python scripts/validate-site.py
python scripts/check-links.py

# analytics HTML 일괄 주입 (배너·스크립트)
python scripts/inject-analytics.py
```

---

## 11. 문의·라이선스

- 연락: hello@launchstatic.dev
- 템플릿 MIT: `docs/MIT-LICENSE.txt`
- 사이트 콘텐츠 © LaunchStatic

---

*마지막 업데이트: 2026-06-19 · 커밋 `0ce6abe` 기준*