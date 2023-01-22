import tempfile
import subprocess
import pathlib
import shutil
import logging

logging.basicConfig(filename="clean_trace.log", level=logging.ERROR)

def clean_trace():
    try:
        # empty temp folder
        temp_folder = pathlib.Path(tempfile.gettempdir())
        for item in temp_folder.glob('*'):
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
    except Exception as e:
        logging.error(f"Error occured while cleaning temp folder: {e}")

    try:
        # delete run box history
        subprocess.run(['reg', 'delete', 'HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RunMRU', '/va', '/f'], shell=True, check=True,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    except Exception as e:
        logging.error(f"Error occured while deleting run box history: {e}")

    try:
        # delete PowerShell history
        history_path = pathlib.Path.home() / 'AppData' / 'Roaming' / 'Microsoft' / 'Windows' / 'PowerShell' / 'PSReadline' / 'ConsoleHost_history.txt'
        history_path.unlink(missing_ok=True)
    except Exception as e:
        logging.error(f"Error occured while deleting PowerShell history: {e}")

    try:
        # empty recycle bin
        recycle_bin = pathlib.Path('C:\\$Recycle.Bin')
        if recycle_bin.exists():
            shutil.rmtree(recycle_bin)
    except Exception as e:
        logging.error(f"Error occured while emptying recycle bin: {e}")
