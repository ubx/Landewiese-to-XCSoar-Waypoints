# Landewiesen to XCSoar Waipoints and Waypoint details

Exctract [CUPX](https://downloads.naviter.com/docs/SeeYou_CUPX_file_format.pdf) from Landewise zip-file(s)
and format to consistent [CUP](https://downloads.naviter.com/docs/SeeYou_CUP_file_format.pdf) and
XCSoar [Waypoint Details, (Chapter 14.5)](https://download.xcsoar.org/releases/7.28/XCSoar-manual.pdf) file,
including the corresponding images.

## How-to

1. Requires Python 3.10 or higher
2. Clone project: `git clone https://github.com/ubx/Landewiese-to-XCSoar-Waypoints`
3. Download zip-file(s), in CPUX format from [here](https://landewiesen.streckenflug.at//index.php?inc=cup). You need an
   account.
4. Copy zip-file(s) to `data/` folder
5. Run `python convert [<name>]`. Default name is *landewisen*
6. In the `output/` folder you will find `<name>.cup`, `<name>_details.txt` and images in `pics/`
7. Copy the above files into the XCSoar folder, dependent on your os and version:
    * for Android: `Android/data/org.xcsoar/files` (use cellphone storage if sd-card is not working)
    * for Linux: `.xcsoar`
    * for Kobo: `/mnt/onboard/XCSoarData`
    * for Windows: ?
8. * In XCSoar: **Config -> System -> Site File**, select *More Waypoints* (or *Watched Waypoints*):
     `<name>.cup` Waypoint details: `<name>_details.txt`
    .* In XCSoar 7.42 : **Config -> System -> Site File**, select *More Waypoints* (or *Watched Waypoints*):
     `<name>.cupx.cup` Waypoint details: `<name>.wp_details.txt`


## Note on Binwalk
Installing `binwalk` seems to have problems, see https://github.com/ReFirmLabs/binwalk/issues/352

### Install on Linux 

Binwalk can be installed globally or within the virtual environment as shown further below. 
```
git clone https://github.com/ReFirmLabs/binwalk.git
cd binwalk
sudo python setup.py install
```

### Install on Windows
```
git clone https://github.com/CypherpunkSamurai/binwalk-win.git 
cd .\binwalk-win\
C:\Users\904906\PycharmProjects\Landewiese-to-XCSoar-Waypoints\venv\Scripts\python.exe  setup.py install
```
Be sure the Windows `path` contains `jar.exe` (e.g. ``C:\Program Files\Java\jdk-19\bin``) and `unzip.exe` (e.g. download from here https://www.somacon.com/p161.php)

# Create environment (optional)

`* Create virtual environment 

    ```
    python3 -m venv .venv
    ```

* Activate environment 

    * Windows

        ```
        .\.venv\Scripts\activate
        ```
    
    * Linux
    
        ```
        . .venv/bin/activate
        ```

* Install Binwalk within the environment

    * Windows

        ```
        git clone https://github.com/CypherpunkSamurai/binwalk-win.git 
        cd .\binwalk-win\
        .\.venv\bin\python setup.py install
        ```

    * Linux
    
        ```
        git clone https://github.com/CypherpunkSamurai/binwalk-win.git 
        cd .\binwalk-win\
        .venv/bin/python setup.py install
        ```

* Install packages 

```
pip install -r requirements.txt 
```

# Install 7z

For Linux 7z can be installed via
    

    ```
    sudo apt-get install p7zip p7zip-full p7zip-rar 
    ```