import ctypes
import os
import winreg

def set_wallpaper(image, style):
    # Available styles
    styles = {
        "Fill": 10,
        "Fit": 6,
        "Stretch": 2,
        "Tile": 0,
        "Center": 0,
        "Span": 22
    }
    wallpaper_style = styles.get(style, 0)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, winreg.KEY_WRITE)
        # Set wallpaper style
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(wallpaper_style))
        # Set tile wallpaper
        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, "1" if style == "Tile" else "0")
        winreg.CloseKey(key)
    except WindowsError as e:
        print(f"Failed to set wallpaper style and tile wallpaper: {e}")

    # Set desktop wallpaper
    SPI_SETDESKWALLPAPER = 0x0014
    update_ini_file = 0x01
    send_change_event = 0x02
    fWinIni = update_ini_file | send_change_event
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image, fWinIni)
    if not result:
        print("Failed to set desktop wallpaper")

# Example usage you need to change path to the image u wanna use
username = os.getlogin()
set_wallpaper(f"C:\\Users\\{username}\\Pictures\\image.jpg", "Fit")
