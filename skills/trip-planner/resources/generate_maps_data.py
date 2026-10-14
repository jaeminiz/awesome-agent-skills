"""
generate_maps_data.py
여행 일정 데이터를 입력받아:
1. Day별 구글 내 지도 호환 표준 6컬럼 CSV (day1_itinerary.csv, day2_itinerary.csv ...)
2. 올인원 구글 내 지도 KML 파일 (일자별 레이어 폴더, 번호 마커, 동선 연결선 LineString 포함)
을 자동으로 생성하는 유틸리티 스크립트.
"""

import csv
import json
import os
import urllib.parse

# 일자별 이동 경로 선 테마 색상 (KML aabbggrr 포맷)
ROUTE_COLORS = [
    "ff147efa",  # 1일차: 주황 (Orange)
    "ffff8833",  # 2일차: 파랑 (Blue)
    "ff44c022",  # 3일차: 초록 (Green)
    "ffa033aa",  # 4일차: 보라 (Purple)
    "ff3399ff",  # 5일차: 골드/옐로우 (Yellow)
    "ff3333ea",  # 6일차: 레드 (Red)
    "ff999900",  # 7일차: 청록 (Teal)
]

def generate_csv_and_kml(trip_title, days_data, output_dir="."):
    """
    days_data 형식:
    [
      {
        "day": 1,
        "date": "2026-10-23",
        "spots": [
          {
            "time": "09:00-09:30",
            "name": "후쿠오카공항 국제선 도착",
            "query": "Fukuoka Airport International Terminal",
            "lat": 33.5859,
            "lng": 130.4447,
            "desc": "도착 후 캐리어 배송 접수...",
            "memo": "국제선 1층 2번 승차장 라라포트행 직행버스 탑승..."
          },
          ...
        ]
      },
      ...
    ]
    """
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []

    # 1. Day별 CSV 파일 생성 (표준 6컬럼: 날짜,시간,여행지,구글지도,설명,이동/메모)
    for day_info in days_data:
        day_num = day_info["day"]
        csv_filename = os.path.join(output_dir, f"day{day_num}_itinerary.csv")
        
        with open(csv_filename, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["날짜", "시간", "여행지", "구글지도", "설명", "이동/메모"])
            
            for spot in day_info["spots"]:
                encoded_q = urllib.parse.quote(spot.get("query", spot["name"]))
                maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_q}"
                writer.writerow([
                    day_info.get("date", ""),
                    spot.get("time", ""),
                    spot["name"],
                    maps_url,
                    spot.get("desc", ""),
                    spot.get("memo", "")
                ])
        generated_files.append(csv_filename)

    # 2. 올인원 KML 파일 생성
    kml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<kml xmlns="http://www.opengis.net/kml/2.2">',
        '  <Document>',
        f'    <name>{trip_title} - 구글 내 지도 (My Maps)</name>',
        f'    <description>{trip_title} 일정: 일자별 레이어, 번호 마커 및 이동 동선</description>',
    ]

    # 스타일 정의
    for i, color in enumerate(ROUTE_COLORS):
        day_idx = i + 1
        kml_lines.extend([
            f'    <Style id="route-day-{day_idx}">',
            '      <LineStyle>',
            f'        <color>{color}</color>',
            '        <width>4</width>',
            '      </LineStyle>',
            '    </Style>'
        ])

    # 각 Day별 Folder (구글 내 지도의 레이어가 됨)
    for i, day_info in enumerate(days_data):
        day_num = day_info["day"]
        color_idx = (day_num - 1) % len(ROUTE_COLORS)
        
        kml_lines.append(f'    <Folder>')
        kml_lines.append(f'      <name>{day_num}일차</name>')

        coords_for_line = []

        # 각 스팟 Placemark
        for idx, spot in enumerate(day_info["spots"], 1):
            name = f"{idx}. {spot['name']}"
            encoded_q = urllib.parse.quote(spot.get("query", spot["name"]))
            maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_q}"
            
            lat = spot.get("lat", 0.0)
            lng = spot.get("lng", 0.0)
            
            if lat != 0.0 and lng != 0.0:
                coords_for_line.append(f"{lng},{lat},0")

            desc_html = (
                f"<b>일자:</b> {day_info.get('date', '')}<br>"
                f"<b>시간:</b> {spot.get('time', '')}<br>"
                f"<b>설명:</b> {spot.get('desc', '')}<br>"
                f"<b>이동/메모:</b> {spot.get('memo', '')}<br>"
                f'<a href="{maps_url}">구글 지도에서 위치 보기</a>'
            )

            kml_lines.extend([
                '      <Placemark>',
                f'        <name>{name}</name>',
                f'        <description><![CDATA[{desc_html}]]></description>',
                '        <Point>',
                f'          <coordinates>{lng},{lat},0</coordinates>',
                '        </Point>',
                '      </Placemark>'
            ])

        # N일차 이동 경로 선 (LineString)
        if len(coords_for_line) >= 2:
            coords_str = " ".join(coords_for_line)
            kml_lines.extend([
                '      <Placemark>',
                f'        <name>{day_num}일차 이동 경로</name>',
                f'        <styleUrl>#route-day-{day_num}</styleUrl>',
                '        <LineString>',
                '          <tessellate>1</tessellate>',
                f'          <coordinates>{coords_str}</coordinates>',
                '        </LineString>',
                '      </Placemark>'
            ])

        kml_lines.append('    </Folder>')

    kml_lines.extend([
        '  </Document>',
        '</kml>'
    ])

    kml_filename = os.path.join(output_dir, f"{trip_title}_mymaps.kml")
    with open(kml_filename, "w", encoding="utf-8") as f:
        f.write("\n".join(kml_lines))
    generated_files.append(kml_filename)

    return generated_files

if __name__ == "__main__":
    import sys
    print("Google My Maps CSV & KML Generator Module Ready")
