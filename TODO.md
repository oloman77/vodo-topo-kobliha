# Vodo-topo Kobliha – TODO

Aktualizováno: 16. 10. 2026

## Aktuálně otevřené úkoly (3)

> Web, HTTPS, e-mailové DNS, responzivita, výkon a náhledy sdílení byly otestovány. Následující úkoly jsou pouze ke sledování a ověření; **bez výslovného souhlasu neprovádět změny v DNS, Cloudflare, GitHubu ani poště**.

- [ ] **1. DNSSEC – nejvyšší priorita.** Počkat na automatické vytvoření a přiřazení KEYSET/DS u CZ.NIC. Poslední autoritativní test 16. 10. 2026 prokázal DNSKEY/RRSIG na Cloudflare, ale **DS v .cz chyběl**; CZ.NIC 16. 10. v 01:37 ve skenech zobrazil `INSECURE_SCHEDULED` na obou serverech, což ještě nepotvrzuje funkční validaci. Po změně ověřit DS a skutečný řetězec důvěry přes nezávislé validující resolvery. Denní automatický dohled je aktivní. Nezasahovat preventivně do DNSSEC/NSSET/MX ani e-mailového DNS.
- [ ] **2. Google – indexace.** V Google Search Console už byla ověřena doména, sitemap přijata (`Success`) a odeslána žádost o indexaci. Poslední doložený stav byl `Discovered – currently not indexed`. Sledovat skutečné zaindexování, případné chyby a změny stavu. Žádost o indexaci bez důvodu neopakovat. Denní veřejná kontrola je naplánovaná.
- [ ] **3. Seznam – indexace.** Seznam Webmaster pro HTTPS byl ověřen. Sledovat první indexované stránky, chyby robota a případná přesměrování v jeho rozhraní; přehled veřejného vyhledávání se kontroluje automaticky. Indexace nové domény může trvat.

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
- [x] Přehled responzivních pravidel a zachování mobilního menu v kódu; reálné vykreslení později ověřeno v Chromiu, Edge, Firefoxu a Safari na iPhonu.
- [x] **Optimalizace a lokální hosting fotografií:** GitHub Actions 16. 10. úspěšně stáhly pět unikátních referenčních fotografií a pozadí patičky, převedly je na 10 verzovaných WebP souborů v `assets/optimized/`, pro šest karet nastavily lokální `src`, pro velké karty také `srcset`/`sizes`. Všechny externí URL fotografií i externí CSS obrázek odstraněny ze zdrojového kódu. Přidány cache hlavičky (rok, immutable). Potvrzeno commitem `ea4eaa2`; atribuce a vzhled v CSS beze změn. **Produkční nasazení, HTTP 200, cache i PageSpeed byly následně ověřeny (viz samostatné dokončené úkoly).**

## Technické kontroly – hotovo

- [x] **TopTower na produkci:** zadavatel 15. 10. 2026 ověřil, že na ostrém webu už není uvedena cena budoucí zakázky. (Kontrola přesné verze/commit ID Cloudflare nebyla nezávisle provedena.)
- [x] **Dostupnost ostré domény a HTTPS:** 16. 10. 2026 externí GitHub Actions ověřily HTTP 200 přes platné HTTPS, Cloudflare NS, A/AAAA, MX pro Seznam Email Profi a SPF v TXT. Test dokončen bez změn DNS.
- [x] **DNSSEC – autoritativní diagnostika 16. 10. 2026:** GitHub Actions read-only kontrola přímým dotazem na `a.ns.nic.cz` i přes resolver 8.8.8.8 a 1.1.1.1 prokázala existenci DNSKEY a RRSIG u Cloudflare, ale **neexistenci DS v nadřazené zóně .cz**. Oba rekurzivní resolvery odpovídají bez SERVFAIL, ale delegace není ověřená řetězcem DNSSEC. MX Seznam Email Profi i SPF platné, poštu funkčně neposuzoval. Logy: https://github.com/oloman77/vodo-topo-kobliha/actions/runs/38823206159 .
- [x] **Přesměrování:** 16. 10. GitHub Actions ověřily trvalé HTTP **301** u `http://vodotopokobliha.cz/`, `http://www.vodotopokobliha.cz/` a `https://www.vodotopokobliha.cz/` → hlavní `https://vodotopokobliha.cz/`.
- [x] **Nasazení lokálních obrázků:** 16. 10. ostrá stránka vrátila HTML s `assets/optimized/`; namátkově ověřené Dubičný potok, SO-HO, Lihovar JIH, TopTower a patička: všechny HTTP 200 `image/webp` + `Cache-Control: max-age=31536000, immutable`.
- [x] **Načítání obrázků v prohlížeči:** GitHub Actions test 16. 10. prověřil všech šest fotografií přes Chromium na šesti šířkách (320/375/390/768/1024/1440 px), všechny se načetly, žádná chyba. Screenshoty jsou v artefaktu běhu `38821797038`.
- [x] **Vizuální kontrola na iPhonu:** uživatel 16. 10. 2026 potvrdil `iPhone OK` pro fotografie a jejich ořezy, navigaci a rozložení v Safari.
- [x] **Finální vizuální kontrola desktopu:** uživatel potvrdil `Desktop OK` po kontrole šesti fotografií, jejich ořezů a rozložení webu ve Firefoxu (16. 10. 2026).
- [x] **Produkční soubory:** 16. 10. externě ověřeno HTTP 200 pro `/favicon.svg`, `/apple-touch-icon.png`, `/assets/social-preview.png`, `/robots.txt`, `/sitemap.xml`; lokální interní a `tel:`/`mailto:` odkazy ověřeny v HTML. 
- [x] **Kontaktní odkazy v praxi:** uživatel 16. 10. potvrdil `iPhone OK` po výzvě vyzkoušet tlačítka pro zavolání a e-mail v Safari (bez odesílání zpráv).
- [x] **Automatická responzivita v Chromiu:** 16. 10. otestováno šest velikostí 320, 375, 390, 768, 1024 a 1440 px; **0 chyb**. Bez vodorovného přetékání; navigace na jednom řádku, mobilní/tabletové tři ikony v jednom řádku, žádné neexistující kotvy; všech šest fotek načtených. Výstup `https://github.com/oloman77/vodo-topo-kobliha/actions/runs/38821797038`.
- [x] **Safari na iPhonu:** ruční vizuální kontrola vzhledu, fotografií, navigace a tří ikon služeb potvrzena uživatelem 16. 10. (`iPhone OK`).
- [x] **Firefox na desktopu:** uživatel potvrdil `Desktop OK` po výzvě ke kontrole webu ve Firefoxu (16. 10. 2026).
- [x] **Microsoft Edge na desktopu:** 16. 10. 2026 nezávislý GitHub Actions test ostrého webu v Microsoft Edge na šířkách 1024 a 1440 px – 0 chyb; bez přetékání, navigace v jednom řádku, všechny lokální fotografie načteny, interní kotvy platné. Workflow: https://github.com/oloman77/vodo-topo-kobliha/actions/runs/38822742587.
- [x] **PageSpeed Insights – mobil, 16. 10. 2026:** Lighthouse Performance **85**, Accessibility **95**, Best Practices **96**, SEO **100**; FCP ~**2,6 s**, LCP **3,9 s**, Speed Index **2,6 s**, TBT **0 ms**, CLS **0,002**. Jde o laboratorní měření (bez dat skutečných uživatelů).
- [x] **Cloudflare Fonts:** zapnutí potvrzeno uživatelem 16. 10. 2026. Následný mobilní Lighthouse audit ukazuje doručování dvou souborů fontů přímo z `vodotopokobliha.cz` (~163 ms / 30,90 KiB a ~138 ms / 27,80 KiB), bez dalšího externího originu k preconnect; nejdelší kritická síťová cesta 163 ms. Lokální doručování potvrzeno, dopad na celkové Performance/LCP ověřit souhrnným měřením.
- [x] **LCP – priorita úvodního obrázku:** 16. 10. 2026 přidáno `rel="preload"` a `fetchpriority="high"` pro `/assets/hero-pipes.svg` v `<head>` podle Lighthouse. Vizuální vzhled a styly beze změny; efekt ověřit novým mobilním měřením (předchozí screenshot `LCP request discovery` upozornil na chybějící vysokou prioritu).
- [x] **Render-blocking – následné měření 16. 10.:** odhad potenciální úspory klesl z 1 760 ms na **120 ms**. Externí Google Fonts zmizely; zůstává pouze Cloudflare `email-decode.min.js` (~150 ms, 1,2 KiB). Kvůli malé úspoře zachovat ochranu e-mailu. Kritická síťová cesta v novém měření 204 ms (předtím 163 ms); běžná odchylka laboratorního testu, nikoli prokázaná regrese.
- [x] **Souhrnný PageSpeed – mobil po optimalizacích, 16. 10.:** Performance **97**, Accessibility **100**, Best Practices **100**, SEO **100**; FCP **0,8 s**, LCP **2,6 s**, Speed Index **0,8 s**, TBT **0 ms**, CLS **0,051**. Proti původnímu měření Performance 85 a LCP 3,9 s významné zlepšení. Mobilní laboratorní skóre přijato jako dostatečné; další agresivní optimalizace bez důvodu nedělat.
- [x] **PageSpeed po optimalizaci:** mobil Performance **97**, přístupnost/Best Practices/SEO **100**; desktop všechna čtyři skóre **100**, dle uživatele. Cache verzovaných lokálních obrázků nezávisle potvrzena v produkci. Nepokračovat v honbě za laboratorními body; případný rozdíl `Improve image delivery` kontrolovat jen při skutečně pomalém či chybném načítání. Vizuální kontrola fotografií je uvedena samostatně.
- [x] **Přístupnost – předběžná oprava kontrastu:** 16. 10. 2026 ztmavena pouze barva malých modrých popisků sekcí `#126fc1` → `#1169b7` na světlých pozadích. V CSS byly vypočteny původní poměry 4,34–4,45 : 1 na různých částech modrého pozadí; nové nejméně 4,73 : 1, tedy přes WCAG AA pro běžný text. Žádné změny layoutu.
- [x] **Přístupnost – kontrolní mobilní Lighthouse 16. 10.:** skóre Accessibility vzrostlo z 95 na **100** po úpravě kontrastu; nebylo potřeba dalšího zásahu.
- [x] **PageSpeed – desktop (16. 10. 2026):** podle výsledků sdělených uživatelem skóre **Performance 100, Accessibility 100, Best Practices 100, SEO 100**. Jednotlivé metriky desktopu nebyly dodány, ale souhrnné hodnocení je potvrzené.
- [x] **Bezpečnostní hlavičky:** produkční HTTP odpověď 16. 10. obsahuje `X-Content-Type-Options: nosniff`, `X-Frame-Options: SAMEORIGIN`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`. 
- [x] **Sdílení přes WhatsApp na iPhonu:** uživatel 16. 10. potvrdil `iPhone OK` po výzvě k ověření náhledu sdíleného odkazu. Obrázek `/assets/social-preview.png` současně veřejně dostupný přes HTTPS (HTTP 200).
- [x] **Technická příprava sdílení pro Facebook/LinkedIn:** 16. 10. nezávislý test živé HTTPS stránky s User-Agent `facebookexternalhit` ověřil `og:type`, `og:url`, `og:title`, `og:description`, `og:image` a přesně odpovídající PNG obrázek 1200 × 630 (HTTP 200). Workflow: https://github.com/oloman77/vodo-topo-kobliha/actions/runs/38822742587.
- [x] **Náhledy Facebook a LinkedIn – potvrzeno uživatelem 16. 10. 2026:** screenshoty z Facebook Sharing Debugger a LinkedIn Post Inspector ukázaly správný název, popis, adresu a obrázek. U Facebooku chybějící `fb:app_id` nebrání běžnému sdílení; u LinkedIn údaje o autorovi/datumu článku nejsou pro firemní prezentační web nutné. Bez požadavků na změny webu.

## SEO – technické nastavení hotovo

- [x] SEO title, description, H1, canonical URL, strukturovaná data a působnost po celé ČR.
- [x] Připraveny soubory `robots.txt`, `sitemap.xml`, favicon a sociální náhled.
- [x] **SEO v produkci:** 16. 10. `robots.txt` a `sitemap.xml` vracejí HTTP 200; produkční HTML obsahuje správnou canonical adresu `https://vodotopokobliha.cz/`.
- [x] Přidat a ověřit doménovou službu `vodotopokobliha.cz` v **Google Search Console** – potvrzeno uživatelem 15. 10. 2026 (`Ownership verified`).
- [x] Odeslat sitemap `https://vodotopokobliha.cz/sitemap.xml` v Google Search Console – stav **Success**, potvrzeno uživatelem 15. 10. 2026. Indexaci URL kontrolovat zvlášť.
- [x] **Požádat o indexaci:** 15. 10. 2026 Google Search Console potvrdila `Indexing requested` – URL zařazena do prioritní fronty pro procházení (potvrzeno uživatelem). Živý test URL nebyl zvlášť potvrzen.
- [x] Vložit ověřovací meta tag **Seznam Webmaster** do hlavičky webu (16. 10. 2026).
- [x] **Seznam Webmaster – HTTPS:** vlastnictví `https://vodotopokobliha.cz/` ověřeno, potvrzeno uživatelem 16. 10. 2026. HTTP varianta je přesměrovaná na HTTPS, proto ji samostatně neověřovat a druhý meta tag nepřidávat.

Poznámka: Potvrzení zadavatelem je zaznamenané jako obchodní schválení zveřejněných údajů. Ostatní neověřená tvrzení do webu nepřidávat.
