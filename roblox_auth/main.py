import os
import subprocess
import platform
import requests
import threading
import re

class AccountLaunch:
    def __init__(self, cookie: str, placeId: [int, str], VIP: bool, privateServerLink: str):
        self.cookie = cookie
        self.placeId = placeId
        self.VIP = VIP
        self.privateServerLink = privateServerLink

    # get x-csrf-token
    def get_xsrf(self):
        auth_url = "https://auth.roblox.com/v2/logout"
        xsrf_request = requests.post(auth_url, cookies={'.ROBLOSECURITY': self.cookie})
        return xsrf_request.headers["x-csrf-token"]

    # opens a ticket to join a server
    def get_authentication_ticket(self):
        launch_url = 'https://auth.roblox.com/v1/authentication-ticket/'
        response = requests.post(launch_url, headers={'X-CSRF-Token': self.get_xsrf(), "Referer": "https://www.roblox.com/games/4924922222/Brookhaven-RP"}, cookies={'.ROBLOSECURITY': self.cookie})
        ticket = response.headers.get("rbx-authentication-ticket", "")
        return ticket

    # gets server id
    def job_id(self):
        try:
            response = requests.get("https://games.roblox.com/v1/games/10515146389/servers/0?sortOrder=1&excludeFullGames=true&limit=25").json()
            data = response["data"][7]
            return data["id"]
        except KeyError:
            response = requests.get("https://games.roblox.com/v1/games/10515146389/servers/0?sortOrder=1&excludeFullGames=true&limit=25").json()
            data = response["data"][4]
            return data["id"]
    
    def get_link_code(self):
        url = self.privateServerLink

        link_code_match = re.search(r'privateServerLinkCode=(\d+)', url)

        LinkCode = link_code_match.group(1) if link_code_match else ''
        return LinkCode
    
    # launch roblox function opens roblox with the inserted roblox cookie
    def launch_roblox(self, ticket, job_id):
        roblox_executable_path = None
        current_version = requests.get("https://clientsettings.roblox.com/v1/client-version/WindowsPlayer").json()["clientVersionUpload"]
        r_path = os.path.join("C:\\Program Files (x86)\\Roblox\\Versions", current_version)
        
        if not os.path.exists(r_path):
            r_path = os.path.join(os.environ.get("LocalAppData"), "Roblox\\Versions", current_version)

        if not os.path.exists(r_path):
            return "ERROR: Failed to find ROBLOX executable"

        roblox_executable_path = os.path.join(r_path, "RobloxPlayerBeta.exe")

        arguments = ""
        if self.VIP:
            arguments = f"--app -t {ticket} -j \"https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestPrivateGame&placeId={self.placeId}&linkCode={self.get_link_code()}\"" # &accessCode={self.privateServerLink}
        else:
            arguments = f"--app -t {ticket} -j \"https://assetgame.roblox.com/game/PlaceLauncher.ashx?request=RequestGame{'' if not job_id else 'Job'}&placeId={self.placeId}{'' if not job_id else '&gameId=' + job_id}&isPlayTogetherGame=false\""
        
        if platform.system() == "Windows":
            subprocess.Popen([roblox_executable_path, arguments])
        
        return "Success"
    
# can launch multiple roblox accounts.
def multi_roblox():
    def roblox_m():
        import win32event
        mutex_name = "ROBLOX_singletonMutex"
        mutex = win32event.CreateMutex(None, 1, mutex_name)

        # Infinite Loop so we don't close the instances!
        while True:
            pass

        win32event.ReleaseMutex(mutex)

    # Start multi roblox silently
    Multi_thread = threading.Thread(target=roblox_m)
    Multi_thread.start()
    return True

# Launch account premade function
def launch_account(cookie: str, placeId, VIP: bool, privateServerLink: str):
    privateServerLink = privateServerLink or ""

    Manager = AccountLaunch(cookie, placeId, VIP, privateServerLink)
    authticket = Manager.get_authentication_ticket()
    server_id = Manager.job_id()

    Manager.launch_roblox(authticket, server_id)
    
    return True