# Vodo-topo Kobliha s.r.o. — firemní web

Jednostránkový prezentační web společnosti Vodo-topo Kobliha s.r.o. Zdrojový kód spravujeme v repozitáři `oloman77/vodo-topo-kobliha`; stav dokončených a otevřených úkolů je veden v [TODO.md](TODO.md).

## Adresy a provoz

- Hlavní doména: https://vodotopokobliha.cz/
- Cloudflare Pages: https://vodo-topo-kobliha.pages.dev/
- GitHub: https://github.com/oloman77/vodo-topo-kobliha
- Produkční větev: `main`; propojení GitHub → Cloudflare Pages pro automatické nasazování již bylo nakonfigurováno. Po commitu ověřit výsledek v Cloudflare Pages → Deployments, nikoli jen stav GitHubu.
- HTTPS a přesměrování z HTTP / `www` na hlavní HTTPS doménu byly 16. 10. 2026 nezávisle ověřeny (HTTP 301 a platný HTTPS certifikát). DNSSEC bylo dokončeno 19. 10. 2026; ověřen DS v nadřazené zóně `.cz` a zelený řetězec podpisů v DNSSEC Debuggeru.
- DNS spravuje Cloudflare, e-mail běží přes Seznam Email Profi. Při úpravách webu **neměnit DNS/MX/SPF/DKIM/DMARC/DNSSEC bez samostatné diagnostiky a souhlasu**. Dokončení DNSSEC a jeho ověření je zaznamenáno v [TODO.md](TODO.md).

## Struktura projektu

| Soubor | Účel |
| --- | --- |
| `index.html` | Obsah, styly, SVG symboly, metadata a JSON-LD |
| `assets/hero-pipes.svg` | Grafika úvodní části |
| `assets/optimized/*.webp` | Lokální optimalizované fotografie referencí a pozadí patičky (v názvech hash kvůli cache) |
| `assets/social-preview.png` | Obrázek pro Open Graph a sociální sítě |
| `favicon.svg`, `apple-touch-icon.png` | Ikony webu |
| `robots.txt`, `sitemap.xml` | Pokyny pro vyhledávače; canonical doména `https://vodotopokobliha.cz/` |
| `_headers` | Bezpečnostní HTTP hlavičky Cloudflare Pages |
| `TODO.md` | Projektové úkoly, ověření a provozní kontroly |
| `FIREMNI_PROFILY.md` | Předávací podklady pro případné firemní zápisy Google a Firmy.cz |
| `OBRAZKY_LICENCE.md` | Evidované zdroje a veřejné licence obrazových podkladů; chybějící souhlasy |

Web nevyžaduje aplikaci či databázi. Změny obsahu a vzhledu jsou v současné podobě přímo v `index.html`.

## Zásady pro úpravy

1. Zachovat jednorázově schválené informace o firmě a referencích; neodvozovat nové kontakty, částky, termíny ani služby.
2. **Mobilní navigaci ponechat v jednom řádku.** Na mobilu musí zůstat tři ikony služeb vedle sebe. Změny desktopové sekce „O nás“ nesmějí rozbít tabletové a mobilní rozložení.
3. Na desktopu má „O nás“ dva sloupce: nadpis a text vlevo, ikony služeb vpravo se začátkem u nadpisu.
4. TopTower je plánovaná zakázka (255 bytů), **bez uvedené ceny**. Do budoucna případnou cenu nezavádět bez schválení.
5. Při úpravách referencí zachovat rozdíl mezi uskutečněnými, probíhajícími a budoucími zakázkami.
6. Fotografie všech šesti referenčních karet i pozadí patičky nyní načítáme lokálně z `assets/optimized/*.webp`. Web si podle `srcset` volí menší či větší variantu. Původní zdroje a atribuce zůstaly uvedeny v sekci autorských práv na webu. Použití potvrdil zadavatel; nezávislé posouzení licencí nebylo doloženo.
7. Každou změnu kontrolovat jako malý diff: neměnit nesouvisející HTML, CSS, SEO, kontakty, funkční odkazy či infrastrukturu.

## Postup při zveřejnění změny

1. Uložit změnu v `main` a zaznamenat odkaz na commit.
2. V Cloudflare Pages → Deployments ověřit úspěch automatického nasazení příslušné verze.
3. Na hlavní doméně zkontrolovat dotčenou sekci na desktopu a mobilu. U vizuálních změn navíc tablet a malé displeje.
4. Ověřit, že fungují formulované kontakty (`tel:`, `mailto:`), odkazy, šest fotografií a že se náhodou neobjevila cena TopTower.
5. Po zásahu do hlavičky nebo SEO ověřit canonical URL, `robots.txt`, `sitemap.xml`, sociální náhled a ověřovací tagy; samotné nasazení nezaručuje indexaci.
6. Zapsat dokončené / zbývající úkoly do [TODO.md](TODO.md).

## Vyhledávače a předání

- Google Search Console: doména ověřena, sitemap přijata, indexace hlavní stránky potvrzena 19. 10. 2026 interním reportem Performance / Pages (4 zobrazení a 1 kliknutí na HTTPS homepage).
- Seznam Webmaster: HTTPS varianta ověřena meta tagem v `index.html`; veřejná indexace hlavní stránky potvrzena výsledkem Seznam.cz dne 19. 10. 2026. HTTP variantu zvlášť neověřovat za cenu rozbití přesměrování.
- Při předání zákazníkovi předat provozní přístupy odpovídajícím oprávněným osobám; vlastnictví Search Console lze řešit přidáním dalšího vlastníka.

## Uzavření projektu (19. 10. 2026)

Všechny tři zbývající úkoly byly uzavřeny: DNSSEC (publikovaný DS, odpovídající KSK a platné podpisy dle DNSSEC Debuggeru), indexace Google (uživatelský screenshot Search Console) a Seznam (veřejný výsledek vyhledávání). Samostatné měření AD bitu přes další rekurzivní resolver nebylo doloženo. Přesměrování, HTTP hlavičky, nasazení WebP a Lighthouse (mobil Performance 97, ostatní 100; desktop všechny kategorie 100) byly ověřeny již 16. 10. 2026. Neotevírat nové úkoly bez konkrétního důvodu; historické licence a firemní profily nejsou součástí aktuálního TODO. Stav a zdroje potvrzení v [TODO.md](TODO.md).

### Běžné obsahové změny po předání

Web je statický, nemá zákaznickou administraci. Pro změny textů, kontaktů, referencí a fotografií zákazník dodá schválené podklady správci webu. Správce upraví zdroje v GitHubu a po automatickém nasazení přes Cloudflare Pages ověří změnu na ostré doméně a na mobilu. Zákazník může samostatně sledovat dostupnost webu a výsledky vyhledávání; přímé editování webu zákazníkem by vyžadovalo přístup ke zdrojům nebo doplnění redakčního systému. DNS a e-mailové nastavení se nemění v rámci obsahových úprav.
