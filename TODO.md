# Vodo-topo Kobliha – TODO

Aktualizováno: 16. 10. 2026

## Potvrzeno zadavatelem

- [x] **Firemní údaje a kontakty** zveřejněné na webu potvrzeny zadavatelem (15. 10. 2026).
- [x] **Nabídka služeb, cíloví zákazníci a text sekce „O nás“** v aktuální podobě potvrzeny zadavatelem (15. 10. 2026). Nezveřejňovat neověřené doplňující sliby o minimální velikosti zakázek či servisu cizích instalací.
- [x] **Reference** – zadavatel potvrdil zveřejněné názvy projektů, stavy, rozsahy prací, počty bytů a uvedené finanční objemy (15. 10. 2026).
- [x] **Fotografie referencí a jejich použití** potvrzeny zadavatelem (15. 10. 2026). Jde o jeho potvrzení; nezávislé licenční posouzení ani písemné souhlasy nemáme v podkladech.
- [x] Doplněny konkrétní popisky všech šesti projektů, včetně 255 bytů u plánovaného TopTower.
- [x] Odstraněna orientační hodnota zakázky TopTower z webu (15. 10. 2026).
- [x] Sjednocen text patičky na „Vodoinstalace · Topení · Servis“ a upraven úvod sekce Reference.

## Statický audit zdrojového kódu – dokončeno 16. 10. 2026

- [x] Doplněna předávací/provozní dokumentace v `README.md`: architektura, nasazení přes GitHub a Cloudflare, důležité SEO adresy, bezpečné úpravy a zásady ochrany mobilního vzhledu (16. 10. 2026).
- [x] Kontrola struktury HTML: jediný H1, bez duplicitních ID, uzavřené hlavní HTML sekce.
- [x] Ověření interních odkazů, kotvicích cílů a SVG ikon: v aktuálním kódu bez chybějících odkazů.
- [x] Kontrola JSON-LD organizace, canonical, robots meta, sitemap, Google a Seznam ověřovacího kódu.
- [x] Všech šest referenčních fotografií má atributy alt a rozměry; lokální soubory pro favicon, sociální náhled a úvodní grafiku jsou přítomné v repozitáři.
- [x] Přehled responzivních pravidel a zachování mobilního menu v kódu; reálné vykreslení v prohlížečích zůstává k otestování.
- [x] **Optimalizace a lokální hosting fotografií:** GitHub Actions 16. 10. úspěšně stáhly pět unikátních referenčních fotografií a pozadí patičky, převedly je na 10 verzovaných WebP souborů v `assets/optimized/`, pro šest karet nastavily lokální `src`, pro velké karty také `srcset`/`sizes`. Všechny externí URL fotografií i externí CSS obrázek odstraněny ze zdrojového kódu. Přidány cache hlavičky (rok, immutable). Potvrzeno commitem `ea4eaa2`; atribuce a vzhled v CSS beze změn. **Zbývá ověřit deploy/živou produkci a zopakovat PageSpeed.**

## Technické kontroly – zbývá dokončit

- [x] **TopTower na produkci:** zadavatel 15. 10. 2026 ověřil, že na ostrém webu už není uvedena cena budoucí zakázky. (Kontrola přesné verze/commit ID Cloudflare nebyla nezávisle provedena.)
- [ ] **Doména a DNSSEC:** po dokončení automatické aktivace DNSSEC v CZ.NIC znovu ověřit veřejné DNS, dostupnost `https://vodotopokobliha.cz/`, platnost HTTPS a doručování pošty. DNSSEC byl 15. 10. ve stavu Pending; na 16. 10. je již naplánována kontrola. Nezasahovat preventivně do DNS.
- [ ] **Přesměrování:** ověřit trvalé 301/308 přesměrování `www.vodotopokobliha.cz` → `https://vodotopokobliha.cz/`.
- [ ] **Lokální obrázky v produkci:** po Cloudflare Pages deploymentu ověřit, že se všech šest fotografií a pozadí patičky načítají jako `/assets/optimized/*.webp` bez 404, že zůstaly ořezy a nedeformuje se rozložení mobil/tablet/desktop. Na GitHubu již vše ověřeno.
- [ ] **Funkčnost v produkci:** ověřit fotografie, `/favicon.svg`, `/apple-touch-icon.png`, `/assets/social-preview.png`, `/robots.txt`, `/sitemap.xml`, telefonní a e-mailové odkazy. **Kontrola repozitáře 16. 10.:** místní obrázky existují, odkazy na sekce vedou na existující ID, SEO metadata a jeden H1 jsou v kódu správně. Veřejné HTTP odpovědi se zatím z kontrolního prostředí nepodařilo změřit.
- [ ] **Responzivita:** otestovat navigaci, kotvy, karty a kontakty na mobilu (včetně 320–390 px), tabletu a desktopu; Safari na iPhonu, Firefox, Edge a Chrome.
- [x] **PageSpeed Insights – mobil, 16. 10. 2026:** Lighthouse Performance **85**, Accessibility **95**, Best Practices **96**, SEO **100**; FCP ~**2,6 s**, LCP **3,9 s**, Speed Index **2,6 s**, TBT **0 ms**, CLS **0,002**. Jde o laboratorní měření (bez dat skutečných uživatelů).
- [x] **Cloudflare Fonts:** zapnutí potvrzeno uživatelem 16. 10. 2026. Následný mobilní Lighthouse audit ukazuje doručování dvou souborů fontů přímo z `vodotopokobliha.cz` (~163 ms / 30,90 KiB a ~138 ms / 27,80 KiB), bez dalšího externího originu k preconnect; nejdelší kritická síťová cesta 163 ms. Lokální doručování potvrzeno, dopad na celkové Performance/LCP ověřit souhrnným měřením.
- [x] **LCP – priorita úvodního obrázku:** 16. 10. 2026 přidáno `rel="preload"` a `fetchpriority="high"` pro `/assets/hero-pipes.svg` v `<head>` podle Lighthouse. Vizuální vzhled a styly beze změny; efekt ověřit novým mobilním měřením (předchozí screenshot `LCP request discovery` upozornil na chybějící vysokou prioritu).
- [x] **Render-blocking – následné měření 16. 10.:** odhad potenciální úspory klesl z 1 760 ms na **120 ms**. Externí Google Fonts zmizely; zůstává pouze Cloudflare `email-decode.min.js` (~150 ms, 1,2 KiB). Kvůli malé úspoře zachovat ochranu e-mailu. Kritická síťová cesta v novém měření 204 ms (předtím 163 ms); běžná odchylka laboratorního testu, nikoli prokázaná regrese.
- [x] **Souhrnný PageSpeed – mobil po optimalizacích, 16. 10.:** Performance **97**, Accessibility **100**, Best Practices **100**, SEO **100**; FCP **0,8 s**, LCP **2,6 s**, Speed Index **0,8 s**, TBT **0 ms**, CLS **0,051**. Proti původnímu měření Performance 85 a LCP 3,9 s významné zlepšení. Mobilní laboratorní skóre přijato jako dostatečné; další agresivní optimalizace bez důvodu nedělat.
- [ ] **Výkon / obrázky – zbývající ověření:** ověřit nový detail `Improve image delivery` / `Use efficient cache lifetimes` a desktopový PageSpeed, plus vizuální kontrolu všech obrázků na mobilu/tabletu/desktopu. LCP 2,6 s těsně nad doporučenými 2,5 s; další optimalizace pouze podle prokázaného problému.
- [x] **Přístupnost – předběžná oprava kontrastu:** 16. 10. 2026 ztmavena pouze barva malých modrých popisků sekcí `#126fc1` → `#1169b7` na světlých pozadích. V CSS byly vypočteny původní poměry 4,34–4,45 : 1 na různých částech modrého pozadí; nové nejméně 4,73 : 1, tedy přes WCAG AA pro běžný text. Žádné změny layoutu.
- [x] **Přístupnost – kontrolní mobilní Lighthouse 16. 10.:** skóre Accessibility vzrostlo z 95 na **100** po úpravě kontrastu; nebylo potřeba dalšího zásahu.
- [x] **PageSpeed – desktop (16. 10. 2026):** podle výsledků sdělených uživatelem skóre **Performance 100, Accessibility 100, Best Practices 100, SEO 100**. Jednotlivé metriky desktopu nebyly dodány, ale souhrnné hodnocení je potvrzené.
- [ ] **Bezpečnost a sdílení:** zkontrolovat na živé doméně HTTP hlavičky z `_headers` a náhledy při sdílení přes WhatsApp/Facebook/LinkedIn.

## SEO a propagace

- [x] SEO title, description, H1, canonical URL, strukturovaná data a působnost po celé ČR.
- [x] Připraveny soubory `robots.txt`, `sitemap.xml`, favicon a sociální náhled.
- [ ] Ověřit na živé doméně `robots.txt`, `sitemap.xml` a správnost canonical URL.
- [x] Přidat a ověřit doménovou službu `vodotopokobliha.cz` v **Google Search Console** – potvrzeno uživatelem 15. 10. 2026 (`Ownership verified`).
- [x] Odeslat sitemap `https://vodotopokobliha.cz/sitemap.xml` v Google Search Console – stav **Success**, potvrzeno uživatelem 15. 10. 2026. Indexaci URL kontrolovat zvlášť.
- [x] **Požádat o indexaci:** 15. 10. 2026 Google Search Console potvrdila `Indexing requested` – URL zařazena do prioritní fronty pro procházení (potvrzeno uživatelem). Živý test URL nebyl zvlášť potvrzen.
- [ ] **Sledovat indexaci Google:** poslední známý stav `Discovered – currently not indexed`, poslední procházení `N/A`. Za několik dní znovu ověřit URL Inspection, případné chyby a skutečné zaindexování; požadavek neopakovat bez důvodu.
- [x] Vložit ověřovací meta tag **Seznam Webmaster** do hlavičky webu (16. 10. 2026).
- [x] **Seznam Webmaster – HTTPS:** vlastnictví `https://vodotopokobliha.cz/` ověřeno, potvrzeno uživatelem 16. 10. 2026. HTTP varianta je přesměrovaná na HTTPS, proto ji samostatně neověřovat a druhý meta tag nepřidávat.
- [ ] **Seznam Webmaster – provoz:** po načtení statistik sledovat indexované stránky, přesměrování a případné chyby robota (u nově přidaného webu se data mohou objevit se zpožděním).
- [ ] Zvážit samostatně firemní profil podle skutečné způsobilosti a schválených údajů.

## Evidence k archivaci (neblokující)

- [ ] Pokud jsou k dispozici, uložit k projektu písemná oprávnění / licence k externím fotografiím. Potvrzení zadavatele již máme, ale samo o sobě nepředstavuje nezávisle doloženou licenci.

Poznámka: Potvrzení zadavatelem je zaznamenané jako obchodní schválení údajů, nikoli jako nezávislé ověření veřejných registrů či licencí. Ostatní neověřená tvrzení do webu nepřidávat.
