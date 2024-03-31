import aiohttp
import asyncio
import aiofiles
import zipfile
from pystyle import Box, Colors, Write, Center
from rich.console import Console
from rich.table import Table
from rich import box
import json
import psutil
import os

config_file = "config.json"
logs_files = "logs\\logs.txt"

class Banner():
    def __init__(self): pass

    def display_banner(self): 
        try:
            banner = '''
   ███        ▄████████  ▄████████    ▄█    █▄        ███        ▄████████  ▄██████▄   ▄█    █▄     ▄████████      ███    █▄     ▄████████ ▀█████████▄          ▄████████    ▄████████    ▄███████▄    ▄████████  ▄█     ▄████████ 
▀█████████▄   ███    ███ ███    ███   ███    ███   ▀█████████▄   ███    ███ ███    ███ ███    ███   ███    ███      ███    ███   ███    ███   ███    ███        ███    ███   ███    ███   ███    ███   ███    ███ ███    ███    ███ 
   ▀███▀▀██   ███    █▀  ███    █▀    ███    ███      ▀███▀▀██   ███    ███ ███    ███ ███    ███   ███    █▀       ███    ███   ███    █▀    ███    ███        ███    ███   ███    █▀    ███    ███   ███    ███ ███▌   ███    ███ 
    ███   ▀  ▄███▄▄▄     ███         ▄███▄▄▄▄███▄▄     ███   ▀  ▄███▄▄▄▄██▀ ███    ███ ███    ███  ▄███▄▄▄          ███    ███   ███         ▄███▄▄▄██▀        ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███   ███    ███ ███▌  ▄███▄▄▄▄██▀ 
    ███     ▀▀███▀▀▀     ███        ▀▀███▀▀▀▀███▀      ███     ▀▀███▀▀▀▀▀   ███    ███ ███    ███ ▀▀███▀▀▀          ███    ███ ▀███████████ ▀▀███▀▀▀██▄       ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀█████████▀  ▀███████████ ███▌ ▀▀███▀▀▀▀▀   
    ███       ███    █▄  ███    █▄    ███    ███       ███     ▀███████████ ███    ███ ███    ███   ███    █▄       ███    ███          ███   ███    ██▄      ▀███████████   ███    █▄    ███          ███    ███ ███  ▀███████████ 
    ███       ███    ███ ███    ███   ███    ███       ███       ███    ███ ███    ███ ███    ███   ███    ███      ███    ███    ▄█    ███   ███    ███        ███    ███   ███    ███   ███          ███    ███ ███    ███    ███ 
   ▄████▀     ██████████ ████████▀    ███    █▀       ▄████▀     ███    ███  ▀██████▀   ▀██████▀    ██████████      ████████▀   ▄████████▀  ▄█████████▀         ███    ███   ██████████  ▄████▀        ███    █▀  █▀     ███    ███ 
                                                                 ███    ███                                                                                     ███    ███                                               ███    ███ 
'''
            secondary_text = '''Designed by The Nebula Developer\nHave Fun Reparing Computers!'''
            Write.Print(Center.XCenter(banner),Colors.light_gray,interval=0.0025)
            print("")
            Write.Print(Box.Lines(secondary_text), Colors.light_gray, interval=0.0025)
            print("")
        except Exception as e: 
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Display Banner - {e}")
            Write.Print(f"[-] Error: Could not Display Banner - {e}\n", Colors.red, interval=0.0025)
            raise

class Tool_Downloader():
    def __init__(self): pass

    async def download_zip_file(self,url, destination):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url,ssl=False) as response:
                    if response.status == 200:
                        async with aiofiles.open(destination, 'wb') as f:
                            while True:
                                chunk = await response.content.read(1024)
                                if not chunk:
                                    break
                                await f.write(chunk)
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Download EXE from {url} - {e}")
            Write.Print(f"[-] Error: Could not Download EXE from {url} - {e}\n", Colors.red, interval=0.0025)
            raise

    async def download_and_extract_zip(self,zip_url, extract_to):
        try:
            await self.download_zip_file(zip_url, 'temp.zip')
            with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not ZIP data - {e}")
            Write.Print(f"[-] Error: Could not ZIP data - {e}\n", Colors.red, interval=0.0025)
            raise

    async def download_file(self,url, destination):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url,ssl=False) as response:
                    if response.status == 200:
                        async with aiofiles.open(destination, 'wb') as f:
                            while True:
                                chunk = await response.content.read(1024)
                                if not chunk:
                                    break
                                await f.write(chunk)
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Download ZIP FOLDER from {url} - {e}")
            Write.Print(f"[-] Error: Could not Download ZIP FOLDER from {url} - {e}\n", Colors.red, interval=0.0025)
            raise

class Drive_Selector: 
    def __init__(self): 
        pass

    def tabler(self,data, title, **kwargs):
            try:
                table = Table(title=title, show_header=True, header_style="yellow", style="cyan")
                table.box = box.MINIMAL
                table.add_column("Selector", style="red", justify="center")
                table.add_column("Drive", style="green", justify="center")

                if isinstance(data, dict):
                    for key, value in data.items():
                        if isinstance(value, dict):
                            for inner_key, inner_value in value.items():
                                table.add_row(inner_key, str(inner_value))
                        else:
                            table.add_row(key, str(value))
                        table.add_row("—" * 20, "—" * 20)

                elif isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            for key, value in item.items():
                                table.add_row(key, str(value))
                        elif isinstance(item, str):
                            table.add_row(item, "N/A")
                        else:
                            table.add_row(str(item), "N/A")
                        table.add_row("—" * 20, "—" * 20)

                console = Console()
                console.print(table, justify="center")
                with open(logs_files, "a") as log_file:
                    log_file.writelines(f"\n[+] Success: Printed Table")
            except Exception as e:
                with open(logs_files, "a") as log_file:
                    log_file.writelines(f"\n[-] Error: Table Could not be displayed - {e}")
                Write.Print(f"[-] Error: Table Could not be displayed - {e}\n", Colors.red, interval=0.0025)
                raise

    def create_selection(self,available_drives): 
        try:
            selection = {}
            for point,drive in enumerate(available_drives): 
                selection[str(point)]=drive
            return selection
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Create Selectables - {e}")
            Write.Print(f"[-] Error: Could not Create Selectables - {e}\n", Colors.red, interval=0.0025)
            raise

    def list_usb_drives(self):
        try:
            usb_drives = []
            for partition in psutil.disk_partitions():
                if 'removable' in partition.opts and partition.mountpoint:
                    if os.path.exists(partition.mountpoint):
                        usb_drives.append(partition.mountpoint)
            return usb_drives
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Get USBs - {e}")
            Write.Print(f"[-] Error: Could not Get USBs - {e}\n", Colors.red, interval=0.0025)
            raise

    def select_drive_input(self,selectables): 
        try:
            selected = Write.Input("""
Enter The Number for the USB Drive to USE
==> """, Colors.light_gray,interval=0.0025)
            if selected.lower() not in selectables:
                Write.Print("\nThe Entered Selection is not valid! Select a Valid Option!\n",Colors.red, interval=0.0025)
                return self.select_drive_input(selectables=selectables)
            else: 
                return selected
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not get User Drive Selection - {e}")
            Write.Print(f"[-] Error: Could not get User Drive Selection - {e}\n", Colors.red, interval=0.0025)
            raise

    def select_drive(self,selected,selection): 
        try:
            if selected == None: 
                Write.Print("The System has had an Internal Error!",Colors.red, interval=0.0025)
            else: 
                drive = selection[selected.lower()]
                return drive
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Select Drive - {e}")
            Write.Print(f"[-] Error: Could not Select Drive - {e}\n", Colors.red, interval=0.0025)
            raise
        
    def main(self,):
        try:
            usb_drives = self.list_usb_drives()
            if usb_drives:
                selection = self.create_selection(usb_drives)
                self.tabler(data=selection,title="USBs to Select")
                selectables = [*(key for key in selection)]
                data = self.select_drive_input(selectables=selectables)
                drive = self.select_drive(selected=data,selection=selection)
                return drive
            else:
                with open(logs_files, "a") as log_file:
                    log_file.writelines(f"\n[-] Error: No USB Drives found!")
                Write.Print(f"[-] Error: No USB Drives found!\n", Colors.red, interval=0.0025)
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Select USB drive - {e}")
            Write.Print(f"[-] Error: Could not Select USB drive - {e}\n", Colors.red, interval=0.0025)
            raise

class File_Managment(): 
    def __init__(self):
        self.tool_downloader = Tool_Downloader()

    def display_tool_types(self,tools, title, **kwargs): 
        try:
            table = Table(title=title, show_header=True, header_style="yellow", style="cyan")
            table.box = box.MINIMAL
            table.add_column("Selector", style="red", justify="center")
            table.add_column("System", style="green", justify="center")

            if isinstance(tools, dict):
                for key, value in tools.items():
                    if isinstance(value, dict):
                        for inner_key, inner_value in value.items():
                            table.add_row(inner_key, str(inner_value["purpose"]))
                    else:
                        table.add_row(key, str(value))
                    table.add_row("—" * 20, "—" * 20)

            elif isinstance(tools, list):
                for item in tools:
                    if isinstance(item, dict):
                        for key, value in item.items():
                            table.add_row(key, str(value["purpose"]))
                    elif isinstance(item, str):
                        table.add_row(item, "N/A")
                    else:
                        table.add_row(str(item), "N/A")
                    table.add_row("—" * 20, "—" * 20)

            console = Console()
            console.print(table, justify="center")
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[+] Success: Printed Table")
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Table Could not be displayed - {e}")
            Write.Print(f"[-] Error: Table Could not be displayed - {e}\n", Colors.red, interval=0.0025)
            raise
    '''
    Start internals
    '''    
    def display_tool_internals(self,tools, title, **kwargs): 
        try:
            table = Table(title=title, show_header=True, header_style="yellow", style="cyan")
            table.box = box.MINIMAL
            table.add_column("Selector", style="red", justify="center")
            table.add_column("Software", style="green", justify="center")

            if isinstance(tools, dict):
                for key, value in tools.items():
                    if isinstance(value, dict):
                        for inner_key, inner_value in value.items():
                            table.add_row(inner_key, str(inner_value))
                    else:
                        table.add_row(key, str(value))
                    table.add_row("—" * 20, "—" * 20)

            elif isinstance(tools, list):
                for item in tools:
                    if isinstance(item, dict):
                        for key, value in item.items():
                            table.add_row(key, str(value))
                    elif isinstance(item, str):
                        table.add_row(item, "N/A")
                    else:
                        table.add_row(str(item), "N/A")
                    table.add_row("—" * 20, "—" * 20)

            console = Console()
            console.print(table, justify="center")
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[+] Success: Printed Table")
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Table Could not be displayed - {e}")
            Write.Print(f"[-] Error: Table Could not be displayed - {e}\n", Colors.red, interval=0.0025)
            raise
    
    def select_tools_internal(self,selectables): 
        try:
            selected = Write.Input("""
Enter The Number for the Internal-System to USE
==> """, Colors.light_gray,interval=0.0025)
            if selected.lower() not in selectables:
                Write.Print("\nThe Entered Selection is not valid! Select a Valid Option!\n",Colors.red, interval=0.0025)
                return self.select_tools_internal(selectables=selectables)
            else: 
                return selected
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Select Internal System - {e}")
            Write.Print(f"[-] Error: Could not Select Internal System - {e}\n", Colors.red, interval=0.0025)
            raise

    def get_tool_internals(self,tools): 
        try:
            tools = set([*(tool for tool in tools)])
            return tools
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Internal Tools - {e}")
            Write.Print(f"[-] Error: Could not Internal Tools - {e}\n", Colors.red, interval=0.0025)
            raise

    def create_selection_internals(self,available_tools_internals): 
        selection = {}
        for point,tool in enumerate(available_tools_internals): 
            selection[str(point)]=tool
        selection[str(len(selection))]="All"
        return selection
    
    def select_system_internals(self,selected,selection): 
        if selected == None: 
            Write.Print("The System has had an Internal Error!",Colors.red, interval=0.0025)
        else: 
            system = selection[selected.lower()]
            return system

    '''
    End internals
    '''
    def create_selection(self,available_tools_types): 
        try:
            selection = {}
            for point,type in enumerate(available_tools_types): 
                selection[str(point)]=type
            selection[str(len(selection))]="All"
            return selection
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Create Selctables - {e}")
            Write.Print(f"[-] Error: Could not Create Selctables - {e}\n", Colors.red, interval=0.0025)
            raise

    def load_tools(self): 
        try:
            with open(config_file,"r") as config_file_data: 
                config_data = json.load(config_file_data)
                tools = config_data["tools"]
                return tools
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Load Config File - {e}")
            Write.Print(f"[-] Error: Could not Load Config File - {e}\n", Colors.red, interval=0.0025)
            raise

    def get_purposes(self,tools): 
        try:
            purposes = set([*(tools[tool]["purpose"] for tool in tools)])
            return purposes
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not get Sub Systems! - {e}")
            Write.Print(f"[-] Error: Could not get Sub Systems! - {e}\n", Colors.red, interval=0.0025)
            raise

    def select_tools(self,selectables): 
        try:
            selected = Write.Input("""
Enter The Number for the System to USE
==> """, Colors.light_gray,interval=0.0025)
            if selected.lower() not in selectables:
                Write.Print("\nThe Entered Selection is not valid! Select a Valid Option!\n",Colors.red, interval=0.0025)
                return self.select_tools(selectables=selectables)
            else: 
                return selected
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not get Select System - {e}")
            Write.Print(f"[-] Error: Could not get Select System - {e}\n", Colors.red, interval=0.0025)
            raise

    def select_system(self,selected,selection): 
        try:
            if selected == None: 
                Write.Print("The System has had an Internal Error!",Colors.red, interval=0.0025)
            else: 
                system = selection[selected.lower()]
                return system
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not get Correct System - {e}")
            Write.Print(f"[-] Error: Could not get Correct System - {e}\n", Colors.red, interval=0.0025)
            raise

    async def selected_download_system(self,tools,drive):
        try:
            console = Console()
            for tool in tools: 
                tool_name = tool
                tool = tools[tool]
                if tool['type'] == "exe": 
                    with console.status(f"[bold cyan]Downloading...{tool_name}", spinner="dots") as status:
                        await self.tool_downloader.download_file(tool["download"], f"{drive}//{tool_name}.exe")
                    console.print(f"[green]Download for {tool_name} complete")
                elif tool['type'] == "zip":
                    with console.status(f"[bold cyan]Downloading...{tool_name}", spinner="dots") as status:
                        await self.tool_downloader.download_and_extract_zip(tool["download"], f"{drive}//{tool['purpose'].lower()}//{tool_name}")
                    console.print(f"[green]Download for {tool_name} complete")
        except Exception as e:
            with open(logs_files, "a") as log_file:
                log_file.writelines(f"\n[-] Error: Could not Download Tool - {e}")
            Write.Print(f"[-] Error: Could not Download Tool - {e}\n", Colors.red, interval=0.0025)
            raise

    async def get_systems(self, selected, tools, drive):
        if selected.lower() == "all":
            Write.Print(f"\nStarted Download of {selected.lower()} systems\n", Colors.light_gray, interval=0.0025)
            await self.selected_download_system(tools=tools, drive=drive)
            Write.Print(f"\nCompleted Download of {selected.lower()} systems\n", Colors.light_gray, interval=0.0025)
        else:
            tools_to_use = {}
            for tool_name, tool_data in tools.items():
                if tool_data["purpose"] == selected:
                    tools_to_use[tool_name] = tool_data
            tools_available = tools_to_use
            tools_internals = self.get_tool_internals(tools=tools_to_use)
            selection_internals = self.create_selection_internals(tools_internals)
            self.display_tool_internals(tools=selection_internals, title=f"Internal Tools for {selected}")
            selected = self.select_tools_internal(selectables=selection_internals)
            selected_internal = self.select_system_internals(selected=selected, selection=selection_internals)
            if selected_internal.lower() == "all":
                try:
                    Write.Print(f"\nStarted Download of {selected_internal.lower()} systems\n", Colors.light_gray, interval=0.0025)
                    await self.selected_download_system(tools=tools_available, drive=drive)
                    Write.Print(f"\nCompleted Download of {selected_internal.lower()} systems\n", Colors.light_gray, interval=0.0025)
                except Exception as e:
                    with open(logs_files, "a") as log_file:
                        log_file.writelines(f"\n[-] Error: Could not get Tool - {e}")
                    Write.Print(f"[-] Error: Could not get Tool - {e}\n", Colors.red, interval=0.0025)
                    raise 
            else:
                try:
                    Write.Print(f"\nStarted Download of {selected_internal.lower()} systems\n", Colors.light_gray, interval=0.0025)
                    await self.selected_download_system(tools={selected_internal: tools_to_use[selected_internal]}, drive=drive)
                    Write.Print(f"\nCompleted Download of {selected_internal.lower()} systems\n", Colors.light_gray, interval=0.0025)
                except Exception as e:
                    with open(logs_files, "a") as log_file:
                        log_file.writelines(f"\n[-] Error: Could not get Tool - {e}")
                    Write.Print(f"[-] Error: Could not get Tool - {e}\n", Colors.red, interval=0.0025)
                    raise

    def main(self): 
        try:
            banner = Banner()
            banner.display_banner()
            select_drive = Drive_Selector()
            drive = select_drive.main()
            if drive == None:
                with open(logs_files, "a") as log_file:
                    log_file.writelines(f"\n[-] Error: No Drive to Create Repair System Found!")
                Write.Print(f"[-] Error: No Drive to Create Repair System Found!\n", Colors.red, interval=0.0025)
            else:
                tools = self.load_tools()
                purposes = self.get_purposes(dict(tools))
                selections = self.create_selection(available_tools_types=purposes)
                self.display_tool_types(selections,title="Select System")
                selected = self.select_tools(selectables=selections)
                system = self.select_system(selected=selected,selection=selections)
                asyncio.run(self.get_systems(tools=tools,drive=drive,selected=system))
        except KeyboardInterrupt: 
            Write.Print(f"\nTerminating System - WARNING USB systems MAY be unsable - if they have been written!\n", Colors.red, interval=0.0025)

system = File_Managment()
system.main()