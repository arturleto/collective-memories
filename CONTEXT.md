# Collective Memories — Флаер & Лендинг | Контекст проекта

## Кто и что

**Артур Лето** (@artur_leto_) — продвигает приложение **Collective Memories** (Web3 фото-приложение).
Суть: обычные люди фотографируют повседневную жизнь на телефон и получают $100–1000/мес.
Никаких вложений, только телефон с камерой.
Инвайт-код: **GQP92** (+1000 ATTN бонус обоим).

---

## Файлы проекта

```
collective_memories_highlights/landing/
├── flyer.html          ← ГЛАВНЫЙ ФАЙЛ — флаер для печати (99×210mm, DL-формат)
├── flyer_side_A.png    ← готовый PNG для типографии, 1169×2481px (300dpi)
├── flyer_side_B.png    ← готовый PNG для типографии, 1169×2481px (300dpi)
├── export_png.js       ← скрипт для генерации PNG через puppeteer
├── index.html          ← лендинг-страница (русский язык)
├── gen_images.py       ← генерация изображений через Vertex AI Imagen
└── assets/
    ├── hero_phone.png
    ├── how_it_works.png
    ├── earnings.png
    ├── community.png
    └── flyer_bg.png
```

---

## Флаер (flyer.html) — текущее состояние

### Формат
- Размер: **99mm × 210mm** (A4 сложенный на треть, DL-формат)
- Тема: тёмная, navy (#030c1a), акценты #00D4FF (cyan) и фиолетовый
- Шрифт: Inter (Google Fonts)
- Фон: CSS-only (radial-gradient orbs + grid texture + dust particles) — без внешних изображений

### Сторона A — текст (3 языковых блока, каждый 70mm)

**Блок 1 — 🇮🇩 Bahasa Indonesia:**
- q-main: "Tahukah kamu ada pekerjaan seperti ini —"
- q-sub: "cukup foto kehidupan di sekitarmu pakai HP?"
- Сумма: $100–1000 per bulan
- Последняя строка: 100.000+ pengguna di seluruh dunia.
- CTA: "Balik & scan QR — aku tunjukkan cara kerjanya."

**Блок 2 — 🇬🇧 English:**
- q-main: "Did you know there's a job like this —"
- q-sub: "just photograph the life around you on your phone?"
- Сумма: $100–1000 per month
- Последняя строка: 100,000+ users worldwide.
- CTA: "Flip & scan the QR — I'll show you how it works."

**Блок 3 — 🇷🇺 Русский:**
- q-main: "А ты знал, что существует такая работа —"
- q-sub: "просто фотографировать жизнь вокруг на телефон?"
- Сумма: $100–1000 в месяц
- Последняя строка: 100.000+ пользователей по всему миру.
- CTA: "Переверни и отсканируй QR — я покажу, как это работает."

**Тело блока (одинаково для всех языков, переведено):**
1. Сумма — без шуток. Могу доказать, напиши мне.
2. Без вложений / Zero investment / Tanpa modal — с underline-подчёркиванием
3. Есть приложение, о котором мало кто знает. Платят за простые кадры как stories.
4. 100.000+ пользователей по всему миру. (highlight-white)

### Сторона B — QR (обратная сторона)

**Верхняя зона (90mm):** большой QR-код 66×66mm + URL

**⚠️ ВАЖНО — QR-КОД НЕ ФИНАЛЬНЫЙ**
Сейчас QR ведёт на: `https://instagram.com/artur_leto_`
Когда купишь домен или определишь финальную ссылку — нужно обновить URL в двух местах:
1. В `flyer.html` найти строку с `api.qrserver.com` и заменить параметр `data=`
2. Обновить текст `.qr-url` (сейчас `instagram.com/artur_leto_`)
3. Перегенерировать PNG: `node landing/export_png.js`

**Нижняя зона (~120mm):** 3 языковых фразы с флагами:
- 🇮🇩 Pelajari cara menghasilkan uang dari stories sehari-hari
- 🇬🇧 Learn how to earn money from everyday stories
- 🇷🇺 Узнай как зарабатывать на обычных сторис

Разделены тонкими градиентными линиями (синий→белый→фиолетовый).

---

## Ключевые CSS-параметры (для ручной правки)

```css
/* Размер карточки */
.flyer { width: 99mm; height: 210mm; }

/* Блок Side A */
.block { padding: 3.2mm 5mm 2.8mm; }
.q-main { font-size: 4.5mm; font-weight: 900; }
.q-sub  { font-size: 3.4mm; font-weight: 800; }
.line   { font-size: 2.5mm; }
.amount { font-size: 3.1mm; color: #00D4FF; }
.cta-bottom { font-size: 2.2mm; font-style: italic; }

/* Блок Side B */
.b-top    { height: 90mm; }          /* зона QR */
.qr-wrap img { width: 66mm; height: 66mm; }
.b-phrase { font-size: 5mm; font-weight: 700; }
.b-flag   { font-size: 8.5mm; }
.b-lang   { padding: 7mm 0; }
```

---

## Как перегенерировать PNG

```bash
cd /Users/artur/Desktop/CLOUDE/collective_memories_highlights
node landing/export_png.js
# → landing/flyer_side_A.png (1169×2481px, 300dpi)
# → landing/flyer_side_B.png (1169×2481px, 300dpi)
```

Требует: Node.js + puppeteer (уже установлен в node_modules).

---

## Git-история ключевых коммитов

```
ebc1a47  feat(flyer): v2 final — unified 3-lang text + larger body fonts
9d38722  feat(landing): flyer v1 — Side A 3 langs + Side B QR with 3-lang CTA
34c6c3a  chore(landing): save full project state
```

Откат к v1 (если нужно): `git checkout 9d38722 -- collective_memories_highlights/landing/flyer.html`

---

## Что ещё нужно сделать

- [ ] **QR-код**: определить финальную ссылку (домен или instagram), обновить в flyer.html, перегенерировать PNG
- [ ] **Лендинг index.html**: перевести на английский и индонезийский (пока только русский)
- [ ] **Печать**: отправить flyer_side_A.png + flyer_side_B.png в типографию (1000 копий, Бали)

---

## Технические детали

- **Vertex AI** для генерации изображений: проект `gen-lang-client-0513605051`, модель `imagen-4.0-generate-001`
- **ADC**: `gcloud auth application-default print-access-token` (аккаунт parslead.bot@gmail.com)
- **Puppeteer**: установлен в `node_modules/puppeteer` в папке collective_memories_highlights
- **Print CSS**: в flyer.html есть `@media print { @page { size: 99mm 210mm; } }` — можно печатать прямо из браузера

---

## Контакты для CTA

- Instagram: **@artur_leto_**
- Инвайт-код: **GQP92**
