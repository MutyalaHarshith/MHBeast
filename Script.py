class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href=https://t.me/MutyalaHarshith>Mutyala Harshith</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- ముత్యాల హర్షిత్ ఓపెన్ సోర్స్ ప్రాజెక్ట్ కాదు. 
- మూలం - అందుబాటులో లేదు 😜😜😜  

<b>DEVS:</b>
- <a href=https://t.me/MutyalaHarshith>Mutyala Harshith</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- ఫిల్టర్ అనేది ఒక నిర్దిష్ట కీవర్డ్ కోసం వినియోగదారులు స్వయంచాలక ప్రత్యుత్తరాలను సెట్ చేయగల లక్షణం మరియు సందేశం కనుగొనబడినప్పుడు హర్షిత్ ప్రతిస్పందిస్తారు

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- హర్షిత్ url మరియు అలర్ట్ ఇన్‌లైన్ బటన్‌లు రెండింటికీ మద్దతు ఇస్తుంది.

<b>NOTE:</b>
1. ఎటువంటి కంటెంట్ లేకుండా బటన్‌లను పంపడానికి టెలిగ్రామ్ మిమ్మల్ని అనుమతించదు, కాబట్టి కంటెంట్ తప్పనిసరి.
2. హర్షిత్ ఏదైనా టెలిగ్రామ్ మీడియా రకం బటన్‌లను సపోర్ట్ చేస్తుంది.
3. బటన్‌లు మార్క్‌డౌన్ ఫార్మాట్‌గా సరిగ్గా అన్వయించబడాలి

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/MHGcBoT)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:ఇది హెచ్చరిక సందేశం)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. మీ ఛానెల్ ప్రైవేట్‌గా ఉంటే నన్ను దానికి అడ్మిన్‌గా చేయండి.
2. మీ ఛానెల్‌లో క్యామ్‌రిప్‌లు, పోర్న్ మరియు నకిలీ ఫైల్‌లు లేవని నిర్ధారించుకోండి.
3. కోట్‌లతో చివరి సందేశాన్ని నాకు ఫార్వార్డ్ చేయండి.
 నేను ఆ ఛానెల్‌లోని అన్ని ఫైల్‌లను నా dbకి జోడిస్తాను."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- ఫిల్టర్‌లను నిర్వహించడానికి బాట్‌ను PMకి కనెక్ట్ చేయడానికి ఉపయోగించబడుతుంది
- ఇది సమూహాలలో స్పామింగ్‌ను నివారించడానికి సహాయపడుతుంది.

<b>NOTE:</b>
1. నిర్వాహకులు మాత్రమే కనెక్షన్‌ని జోడించగలరు.
2. పంపండి <code>/connect</code> నన్ను మీ PMకి కనెక్ట్ చేసినందుకు

<b>Commands and Usage:</b>
• /connect  - <code>మీ PMకి నిర్దిష్ట చాట్‌ని కనెక్ట్ చేయండి</code>
• /disconnect  - <code>చాట్ నుండి డిస్‌కనెక్ట్ చేయండి</code>
• /connections - <code>మీ అన్ని కనెక్షన్లను జాబితా చేయండి</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
ఇవి హర్షిత్ యొక్క అదనపు లక్షణాలు

<b>Commands and Usage:</b>
• /id - <code>పేర్కొన్న వినియోగదారు ఐడిని పొందండి.</code>
• /info  - <code>వినియోగదారు గురించి సమాచారాన్ని పొందండి.</code>
• /imdb  - <code>IMDb మూలం నుండి సినిమా సమాచారాన్ని పొందండి.</code>
• /search  - <code>వివిధ మూలాల నుండి సినిమా సమాచారాన్ని పొందండి.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
ఈ మాడ్యూల్ నా నిర్వాహకులకు మాత్రమే పని చేస్తుంది

<b>Commands and Usage:</b>
• /logs - <code>ఇటీవలి లోపాలను పొందడానికి</code>
• /MHstats - <code>dbలో ఫైల్‌ల స్థితిని పొందడానికి.</code>
• /delete - <code>db నుండి నిర్దిష్ట ఫైల్‌ను తొలగించడానికి.</code>
• /MHusers - <code>నా వినియోగదారులు మరియు IDల జాబితాను పొందడానికి.</code>
• /chats - <code>నా చాట్‌లు మరియు ఐడిల జాబితాను పొందడానికి </code>
• /MHleave  - <code>చాట్ నుండి నిష్క్రమించడానికి.</code>
• /MHdisable  -  <code>చాట్‌ని డిసేబుల్ చేయండి.</code>
• /MHban  - <code>వినియోగదారుని నిషేధించడానికి.</code>
• /MHunban  - <code>వినియోగదారుని నిషేధాన్ని తీసివేయడానికి.</code>
• /channel - <code>కనెక్ట్ చేయబడిన మొత్తం ఛానెల్‌ల జాబితాను పొందడానికి</code>
• /MHbroadcast - <code>వినియోగదారులందరికీ సందేశాన్ని ప్రసారం చేయడానికి</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup of @MHGcBoT
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser of @MHGcBoT
ID - <code>{}</code>
Name - {}
"""
