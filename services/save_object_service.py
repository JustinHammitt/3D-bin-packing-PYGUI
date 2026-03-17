import json


class SaveObjectService:
    @staticmethod
    def save_json_file(file_path, data):
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def load_json_file(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def build_box_data(bin_name, bin_w, bin_h, bin_d, bin_weight, bin_corner, items):
        return {
            "bin": {
                "name": bin_name,
                "WHD": [bin_w, bin_h, bin_d],
                "max_weight": bin_weight,
                "corner": bin_corner,
            },
            "items": [
                {
                    "name": item["name"],
                    "WHD": list(item["WHD"]),
                    "weight": item["weight"],
                    "qty": item["qty"],
                    "color": item["color"],
                    "updown": item["updown"],
                    "fill_to_max": item.get("fill_to_max", False),
                }
                for item in items
            ],
        }

    @staticmethod
    def build_item_data(name, w, h, d, weight, qty, color, updown, fill_to_max):
        return {
            "name": name,
            "WHD": [w, h, d],
            "weight": weight,
            "qty": qty,
            "color": color,
            "updown": updown,
            "fill_to_max": fill_to_max,
        }

    @staticmethod
    def normalize_loaded_item(item_data):
        whd = item_data.get("WHD", [0, 0, 0])

        return {
            "name": str(item_data.get("name", "")).strip(),
            "WHD": (
                float(whd[0]),
                float(whd[1]),
                float(whd[2]),
            ),
            "weight": float(item_data.get("weight", 1)),
            "qty": int(item_data.get("qty", 1)),
            "color": str(item_data.get("color", "#4F81BD")),
            "updown": bool(item_data.get("updown", True)),
            "fill_to_max": bool(item_data.get("fill_to_max", False)),
        }

    @staticmethod
    def extract_box_parts(data):
        bin_data = data.get("bin", {})
        items_data = data.get("items", [])
        whd = bin_data.get("WHD", [100, 100, 100])

        return {
            "bin_name": str(bin_data.get("name", "MainBin")),
            "bin_whd": whd,
            "bin_weight": bin_data.get("max_weight", 1000),
            "bin_corner": bin_data.get("corner", 0),
            "items": items_data,
        }