import os
import re
from collections import defaultdict
from typing import Dict, List

def get_browser_data(browser: str, data_type: str) -> List[Dict[str, str]]:
    result = []

    if browser not in ["chrome", "edge", "firefox", "ie", "safari"]:
        print("Invalid browser type")
        return result

    if data_type not in ["history", "bookmarks"]:
        print("Invalid data type")
        return result

    regex = '(http|https)://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)*?'
    browser_data_paths = defaultdict(lambda: defaultdict(str))
    browser_data_paths["chrome"]["history"] = os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/History")
    browser_data_paths["chrome"]["bookmarks"] = os.path.expanduser("~/AppData/Local/Google/Chrome/User Data/Default/Bookmarks")
    browser_data_paths["edge"]["history"] = os.path.expanduser("~/AppData/Local/Microsoft/Edge/User Data/Default/History")
    browser_data_paths["edge"]["bookmarks"] = os.path.expanduser("~/AppData/Local/Microsoft/Edge/User Data/Default/Bookmarks")
    browser_data_paths["firefox"]["history"] = os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles/*.default-release/places.sqlite")
    browser_data_paths["firefox"]["bookmarks"] = os.path.expanduser("~/AppData/Roaming/Mozilla/Firefox/Profiles/*.default-release/bookmarks.html")
    browser_data_paths["ie"]["history"] = os.path.expanduser("~/AppData/Local/Microsoft/Internet Explorer/History")
    browser_data_paths["ie"]["bookmarks"] = os.path.expanduser("~/Favorites")
    browser_data_paths["safari"]["history"] = os.path.expanduser("~/Library/Safari/History.plist")
    browser_data_paths["safari"]["bookmarks"] = os.path.expanduser("~/Library/Safari/Bookmarks.plist")

    path = browser_data_paths[browser][data_type]

    if os.path.exists(path):
        with open(path, 'r') as f:
            content = f.read()
            matches = re.findall(regex, content)
            matches = list(set(matches))
            for match in matches:
                result.append({
                    "user": os.getlogin(),
                    "browser": browser,
                    "data_type": data_type,
                    "data": match
                })
    else:
        print(f"{path} not found")

    return result
