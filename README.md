# GeoCrackr

**GeoCrackr** is a Python [Selenium](https://www.seleniumhq.org/) webdriver wrapper that reveals a users position in the popular online game GeoGuessr for Windows currently.

## Installation

```command
# Clone the repo
C:\user> git clone https://github.com/JossMoff/GeoCrackr.git

# Change the working directory to GeoCrackr
C:\user> cd GeoCrackr
```

## Prebuilt

 Now if you check in the directory  there will be a **GeoCrackr.exe** for anyone who doesn't want to build their own .exe and can then just run it directly from there.

## Build your own

Using the **requirements.txt** you can build your own version of the .exe

```command
# Install python3 and python3-pip if not exist

# Install the requirements
C:\user> pip3 install -r requirements.txt
```

From here we can use [PyInstaller](https://www.pyinstaller.org/) to build the app. Using the code:

```command
    pyinstaller GeoCrackr.py
```

   This will generate the bundle in a subdirectory called **dist**. However the recommended way will be like this:

   ```command
     pyinstaller GeoCrackr.py -F -i ./images/geocrackr.ico
   ```

   >If **Geocrackr.exe** does not run, make sure the driver folder is in the same directory  as **Geocrackr.exe**.

## Usage

Simply run the program and provide the link of the game you wish to play. It will then redirect you and you can see where you've been dropped.

![enter image description here](https://i.imgur.com/ignVND4.gif)
   >Please note for .gif brevity I just estimated where abouts the location was.

## Further Improvements

How I plan to extend the quick project:
 -🍎Provide OS X support
 -🐧Provide Linux Support
 -💻Add extra terminal features
 -😀Add emoji support in OS X/ Linux Terminals
 -📌Make pin automatically place on the right place
