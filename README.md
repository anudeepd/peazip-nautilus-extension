
## peazip-nautilus-extension

A simple sub menu extension that integrates PeaZip's functionality into the Nautilus file manager, designed using Python.

Please note that the script has been **designed to work with the Flatpak version** of PeaZip. In case a binary of PeaZip is being used, change the path accordingly.

This has been last tested on **Nautilus 46.1**

## Steps to follow

-   Install `nautilus-python` from your package repositories. [![Packaging status](https://repology.org/badge/tiny-repos/nautilus-python.svg)](https://repology.org/project/nautilus-python/versions)

-   Create the below path if it doesn't exist and place `peazip_submenu.py` there.

    ```bash 
    ~/.local/share/nautilus-python/extensions
    ```

-   Restart nautilus using the below command. The sub menu should now be accessible.

    ```bash
    nautilus -q
    ```
    
## Demo

https://github.com/anudeepd/peazip-nautilus-extension/assets/29518413/5cfba0e6-9ab1-41ea-a768-8633b97d9f1c
