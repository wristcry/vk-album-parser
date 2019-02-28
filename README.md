# A parsing script for VK social network.

### Requirements:
- Python 3
- https://github.com/python273/vk_api

### Configuration:
When you run this script first time, it create a configuration file with 4 parameters:
- Login
- Password
- Group_URL
- Offset

1. In "login", you need to put your VK login, or phone number which linked to your VK account.
2. In "Password", you need to put your VK password.
3. In "Group_URL", you need to put a URL of the group from whose albums you want to parse photos without "https://vk.com/"
4. By changing "Offset" you can 'bypass' the 1000 photos limit per request. Just increase it by 1000 every time after you will parse 1000 photos.

### Usage:
1. Fill "Configuration.ini"
2. Run the script.
3. Profit! Parsed albums will be saved at "parsed" directory.