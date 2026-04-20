# 享學 CHANGELOG

品牌：**享學**（享受學習 · 學習享受）  
主色：`#6442A1 → #A5B4FC`（紫色漸層，Stripe 框架）

---

## [Unreleased]

### In Progress
- Phase 2：Badge/Tag 元件、Quiz 進度指示、RWD 響應式
- Phase 3：Icon 系統（取代 emoji placeholder）、表單元件
- Logo Direction B（學習漣漪）待深化

---

## [v0.8.0] — 2026-04-20

### Added — 編輯模式（Edit Mode）
- `courses/week4-v2.html` 新增 **編輯模式**（鉛筆 FAB，bottom: 88px）
  - 進入編輯模式後，所有文字區塊（hero、section 標題、步驟卡、Toggle、Callout、Prompt 區、Quiz、圖說）皆可直接 `contenteditable` 內嵌修改
  - 圖片佔位符 hover 出現上傳 overlay，選取本機圖片後以 FileReader base64 嵌入，不需後端
  - 底部滑入 **編輯工具列**：「離開編輯」+ 「下載儲存」兩個按鈕
  - 「下載儲存」：clone 整頁 DOM → 清除編輯標記 → 下載為 `week4-v2.html`（完全離線，無 localStorage）
  - 進入編輯模式時自動退出上課模式，兩種模式互斥

---

## [v0.7.0] — 2026-04-20

### Changed — 版本體系梳理
- 統一版本號：全專案只使用 CHANGELOG 版本，`brand-system-v2.html` 內部不再使用獨立版本號
- `index.html` 全面重寫：分為兩個層次
  - 「現在上課」大卡片（Week 4 v2 為主角）
  - 「所有課程」縱向列表（左）+ 「設計工作台」面板（右）
- 資料夾結構整理：
  - 舊版課件 → `courses/_archive/`（week4-v1, week3-v1）
  - 舊版設計檔 → `design-system/_history/`（brand-system-v1, v2-concept, color-directions-v1, logo-directions-v1, mockup-v3）
- `brand-system-v2.html` sidebar 加入「版本歷程」區塊，可直接連結所有歷史探索檔案

### 版本規則更新
- **唯一版本號**：只有 CHANGELOG.md 的 `v0.x.0` 是官方版本
- 檔名的 `-v1`、`-v2` 是迭代代號，非版本號
- 未來新增內容：更新 CHANGELOG，`index.html` 的版本顯示跟著更新

---

## [v0.6.0] — 2026-04-20

### Added
- `courses/week4-v2.html` 加入左側章節導覽（`.chapter-nav`）
  - 捲過 hero 後淡入，scroll spy 同步 active 狀態
  - 1180px 以下自動隱藏
- `design-system/brand-system-v2.html` 整體升級：
  - 加入 System Intro header（品牌標題 + 4 項數據統計）
  - Section reveal 改為 IntersectionObserver，全頁皆有入場動畫
  - 新增第 12 節 Motion（duration scale、easing curves 可預覽、motion rules）
  - Sidebar 加入 Motion 連結

---

## [v0.5.0] — 2026-04-20

### Added
- `courses/week4-v2.html` — Week 4 NotebookLM 課件全新 Editorial Scroll 設計
  - 70dvh 暗色電影感 hero（radial glow + 網格線 overlay）
  - 智慧 sticky nav（捲超過 50% hero 後滑入，顯示章節名 + 進度條）
  - 無側邊欄，純長捲 editorial 版面
  - Editorial step cards（72px 漸層數字 + 內容，active 時數字全亮）
  - 行內 Toggle、Callout（三種）、Image block 元件
  - Featured dark prompt 區塊（品牌深色背景）
  - 浮動 FAB 上課模式按鈕（右下角固定）
  - 完整 JS：scroll spy、toggle、複製 prompt、quiz、上課模式字放大

### Changed
- `index.html` 更新至 v0.5.0，Week 4 v2 設為主要連結，v1 保留存檔

### Design Decisions
- Tim 確認課件設計方向：**B — Editorial Scroll**（Apple Environment 頁風格）
- Logo 確認使用 Direction C（純字標：享漸層 + 學深色），Direction B 暫存未來

---

## [v0.4.0] — 2026-04-20

### Added
- `design-system/logo-directions-v1.html` — 四個 SVG logo 方向對比頁面
  - Direction A：享字符號化（三元素幾何 mark）
  - Direction B：學習漣漪（同心弧線）
  - Direction C：享學純字標（Apple 路線）
  - Direction D：電影序幕（弧線收斂 + 聚光點）
- `design-system/brand-system-v1.html` — 完整品牌設計系統 HTML（色彩、字型、間距、元件、Motion）

### Brand Foundation Completed
- 品牌哲學：享受學習 · 學習享受
- 人格：暖場者（Hi 大家好）+ 電影導演（序幕即體驗）
- 受眾：職場有活力的年輕人
- 拒絕成為：補習班感、玩具感、企業培訓感、學術機構感
- 學員描述：挺有意思的 · 教不一樣的思考 · 老師好玩
- 設計優先順序：第一印象 A → 操作當下 B → 課後回味 C
- Typography 感：Apple 權威感（C）+ 電影字幕個性（D）

---

## [v0.3.0] — 2026-04-20

### Added
- `design-system/mockup-v3.html` — 設計系統 mockup 第三版（色彩 token 全面更新）
- `specs/2026-04-20-design-system.md` — 品牌設計規格 v1.0 文件

### Changed
- 色彩系統全面更新：所有中性色改為帶藍紫色溫
  - `--brand: #6442A1`（主紫）
  - `--brand-end: #A5B4FC`（淡藍紫，漸層終點）
  - `--brand-dark: #1A1440`
  - 所有中性色（ink / border / bg）加入藍紫色溫
- 漸層統一為 2-stop（移除多段漸層）
- Stripe 框架確立：白底 + 漸層只打關鍵元素

---

## [v0.2.0] — 2026-04-20

### Added
- `design-system/color-directions-v1.html` — 三個漸層方向對比頁面
  - Direction 1：`#6442A1 → #A5B4FC`（清新，**選定**）
  - Direction 2：`#6442A1 → #F9A8D4`（溫暖活潑）
  - Direction 3：`#6442A1 → #FDBA74`（最跳）

### Changed
- `design-system/mockup-v2.html` — 更新為 Stripe 框架（白底為主）

---

## [v0.1.0] — 2026-04-20

### Added
- `design-system/mockup-v1.html` — 初版設計系統 mockup（兩欄式課程版面）
- `courses/week3-v1.html` — Week 3 旅遊場景課件 v1
- `courses/week3-v2.html` — Week 3 旅遊場景課件 v2（版面優化）
- `courses/week4-v1.html` — Week 4 NotebookLM 課件（含上課模式、進度條、Scroll Spy）

---

## 版本號規則

`[主版本].[功能版本].[修補版本]`

- **主版本**：品牌方向重大轉變（通常不會動）
- **功能版本**：新增課件、設計系統重大更新、logo 確定
- **修補版本**：小修正、文案調整、bug 修復
