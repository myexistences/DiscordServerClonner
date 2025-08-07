from utils.innit import *
import time

async def cloner():
    clear()
    logo()
    g_id = input(f"                {b}[{w}Source Guild ID{b}]{w} >> ")
    p_id = input(f"                {b}[{w}Paste Guild ID{b}]{w} >> ")
    clear()
    logo()

    with open('token.txt') as f:
        token = f.readline().strip()

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    channel_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
    response = requests.get(channel_url, headers=headers)

    if response.status_code == 200:
        channels = response.json() 
        for channel in channels:
            delete_channel_url = f"https://discord.com/api/v9/channels/{channel['id']}"
            delete_channel = requests.delete(delete_channel_url, headers=headers)
            if delete_channel.status_code in [200, 204]:  
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Deleted channel: {channel['name']}")
    
            else:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to delete channel {channel['name']}: {delete_channel.status_code}")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to fetch channels: {response.status_code}")

    role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles"
    response = requests.get(role_url, headers=headers)

    if response.status_code == 200:
        roles = response.json()
        for role in roles:
            delete_role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles/{role['id']}"
            while True:  
                delete_response = requests.delete(delete_role_url, headers=headers)
                if delete_response.status_code in [200, 204]:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Deleted role: {role['name']}")
                    break
                elif delete_response.status_code == 429:
                    retry_after = int(delete_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate-limited. Retrying after {retry_after} seconds")
                    time.sleep(retry_after)
                elif delete_response.status_code == 400:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Skipped role: {role['name']} (possibly @everyone)")
                    break
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to delete role: {role['name']} = {delete_response.status_code}")
                    break
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to fetch roles: {response.status_code}")

    guild_url = f"https://discord.com/api/v9/guilds/{g_id}"
    response = requests.get(guild_url, headers=headers)

    if response.status_code == 200:
        guild = response.json()
        guild_name_url = f"https://discord.com/api/v9/guilds/{p_id}"
        if guild['icon']:
            icon_url = f"https://cdn.discordapp.com/icons/{g_id}/{guild['icon']}.png"
            icon_response = requests.get(icon_url)

            if icon_response.status_code == 200:
                icon_base64 = base64.b64encode(icon_response.content).decode('utf-8')
                icon_data = f"data:image/png;base64,{icon_base64}"
            else:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Failed to fetch guild icon. Continuing without icon.")
                icon_data = None
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Guild has no icon. Continuing without icon.")
            icon_data = None

        payload = {
            "name": guild['name']
        }
        if icon_data:
            payload["icon"] = icon_data

        change_name = requests.patch(guild_name_url, headers=headers, json=payload)
        if change_name.status_code == 200:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Changed server name to: {guild['name']}")
            if icon_data:
                t = current_time()
                print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Updated the server icon.")
        else:
            t = current_time()
            print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to change server name/icon: {change_name.status_code}")
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to fetch guild details: {response.status_code}")

    get_channels_url = f"https://discord.com/api/v9/guilds/{g_id}/channels"
    response = requests.get(get_channels_url, headers=headers)

    if response.status_code == 200:
        source_channels = response.json()
        
        categories = [ch for ch in source_channels if ch['type'] == 4]
        channels = [ch for ch in source_channels if ch['type'] != 4]

        categories.sort(key=lambda x: x['position'])
        channels.sort(key=lambda x: x['position'])

        created_categories = {}
        for category in categories:
            payload = {
                "name": category['name'],
                "type": 4,  
                "permission_overwrites": category['permission_overwrites']
            }
            create_category_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
            while True:
                create_response = requests.post(create_category_url, headers=headers, json=payload)
                if create_response.status_code == 201:
                    created_category = create_response.json()
                    created_categories[category['id']] = created_category['id']  
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Created category: {category['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate-limited. Retrying after {retry_after} seconds")
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to create category: {category['name']} = {create_response.status_code}")
                    break

        for channel in channels:
            payload = {
                "name": channel['name'],
                "type": channel['type'],
                "parent_id": created_categories.get(channel['parent_id']),  
                "permission_overwrites": channel['permission_overwrites'],
                "topic": channel.get('topic', ''),
                "nsfw": channel.get('nsfw', False),
                "rate_limit_per_user": channel.get('rate_limit_per_user', 0),
            }
            create_channel_url = f"https://discord.com/api/v9/guilds/{p_id}/channels"
            while True:
                create_response = requests.post(create_channel_url, headers=headers, json=payload)
                if create_response.status_code == 201:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Created channel: {channel['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Ratelimited. Retrying after {retry_after} seconds")
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to create channel: {channel['name']} = {create_response.status_code}")
                    break
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to fetch channels from source guild: {response.status_code}")

    get_roles_url = f"https://discord.com/api/v9/guilds/{g_id}/roles"
    response = requests.get(get_roles_url, headers=headers)

    if response.status_code == 200:
        source_roles = response.json()
        source_roles.sort(key=lambda x: x['position'], reverse=True)

        for role in source_roles:
            payload = {
                "name": role['name'],
                "permissions": role['permissions'],
                "color": role['color'],
                "hoist": role['hoist'],
                "mentionable": role['mentionable']
            }
            create_role_url = f"https://discord.com/api/v9/guilds/{p_id}/roles"
            while True:
                create_response = requests.post(create_role_url, headers=headers, json=payload)
                if create_response.status_code in [201, 200]:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {g}[+]{w} Created role: {role['name']}")
                    break
                elif create_response.status_code == 429:
                    retry_after = int(create_response.headers.get("Retry-After", 1))
                    print(f"                {b}[{w}{t}{b}]{w} {y}[x]{w} Rate-limited. Retrying after {retry_after} seconds")
                    time.sleep(retry_after)
                else:
                    t = current_time()
                    print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to create role: {role['name']} {create_response.status_code}")
                    break
            time.sleep(2)
    else:
        t = current_time()
        print(f"                {b}[{w}{t}{b}]{w} {r}[-]{w} Failed to fetch roles from source guild: {response.status_code}")