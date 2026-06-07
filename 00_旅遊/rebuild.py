import json

with open("/Users/foongotino/Documents/00_旅遊/data.js") as f:
    raw = f.read()

start = len("var DATA=")
end = raw.index("var VOICE=")
data = json.loads(raw[start:end].rstrip().rstrip(';'))

voice_str = raw[raw.index("var VOICE=") + len("var VOICE="):].rstrip().rstrip(';')
voice = json.loads(voice_str)

# Updated itinerary
data['days'] = [
  {"ti": "Day 1 | 4/17 | 準備出發", "ci": "美國", "ss": [{"tm": "全天", "ac": "整理行李、確認證件、提前3小時到機場", "tg": "leisure", "p": ""}]},
  {"ti": "Day 2 | 4/18 | 飛往台灣→胡志明市", "ci": "飛機/胡志明市", "ss": [
    {"tm": "00:10", "ac": "CI 0023 起飛 — 安大略 ONT→台北 TPE", "tg": "flight", "p": "Ontario International Airport"},
    {"tm": "05:15", "ac": "抵達台北 TPE，轉機候機", "tg": "flight", "p": "Taiwan Taoyuan International Airport"},
    {"tm": "07:15", "ac": "CI 0781 起飛 — 台北 TPE→胡志明市 SGN", "tg": "flight", "p": "Taiwan Taoyuan International Airport"},
    {"tm": "09:25", "ac": "抵達胡志明市 SGN，入境提行李", "tg": "flight", "p": "Tan Son Nhat International Airport"},
    {"tm": "下午", "ac": "入住 Sherwood Residence（4/18-4/22）", "tg": "hotel", "p": "Sherwood Residence Ho Chi Minh City"},
    {"tm": "晚", "ac": "就近品嚐 Phở Chay（素食河粉）", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 3 | 4/19 | 胡志明市—市區觀光", "ci": "胡志明市", "ss": [
    {"tm": "08:00", "ac": "早餐：越南法棍 Bánh Mì", "tg": "food", "p": "Banh Mi HCMC"},
    {"tm": "09:00", "ac": "統一宮 Reunification Palace", "tg": "sightseeing", "p": "Reunification Palace"},
    {"tm": "11:00", "ac": "聖母大教堂（粉紅教堂）", "tg": "sightseeing", "p": "Saigon Notre-Dame Basilica"},
    {"tm": "12:30", "ac": "午餐：Quan Chay Nhu 素食", "tg": "food", "p": "Quan Chay Nhu District 1 HCMC"},
    {"tm": "14:00", "ac": "中央郵政局", "tg": "sightseeing", "p": "Saigon Central Post Office"},
    {"tm": "15:30", "ac": "書街 Saigon Book Street", "tg": "sightseeing", "p": "Saigon Book Street"},
    {"tm": "18:00", "ac": "晚餐：酒店附近素食", "tg": "food", "p": ""},
    {"tm": "19:30", "ac": "阮廌路散步街夜景", "tg": "sightseeing", "p": "Nguyen Hue Walking Street"}
  ]},
  {"ti": "Day 4 | 4/20 | 胡志明市—網紅打卡日", "ci": "胡志明市", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:30", "ac": "The Cafe Apartment 7層網紅咖啡店", "tg": "instagram", "p": "The Cafe Apartment Ho Chi Minh City"},
    {"tm": "11:30", "ac": "咖啡公寓 44 Pho Hue", "tg": "instagram", "p": "Coffee Apartment 44 Pho Hue"},
    {"tm": "13:00", "ac": "午餐：Cay Da Vegetarian", "tg": "food", "p": "Cay Da Vegetarian HCMC"},
    {"tm": "15:00", "ac": "Le Café des Stagiaires 屋頂酒吧", "tg": "instagram", "p": "Le Cafe des Stagiaires HCMC"},
    {"tm": "17:30", "ac": "Banana Mama Rooftop Bar 看夕陽", "tg": "instagram", "p": "Banana Mama Rooftop Bar HCMC"},
    {"tm": "20:00", "ac": "晚餐：Hum Garden 米其林", "tg": "food", "p": "Hum Garden Ho Chi Minh City"}
  ]},
  {"ti": "Day 5 | 4/21 | 胡志明市—文化體驗", "ci": "胡志明市", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:00", "ac": "戰爭博物館 War Remnants Museum", "tg": "sightseeing", "p": "War Remnants Museum"},
    {"tm": "11:00", "ac": "美術博物館 Fine Arts Museum", "tg": "sightseeing", "p": "Fine Arts Museum Ho Chi Minh"},
    {"tm": "13:00", "ac": "午餐：Loving Hut 連鎖素食", "tg": "food", "p": "Loving Hut Ho Chi Minh City"},
    {"tm": "15:00", "ac": "范五老街 Pham Ngu Lao 逛街", "tg": "shopping", "p": "Pham Ngu Lao Street"},
    {"tm": "18:00", "ac": "Ben Thanh Market 夜市", "tg": "shopping", "p": "Ben Thanh Market"},
    {"tm": "20:00", "ac": "晚餐：安東市場素食小吃", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 6 | 4/22 | 胡志明市→芽莊（VN 1344）", "ci": "芽莊", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:30", "ac": "西宮會館 Mariamman Temple 印度廟", "tg": "sightseeing", "p": "Mariamman Temple Saigon"},
    {"tm": "11:00", "ac": "天后宮 Thien Hau Temple", "tg": "sightseeing", "p": "Thien Hau Temple"},
    {"tm": "13:00", "ac": "午餐：Vị Quê Kitchen 米其林", "tg": "food", "p": "Vi Que Kitchen Ho Chi Minh"},
    {"tm": "14:00", "ac": "Ben Thanh Market 最後購物", "tg": "shopping", "p": "Ben Thanh Market"},
    {"tm": "16:00", "ac": "退房，前往機場", "tg": "hotel", "p": ""},
    {"tm": "17:00", "ac": "VN 1344 起飛 — 胡志明市 SGN→芽莊 CXR", "tg": "flight", "p": "Tan Son Nhat International Airport"},
    {"tm": "18:00", "ac": "抵達芽莊 CXR，前往酒店", "tg": "flight", "p": "Cam Ranh International Airport"},
    {"tm": "晚上", "ac": "入住 Sunrise Nha Trang Beach Hotel（4/22-4/26）", "tg": "hotel", "p": "Sunrise Nha Trang Beach Hotel"},
    {"tm": "晚", "ac": "芽莊海灘散步 + 海灘夜市", "tg": "leisure", "p": "Nha Trang Beach"}
  ]},
  {"ti": "Day 7 | 4/23 | 芽莊—海灘與網紅", "ci": "芽莊", "ss": [
    {"tm": "06:30", "ac": "芽莊海灘日出", "tg": "sightseeing", "p": "Nha Trang Beach"},
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:30", "ac": "Ola Cafe 摩洛哥風建築", "tg": "instagram", "p": "Ola Cafe Nha Trang"},
    {"tm": "12:00", "ac": "午餐：海灘附近餐廳", "tg": "food", "p": ""},
    {"tm": "14:00", "ac": "婆那加塔 Po Nagar Cham Towers", "tg": "sightseeing", "p": "Po Nagar Cham Towers"},
    {"tm": "16:30", "ac": "Jungle Coffee 叢林風咖啡廳", "tg": "instagram", "p": "Jungle Coffee Nha Trang"},
    {"tm": "18:30", "ac": "海灘夕陽", "tg": "leisure", "p": "Nha Trang Beach"},
    {"tm": "20:00", "ac": "晚餐：Good Morning Vietnam", "tg": "food", "p": "Good Morning Vietnam Nha Trang"}
  ]},
  {"ti": "Day 8 | 4/24 | 芽莊—跳島/一日遊", "ci": "芽莊", "ss": [
    {"tm": "08:00", "ac": "跳島一日遊或 Vinpearl Land", "tg": "leisure", "p": "Nha Trang"},
    {"tm": "12:00", "ac": "午餐：島上/園區內", "tg": "food", "p": ""},
    {"tm": "15:00", "ac": "返回市區", "tg": "leisure", "p": ""},
    {"tm": "17:00", "ac": "酒店泳池/海灘", "tg": "leisure", "p": ""},
    {"tm": "20:00", "ac": "晚餐：當地素食餐廳", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 9 | 4/25 | 芽莊—放鬆日", "ci": "芽莊", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:00", "ac": "上午沙灘/泳池", "tg": "leisure", "p": "Nha Trang Beach"},
    {"tm": "11:00", "ac": "Spa/傳統按摩", "tg": "leisure", "p": ""},
    {"tm": "13:00", "ac": "午餐：海邊素食餐廳", "tg": "food", "p": ""},
    {"tm": "15:00", "ac": "Nha Trang Center 商場", "tg": "shopping", "p": "Nha Trang Center"},
    {"tm": "18:00", "ac": "海灘最後夕陽", "tg": "leisure", "p": "Nha Trang Beach"},
    {"tm": "20:00", "ac": "海灘燭光晚餐", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 10 | 4/26 | 芽莊→大叻（包車）", "ci": "大叻", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:00", "ac": "退房，包車出發前往大叻（車程約3.5-4小時）", "tg": "leisure", "p": "Nha Trang"},
    {"tm": "12:00", "ac": "抵達大叻，入住 Swiss Belresort Tuyen Lam（4/26-4/28）", "tg": "hotel", "p": "Swiss Belresort Tuyen Lam Dalat"},
    {"tm": "13:00", "ac": "午餐：酒店/當地素食", "tg": "food", "p": ""},
    {"tm": "15:00", "ac": "Ixora Dalat 網美花園", "tg": "instagram", "p": "Ixora Dalat"},
    {"tm": "17:30", "ac": "大叻湖 Xuan Huong Lake 散步", "tg": "sightseeing", "p": "Xuan Huong Lake Dalat"},
    {"tm": "19:00", "ac": "晚餐：當地法式料理/素食", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 11 | 4/27 | 大叻—浪漫山城", "ci": "大叻", "ss": [
    {"tm": "07:30", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "08:30", "ac": "Mê Linh Coffee Garden 雲霧咖啡園", "tg": "instagram", "p": "Me Linh Coffee Garden Dalat"},
    {"tm": "10:30", "ac": "Dalat Flower Park 法式花園", "tg": "sightseeing", "p": "Dalat Flower Park"},
    {"tm": "12:30", "ac": "午餐：Lien Hoa Vegetarian", "tg": "food", "p": "Lien Hoa Vegetarian Dalat"},
    {"tm": "14:00", "ac": "Crazy House 奇幻建築", "tg": "sightseeing", "p": "Crazy House Dalat"},
    {"tm": "16:00", "ac": "Robin Hill 俯瞰大叻全景", "tg": "instagram", "p": "Robin Hill Dalat"},
    {"tm": "18:00", "ac": "大叻夜市", "tg": "shopping", "p": "Da Lat Night Market"},
    {"tm": "20:00", "ac": "晚餐：夜市素食小吃", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 12 | 4/28 | 大叻→胡志明市（包車）", "ci": "胡志明市", "ss": [
    {"tm": "07:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "08:00", "ac": "退房，包車出發前往胡志明市（車程約5-6小時）", "tg": "leisure", "p": "Dalat to Ho Chi Minh"},
    {"tm": "13:00", "ac": "途中午餐", "tg": "food", "p": ""},
    {"tm": "14:00", "ac": "抵達胡志明市，入住 Sherwood Residence（4/28-4/29）", "tg": "hotel", "p": "Sherwood Residence Ho Chi Minh City"},
    {"tm": "晚上", "ac": "素食餐廳 + 早點休息", "tg": "food", "p": ""}
  ]},
  {"ti": "Day 13 | 4/29 | 胡志明市→台灣", "ci": "台灣", "ss": [
    {"tm": "08:00", "ac": "早餐：酒店早餐", "tg": "food", "p": ""},
    {"tm": "09:00", "ac": "退房，最後自由活動/購物", "tg": "shopping", "p": ""},
    {"tm": "10:50", "ac": "CI 0782 起飛 — 胡志明市 SGN→台北 TPE", "tg": "flight", "p": "Tan Son Nhat International Airport"},
    {"tm": "15:20", "ac": "抵達台北 TPE，通關入境", "tg": "flight", "p": "Taiwan Taoyuan International Airport"},
    {"tm": "下午", "ac": "入住 Grand Forward Hotel（板橋，4/29-5/2）", "tg": "hotel", "p": "Grand Forward Hotel Banqiao New Taipei"},
    {"tm": "晚上", "ac": "板橋夜市/便利店素食", "tg": "food", "p": "Banqiao Night Market"}
  ]},
  {"ti": "Day 14 | 4/30 | 台北—城市探索", "ci": "台北", "ss": [
    {"tm": "07:30", "ac": "早餐：便利商店素食", "tg": "food", "p": "7-Eleven Taiwan"},
    {"tm": "09:00", "ac": "龍山寺 Longshan Temple", "tg": "sightseeing", "p": "Longshan Temple Taipei"},
    {"tm": "10:30", "ac": "剝皮寮歷史街區", "tg": "sightseeing", "p": "Bopiliao Historic District"},
    {"tm": "11:30", "ac": "西門町 Ximending", "tg": "shopping", "p": "Ximending Taipei"},
    {"tm": "13:00", "ac": "午餐：師大夜市素食", "tg": "food", "p": "Shida Night Market"},
    {"tm": "14:30", "ac": "中正紀念堂 Chiang Kai-shek Memorial Hall", "tg": "sightseeing", "p": "Chiang Kai-shek Memorial Hall"},
    {"tm": "16:30", "ac": "信義商圈/101外觀", "tg": "shopping", "p": "Taipei 101"},
    {"tm": "18:00", "ac": "象山步道 101夜景", "tg": "instagram", "p": "Xiangshan Trail Taipei"},
    {"tm": "20:00", "ac": "晚餐：寧夏夜市素食", "tg": "food", "p": "Ningxia Night Market"}
  ]},
  {"ti": "Day 15 | 5/1 | 台北—悠閒日", "ci": "台北", "ss": [
    {"tm": "08:00", "ac": "早餐：便利商店/飯店早餐", "tg": "food", "p": ""},
    {"tm": "09:30", "ac": "迪化街（年貨大街）", "tg": "sightseeing", "p": "Dihua Street Taipei"},
    {"tm": "11:00", "ac": "大稻埕碼頭、碼頭咖啡", "tg": "leisure", "p": "Dajia Riverside Park"},
    {"tm": "13:00", "ac": "午餐：保安宮附近素食", "tg": "food", "p": ""},
    {"tm": "15:00", "ac": "華山1914文化創意產業園區", "tg": "sightseeing", "p": "Huashan 1914 Creative Park"},
    {"tm": "18:00", "ac": "饒河街夜市", "tg": "food", "p": "Raohe Street Night Market"},
    {"tm": "晚", "ac": "整理行李，早點休息", "tg": "leisure", "p": ""}
  ]},
  {"ti": "Day 16 | 5/2 | 九份→返美", "ci": "九份/機場", "ss": [
    {"tm": "07:30", "ac": "早餐：飯店早餐", "tg": "food", "p": ""},
    {"tm": "08:30", "ac": "出發前往九份（車程約1小時）", "tg": "leisure", "p": ""},
    {"tm": "09:30", "ac": "豎崎路 宮崎駿靈感地", "tg": "sightseeing", "p": "Shukadan Road Jiufen"},
    {"tm": "10:30", "ac": "阿妹茶樓", "tg": "instagram", "p": "A-Mei Tea House Jiufen"},
    {"tm": "11:30", "ac": "基山街逛街", "tg": "shopping", "p": "Jishan Street Jiufen"},
    {"tm": "13:00", "ac": "午餐：九份素食（芋圓等）", "tg": "food", "p": ""},
    {"tm": "15:00", "ac": "返回台北市區", "tg": "leisure", "p": ""},
    {"tm": "17:30", "ac": "抵達桃園機場，辦理登機", "tg": "flight", "p": "Taiwan Taoyuan International Airport"},
    {"tm": "21:10", "ac": "CI 0024 起飛 — 台北 TPE→安大略 ONT", "tg": "flight", "p": "Taiwan Taoyuan International Airport"}
  ]},
  {"ti": "Day 17 | 5/2 | 抵達家門", "ci": "到家", "ss": [
    {"tm": "18:00", "ac": "抵達安大略 ONT（美國時間）", "tg": "leisure", "p": "Ontario International Airport"}
  ]}
]

# Add VN 1344 flight
data['flights'].insert(2, {
    "a": "越南航空",
    "f": "VN 1344",
    "r": "胡志明市 SGN→芽莊 CXR",
    "d": "4/22 17:00 起飛 → 約18:00抵達",
    "p": "Tan Son Nhat International Airport"
})

# Sort flights by departure time
def flight_sort_key(f):
    # Extract date and time for sorting
    d = f['d']
    # e.g. "4/17 00:10→4/18 05:15" or "4/22 17:00 起飛 → 約18:00抵達"
    import re
    m = re.search(r'(\d+/\d+)\s+(\d+:\d+)', d)
    if m:
        return m.group(1) + ' ' + m.group(2)
    return d

data['flights'].sort(key=flight_sort_key)

# Read old HTML and replace DATA+VOICE
with open("/Users/foongotino/Documents/00_旅遊/越南＋台灣 旅遊攻略 2026.html") as f:
    html_old = f.read()

old_data_start = html_old.index("var DATA=")
old_voice_start = html_old.index("var VOICE=")
old_voice_len = len("var VOICE=")

new_data_str = json.dumps(data, ensure_ascii=False)
new_voice_str = json.dumps(voice, ensure_ascii=False)

new_html = (
    html_old[:old_data_start]
    + "var DATA=" + new_data_str + ";\nvar VOICE=" + new_voice_str + ";"
    + html_old[old_voice_start + old_voice_len:]
)

print(f"Days: {len(data['days'])}, Flights: {len(data['flights'])}")
print(f"New HTML size: {len(new_html)}")

with open("/Users/foongotino/Documents/00_旅遊/越南＋台灣 旅遊攻略 2026.html", "w") as f:
    f.write(new_html)

print("Done!")

# Also backup
with open("/Users/foongotino/Documents/00_旅遊/backup/旅遊攻略_2026_v2.html", "w") as f:
    f.write(new_html)
print("Backup saved!")
