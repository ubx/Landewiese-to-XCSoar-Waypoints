# Landewiese to XCSoar Waipoints and Waypoint details

Exctract [CUPX](https://downloads.naviter.com/docs/SeeYou_CUPX_file_format.pdf) from Landewise zip-file(s)
and format to consistent [CUP](https://downloads.naviter.com/docs/SeeYou_CUP_file_format.pdf) and
XCSoar [Waypoint Details, (Chapter 14.5)](https://download.xcsoar.org/releases/7.28/XCSoar-manual.pdf) file,
including the corresponding images.

## How-to

1. Clone project: `git clone https://github.com/ubx/Landewiese-to-XCSoar-Waypoints`
2. Download zip-file(s), in CPUX format from [here](https://landewiesen.streckenflug.at//index.php?inc=cup). You need an
   account.
3. Copy zip-file(s) to `output/` folder
4. Run `python convert [<name>]`. Default name is *landewisen*
5. In the `output/` folder you will find `<name>.cup`, `<name>_details.txt` and images in `pics/`
6. Copy the above files into the XCSoar folder, dependent on your os and version:
    * for Android: `Android/data/org.xcsoar/files`
    * for Linux: `.xcsoar`
    * for Windows: ?
7. In XCSoar: **Config -> System -> Site File**, select *More Waypoints* (or *Watched Waypoints*):
     `<name>.cup` an Waypoint details: `<name>_details.txt`

### Note
Installing `binwalk` semms to have problems, see https://github.com/ReFirmLabs/binwalk/issues/352

