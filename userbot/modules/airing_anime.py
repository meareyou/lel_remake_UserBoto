import datetime
import json
import requests
import asyncio
from userbot import CMD_HELP
from userbot.events import register


def t(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " Days, ") if days else "") + \
        ((str(hours) + " Hours, ") if hours else "") + \
        ((str(minutes) + " Minutes, ") if minutes else "") + \
        ((str(seconds) + " Seconds, ") if seconds else "") + \
        ((str(milliseconds) + " ms, ") if milliseconds else "")
  return tmp[:-2]
 

def ani_api(search_str):
    query = '"""
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        siteUrl
        bannerImage 
        episodes
        title {
          romaji
          english
          native        
        }
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        } 
      }
    }
    """
    variables = {
        'search' : search_str
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})
    return response.text   

async def formatJson(data_str):
     msg = ""
     jsonData = json.loads(data_str)                                                                                                                                                                  
     res = list(jsonData.keys())      
     if "errors" in res:
           msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
        else:
     jsonData = jsonData["data"]["media"]
      if "bannerImage" in jsonData.keys():
             image = jsonData["bannerImage"]
          else:
             msg = f"*Name*: *{jsonData['title']['romaji']}*(`{jsonData['title']['native']}`)\n*ID*: `{jsonData['id']}`[⁠ ⁠]({image})"
     if jsonData['nextAiringEpisode']:
         time = jsonData['nextAiringEpisode']['timeUntilAiring'] * 1000
         time = t(time)
         msg += f"\n*Episode*: `{jsonData['nextAiringEpisode']['episode']}`\n*Airing In*: `{time}`"
     else:
         msg += f"\n*Episode*:{jsonData['episodes']}\n*Status*: `N/A`"
     return msg
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
 @register(outgoing=True, pattern=r"^\.airings ?(.*)")
    async def ani_airings(event):
     if event.fwd_from:    
       return
       message = await event.get_reply_message()
       search_query = event.pattern_match.group(1)              
       if search_query:
            pass
        elif message:
            search_query = message.text
         else:
            await event.edit("Format: `.airings <anime name>`")
        return      
           result = await ani_api(search_query)
           msg = await formatJSON(result)
           await event.edit(msg, link_preview=True)
     
