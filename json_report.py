import json

def write_json_report(page_data, filename="report.json"):
    page_data_values = sorted(page_data.values(), key=lambda item: item["url"])
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(page_data_values, f, indent=2)
