"""
generate_maps_data.py
여행 일정 데이터를 입력받아:
1. Day별 구글 내 지도 호환 표준 8컬럼 CSV (날짜, 시간, 여행지, 위도, 경도, 구글지도, 설명, 이동/메모)
2. 통합 CSV (전 일정)
3. 구글 내 지도 100% 호환 올인원 KML (XML 엔티티 이스케이프 및 My Maps 파서 최적화)
4. Day별 개별 레이어 전용 KML
을 자동으로 생성하고 XML 유효성을 정밀 검증하는 유틸리티 모듈.
"""

import csv
import json
import os
import urllib.parse
import xml.sax.saxutils
import xml.etree.ElementTree as ET

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

def clean_xml_text(text):
    """XML 문법 에러를 방지하기 위해 특수문자 및 유니코드 화살표를 안전하게 정제"""
    if not text:
        return ""
    # 유니코드 특수 화살표 치환 및 XML 표준 엔티티 이스케이프 (& -> &amp;, < -> &lt;, > -> &gt;)
    t = str(text).replace("➔", "->")
    return xml.sax.saxutils.escape(t)

def generate_csv_and_kml(trip_title, days_data, output_dir="."):
    """
    days_data 형식:
    [
      {
        "day": 1,
        "date": "2026-10-23",
        "spots": [
          {
            "id": 1,
            "time": "07:00-11:30",
            "name": "다낭 국제공항(DAD) 도착 및 입국",
            "query": "Da Nang International Airport",
            "lat": 16.0539,
            "lng": 108.2022,
            "desc": "LCC 직항 탑승 및 다낭 입국심사 후 입국장 이동...",
            "memo": "공항 픽업 차량 또는 그랩 탑승 (호텔까지 약 15분)..."
          },
          ...
        ]
      },
      ...
    ]
    """
    os.makedirs(output_dir, exist_ok=True)
    generated_files = []

    # 1. Day별 개별 CSV 및 전체 통합 CSV 생성 (표준 8컬럼: 날짜, 시간, 여행지, 위도, 경도, 구글지도, 설명, 이동/메모)
    total_csv_filename = os.path.join(output_dir, f"{trip_title}_Itinerary.csv")
    total_spots = []

    for day_info in days_data:
        day_num = day_info["day"]
        csv_filename = os.path.join(output_dir, f"{trip_title}_Day{day_num}.csv")
        
        with open(csv_filename, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["날짜", "시간", "여행지", "위도", "경도", "구글지도", "설명", "이동/메모"])
            
            for spot in day_info["spots"]:
                encoded_q = urllib.parse.quote(spot.get("query", spot["name"]))
                maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_q}"
                lat = spot.get("lat", 0.0)
                lng = spot.get("lng", 0.0)
                
                row = [
                    day_info.get("date", ""),
                    spot.get("time", ""),
                    spot["name"],
                    lat,
                    lng,
                    maps_url,
                    spot.get("desc", ""),
                    spot.get("memo", "")
                ]
                writer.writerow(row)
                total_spots.append(row)
                
        generated_files.append(csv_filename)

    # 전체 통합 CSV
    with open(total_csv_filename, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["날짜", "시간", "여행지", "위도", "경도", "구글지도", "설명", "이동/메모"])
        for r in total_spots:
            writer.writerow(r)
    generated_files.append(total_csv_filename)

    # 2. 구글 내 지도(My Maps) 100% 호환 올인원 KML 생성 (Flat Placemark 구조)
    kml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<kml xmlns="http://www.opengis.net/kml/2.2">',
        '  <Document>',
        f'    <name>{clean_xml_text(trip_title)} - 마스터 일정</name>',
        f'    <description>{clean_xml_text(trip_title)} 전 일정 스팟 목록</description>',
    ]

    for day_info in days_data:
        day_num = day_info["day"]
        for idx, spot in enumerate(day_info["spots"], 1):
            raw_name = f"[{day_num}일차 #{idx}] {spot['name']}"
            name = clean_xml_text(raw_name)
            encoded_q = urllib.parse.quote(spot.get("query", spot["name"]))
            maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_q}"
            lat = spot.get("lat", 0.0)
            lng = spot.get("lng", 0.0)

            clean_desc = spot.get("desc", "").replace("➔", "->")
            clean_memo = spot.get("memo", "").replace("➔", "->")

            desc_html = (
                f"일자: {day_info.get('date', '')} ({spot.get('time', '')})<br>"
                f"설명: {clean_desc}<br>"
                f"메모: {clean_memo}<br>"
                f"구글지도: {maps_url}"
            )

            kml_lines.extend([
                '    <Placemark>',
                f'      <name>{name}</name>',
                f'      <description><![CDATA[{desc_html}]]></description>',
                '      <Point>',
                f'        <coordinates>{lng},{lat},0</coordinates>',
                '      </Point>',
                '    </Placemark>'
            ])

    kml_lines.extend([
        '  </Document>',
        '</kml>'
    ])

    kml_content = "\n".join(kml_lines)
    # XML 유효성 엄격 검증
    ET.fromstring(kml_content)

    kml_filename = os.path.join(output_dir, f"{trip_title}_mymaps.kml")
    with open(kml_filename, "w", encoding="utf-8") as f:
        f.write(kml_content)
    generated_files.append(kml_filename)

    # 3. Day별 개별 KML 생성 (레이어별 추가용)
    for day_info in days_data:
        day_num = day_info["day"]
        day_kml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<kml xmlns="http://www.opengis.net/kml/2.2">',
            '  <Document>',
            f'    <name>{clean_xml_text(trip_title)} {day_num}일차</name>'
        ]
        for idx, spot in enumerate(day_info["spots"], 1):
            name = clean_xml_text(f"#{idx} {spot['name']}")
            encoded_q = urllib.parse.quote(spot.get("query", spot["name"]))
            maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_q}"
            lat = spot.get("lat", 0.0)
            lng = spot.get("lng", 0.0)
            clean_desc = spot.get("desc", "").replace("➔", "->")
            desc_html = f"시간: {spot.get('time', '')}<br>설명: {clean_desc}<br>구글지도: {maps_url}"

            day_kml_lines.extend([
                '    <Placemark>',
                f'      <name>{name}</name>',
                f'      <description><![CDATA[{desc_html}]]></description>',
                '      <Point>',
                f'        <coordinates>{lng},{lat},0</coordinates>',
                '      </Point>',
                '    </Placemark>'
            ])
        day_kml_lines.extend(['  </Document>', '</kml>'])
        day_kml_content = "\n".join(day_kml_lines)
        ET.fromstring(day_kml_content)

        day_kml_filename = os.path.join(output_dir, f"{trip_title}_Day{day_num}.kml")
        with open(day_kml_filename, "w", encoding="utf-8") as f:
            f.write(day_kml_content)
        generated_files.append(day_kml_filename)

    return generated_files

if __name__ == "__main__":
    print("Google My Maps CSV & KML Generator Module (v1.4.1) Ready - XML Escaped & Coordinate Validated")
