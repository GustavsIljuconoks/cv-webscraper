# Darba Sludinājumu Web Scraping Sistēma

## Projekta uzdevums
Šī projekta mērķis ir automatizēta web scraping sistēma, kas ļauj iegūt un analizēt darba sludinājumus no dažādām interneta platformām Latvijā.
Projekta mērķis ir atvieglot darba meklēšanas procesu, sistemātiski apkopojot informāciju no dažādiem avotiem un attēlot tos lietotājiem vienotā formā.

## Projekta izmantošanas iespējas
Galvenais mērķis ar projekta palīdzību ir atvieglot lietotāju pieredzi vakances meklējumos.
Projekts nodrošina iespēju ērti apkopot rezultātus no dažādām mājaslapām, izmantojot iespēju lietotājam ievadīt dažādus filtrus.

- **Darba vakances meklēšana**: Lietotāji var meklēt darba sludinājumus no dažādām platformām.
- **Filtrēšanas iespējas**: Iespēja filtrēt rezultātus pēc atslēgvārdiem, algas un atrašanās vietas.
- **Datu saglabāšana**: Iegūtie dati tiek automātiski saglabāti CSV formā.
- **Meklēšanas vēsture**: Sistēma saglabā pēdējo 5 meklēšanas rezultātu vēsturi, ko var apskatīt galvenajā izvēlnē.

### Turpmākās attīstības iespējas
- Paplašināt atbalstītos darba sludinājumu avotus
- Izveidot grafisko lietotāja interfeisu (GUI) vai mājaslapu
- Pievienot papildu filtrēšanas opcijas (darba kategorijas, uzņēmuma tips, u.c.)
- Implementēt automātisko paziņojumu sistēmu par jauniem darba sludinājumiem

## Pakotnes
- `selenium`: Dinamisko tīmekļa lapu ielādei
- `chromedriver-py`: Chrome draivera automatizētai instalēšanai
- `time`: Gaidīšanas laika iestatīšanai starp darbībām
- `csv`: Datu saglabāšanai un apstrādei CSV formātā
- `json`: Datu serializēšanai JSON formātā
- `collections`: Specializēti datu tipu importēšanai (t.i `deque`)
- `os`: Operētājsistēmu atkarīgu funkcionalitāšu izmantošanai
- `datetime`: Datuma un laika ierakstīšanas implementēšanai

## Datu struktūras
Projekts izmanto šādas datu struktūras:
- Saraksti (list): Darba sludinājumu saglabāšanai
- Vārdnīcas (dict): Darba sludinājumu atribūtu glabāšanai
- Rinda (deque): Meklēšanas vēstures pārvaldībai ar ierobežotu izmēru

### Iegūto datu formāts
Katrs darba sludinājums tiek saglabāts kā vārdnīca ar šādiem laukiem:
- `title`: Darba sludinājuma nosaukums
- `location`: Darba vietas atrašanās vieta
- `link`: Saite uz oriģinālo sludinājumu

## Autori
- Gustavs Iļjučonoks
- Kristiāns Neško
