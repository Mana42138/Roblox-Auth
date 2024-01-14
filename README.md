[![Latest Downloads](https://img.shields.io/github/downloads/ic3w0lf22/Roblox-Account-Manager/latest/total)](https://github.com/Mana42138/Roblox-Auth/releases/download/roblox-auth/Roblox-Auth-main.zip)
[![Discord](https://img.shields.io/discord/871845273800957982?label=Discord)](https://discord.gg/Af7HahqdzF)
# Roblox Account Launcher

This Python package provides a simple interface for launching Roblox games using an authenticated account. It includes functions to obtain necessary authentication tokens and launch a specified Roblox game.

## Prerequisites

Before using this package, ensure that you have the following installed:

- Python 3
- Required Python packages: `requests pywin32`

## Usage

1. Import the `AccountLaunch` class from the package.

   ```python
   from roblox_auth import AccountLaunch, multi_roblox, launch_account
   ```

2. Initialize an `AccountLaunch` object with the Roblox account's cookie and the target place ID.

   ```python
   account_launcher = AccountLaunch(cookie="your_cookie_here", placeId="target_place_id", VIP=True, privateServerLink="your_private_server_link")
   ```

3. Obtain the required authentication tokens.

   ```python
   xsrf_token = account_launcher.get_xsrf()
   authentication_ticket = account_launcher.get_authentication_ticket()
   ```

4. Retrieve the Job ID for the target game.

   ```python
   job_id = account_launcher.job_id()
   ```

5. Add Multi Roblox on launch if wanted.

   ```python
   multi_roblox()
   ```

6. Launch Roblox with the specified parameters.

   ```python
   launch_result = account_launcher.launch_roblox(ticket=authentication_ticket, job_id=job_id)
   print(launch_result)
   ```

7. Easier way to launch roblox.

   ```python
   from roblox_auth import AccountLaunch, multi_roblox, launch_account
   launch_account(cookie="your_cookie_here", placeId="target_place_id", VIP=True, privateServerLink="your_private_server_link")
   ```

## Notes

- The package assumes that Roblox is installed in the default directory on Windows. If not, it attempts to find the installation path in the local AppData directory.
- Ensure that the required packages are installed using `pip install requests pywin32`.
- The package supports multi roblox instances as long as the program stays open.

## Example

```python
from roblox_auth import AccountLaunch, multi_roblox, launch_account

# Initialize AccountLaunch object
account_launcher = AccountLaunch(cookie="your_cookie_here", placeId="target_place_id", VIP=True, privateServerLink="your_private_server_link")

# Get authentication tokens
xsrf_token = account_launcher.get_xsrf()
authentication_ticket = account_launcher.get_authentication_ticket()

# Get the Job ID
job_id = account_launcher.job_id()

# Add Multi Roblox
multi_roblox()

# Launch Roblox
launch_result = account_launcher.launch_roblox(ticket=authentication_ticket, job_id=job_id)
print(launch_result)

# Easier way to launch account without other functions
launch_account(cookie="your_cookie_here", placeId="target_place_id", VIP=True, privateServerLink="your_private_server_link")
```
