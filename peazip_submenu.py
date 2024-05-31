from gi.repository import Nautilus, GObject
from typing import List
import subprocess
import os
import urllib.parse
import logging

class PeazipMenuProvider(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        super().__init__()
        # Set up logging
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def get_file_items(self, files: List[Nautilus.FileInfo]) -> List[Nautilus.MenuItem]:
        # Create the top-level menu item
        top_menuitem = Nautilus.MenuItem(
            name="PeazipMenuProvider::Main",
            label="PeaZip"
        )

        submenu = Nautilus.Menu()
        top_menuitem.set_submenu(submenu)
        
        actions = [
            ("Add to Archive", "-add2archive"),
            ("Convert", "-add2convert"),
            ("Extract Archive", "-ext2main"),
            ("Extract Here", "-ext2here"),
            ("Extract to Folder", "-ext2folder"),
            ("Open Archive", "-ext2browse")
        ]
        
        # Create submenu items for each PeaZip action
        for action_label, action_command in actions:
            sub_menuitem = Nautilus.MenuItem(
                name=f"PeazipMenuProvider::{action_label.replace(' ', '')}",
                label=action_label
            )
            sub_menuitem.connect("activate", self.execute_peazip_command, files, action_command)
            submenu.append_item(sub_menuitem)
            
        return [top_menuitem]
    
    def execute_peazip_command(self, menu, files, command):
        # Extract the file paths of all selected files and decode URIs
        selected_file_paths = [urllib.parse.unquote(file.get_uri().replace("file://", "")) for file in files]
        
        # Path to PeaZip's Flatpak application ID
        flatpak_app_id = "io.github.peazip.PeaZip"
        
        # Log the command and file paths
        logging.debug(f"Running PeaZip with command: {command} on files: {selected_file_paths}")
        
        # Verify Flatpak is installed
        if not self.is_flatpak_installed():
            logging.error("Flatpak is not installed.")
            return
        
        # Run PeaZip as a Flatpak with the specified command and selected files
        try:
            subprocess.Popen(["flatpak", "run", flatpak_app_id, command] + selected_file_paths)
        except Exception as e:
            logging.error(f"Failed to run PeaZip: {e}")
    
    def is_flatpak_installed(self):
        # Check if Flatpak is installed
        try:
            subprocess.check_output(["flatpak", "--version"])
            return True
        except subprocess.CalledProcessError:
            return False

