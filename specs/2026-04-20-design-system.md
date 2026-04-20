# 享學 Design System — 品牌設計規格

**日期：** 2026-04-20  
**版本：** v1.0  
**狀態：** 待實作

---

## 一、品牌背景

**品牌名稱：** 享學  
**品牌哲學：** 享受學習・學習享受  
**定位：** AI 時代的終身教育品牌，以「好玩、想進去、不是來學習是來玩的」作為設計感受目標  
**核心產品：** 課件（HTML 互動課程素材），供老師在課堂中投影展示，學員在個人裝置上操作

**目標學員：** 中高齡成人（50 歲以上為主）  
**使用情境：** 課堂投影 + 學員個人裝置（平板/手機）並行使用

---

## 二、色彩系統

### 設計原則
- 漸層（紫→淡藍紫）只打在**關鍵元素**：logo mark、active 狀態、CTA 按鈕、步驟數字
- 大面積使用白底，讓顏色有呼吸空間（Stripe 框架）
- 所有中性色帶藍紫色溫，非純灰

### CSS Token

```css
:root {
  /* 品牌色 */
  --brand:        #6442A1;  /* 漸層起點（主紫）*/
  --brand-end:    #A5B4FC;  /* 漸層終點（淡藍紫）*/
  --brand-grad:   linear-gradient(135deg, #6442A1, #A5B4FC);
  --brand-dark:   #1A1440;  /* sidebar 底色 */
  --brand-mid:    #9B87D0;  /* hover / 次強調 */
  --brand-light:  #EEF0FF;  /* 淺背景色塊 */
  --brand-xlight: #FAFBFF;  /* 頁面底色 */

  /* 中性色（帶藍紫色溫）*/
  --ink:          #1A1440;  /* 主文字 */
  --ink-2:        #5A5A7A;  /* 次文字 */
  --ink-3:        #9090B8;  /* 說明 / 佔位文字 */
  --bg:           #FFFFFF;
  --bg-2:         #FAFBFF;
  --border:       #E0E4FF;

  /* 功能色 */
  --green:        #28C76F;
  --green-light:  #E2F8ED;
  --amber:        #FF9F43;
  --amber-light:  #FFF3E0;
}
```

### 漸層使用規則
| 元素 | 使用方式 |
|------|---------|
| Logo mark | `background: var(--brand-grad)` |
| Active nav item | `background: var(--brand-grad)` |
| CTA 按鈕 | `background: var(--brand-grad)` |
| Active 步驟數字圓 | `background: var(--brand-grad)` |
| Active toggle tab | `background: var(--brand-grad)` |
| 文字連結 / 標籤 | 純色 `var(--brand)` |
| 大面積背景 | 禁止使用漸層 |

---

## 三、字型規範

字體堆疊：`-apple-system, BlinkMacSystemFont, 'Noto Sans TC', 'PingFang TC', sans-serif`

| 層級 | 尺寸 | 字重 | 用途 |
|------|------|------|------|
| H1 | 32px | 800 | 課程標題 |
| H2 | 24px | 700 | 章節名稱 |
| H3 | 18px | 600 | 小節標題 |
| Body | **17px** | 400 | 課程內文（投影可讀）|
| Meta | 13px | 500 | 標籤 / 說明 |

**重要：** 課程內文最小 17px，考量中高齡學員視覺需求與投影閱讀距離。

---

## 四、版面結構

### 兩欄式課程頁面（GitBook 型）

```
┌─────────────────────────────────────────────┐
│  Sidebar (240px)  │  Content Area (flex: 1)  │
│  深色 #1A1440     │  白底 #FFFFFF            │
│  ─────────────    │  ─────────────────────── │
│  Logo mark        │  Breadcrumb              │
│  課程名稱          │  H1 課程標題              │
│  ─────────────    │  Meta 資訊               │
│  Week badge       │                           │
│  ─────────────    │  [Content Components]    │
│  Nav items        │                           │
│  (今日章節)        │                           │
│  ─────────────    │                           │
│  Footer           │                           │
└─────────────────────────────────────────────┘
```

**Sidebar 行為：**
- 只顯示當天課程章節（不顯示其他週）
- Active 章節用漸層高亮
- 已完成章節降低透明度

**Content Area：**
- 內距 `padding: 36px 48px`
- 最大寬度無限制，scroll 向下
- 包含所有課程元件

---

## 五、核心元件

### 5.1 Prompt 複製框
學員可一鍵複製 AI Prompt，降低輸入錯誤。

```
┌────────────────────────────────────┐
│ 📋 今日 PROMPT         [複製] ← 漸層按鈕
│                                    │
│ 給我 15 個跟芝加哥旅行相關的...     │
└────────────────────────────────────┘
```
- 背景：`var(--brand-xlight)`
- 左邊框：`4px solid var(--brand)`
- 複製按鈕：漸層，成功後切換為「✓ 已複製」並還原

### 5.2 步驟指示器
引導學員依序完成操作步驟。

- 未到：灰色數字圓 + 淡底
- 進行中：漸層數字圓 + `var(--brand-light)` 底色
- 已完成：綠色 ✓ + 文字降透明度

### 5.3 基礎 / 進階切換
同一概念提供兩種深度的說明，學員自選。

- Tab row：白底圓角框，active 用漸層
- Content body：`var(--bg-2)` 底色

### 5.4 隨堂測驗（Quiz）
驗證學員理解，即時回饋。

- 題目文字 16px / 700
- 選項：白底卡片，hover 帶 `var(--brand-light)`
- 正確：綠色邊框 + 淡綠底
- 錯誤：紅色邊框（不揭露正確答案，讓老師引導）
- 進度追蹤留待 Phase 2（需後端）

### 5.5 圖片 / 截圖區塊
展示操作截圖，附說明文字。

- 佔位：虛線框 + 居中圖示
- 說明：圖片下方斜體 13px

### 5.6 計時器（低優先）
課堂練習倒數。設計預留位置，Phase 2 實作。

---

## 六、元件半徑與陰影

```css
--radius:    12px;   /* 卡片、面板 */
--radius-sm:  8px;   /* 按鈕、小元件 */
--shadow:    0 2px 16px rgba(100,66,161,0.07);
--shadow-md: 0 8px 40px rgba(100,66,161,0.12);
```

---

## 七、設計參考

| 參考 | 借鑑點 |
|------|-------|
| Stripe Docs | 白底 + 漸層只打關鍵元素、清新不沉重 |
| Linear | 中性色帶品牌色色溫、整體視覺統一 |
| GitBook | 兩欄課程導覽結構 |
| Notion | 簡潔的內文排版 |

---

## 八、實作範疇

### Phase 1（當前）
- 靜態 HTML 課件（Week 4 NotebookLM 旅遊場景）
- 所有 5.1–5.4 元件
- 兩欄版面
- 無後端、無登入

### Phase 2（未來）
- 享學 OS 平台：Next.js + Supabase + Google OAuth
- 三角色：Admin / Teacher / Student
- Quiz 進度追蹤
- 計時器

---

## 九、待確認事項

- [ ] 品牌 logo 最終版型（目前以「享」字 mark 替代）
- [ ] 課件是否需要列印友好版本
- [ ] 行動裝置（手機）的響應式斷點策略
