class ObjectBuilderService:
    @staticmethod
    def build_item(
        name,
        width,
        height,
        depth,
        weight,
        qty,
        color,
        updown,
        fill_to_max=False,
    ):
        return {
            "name": name.strip(),
            "WHD": (width, height, depth),
            "weight": weight,
            "qty": qty,
            "color": color.strip() or "#4F81BD",
            "updown": updown,
            "fill_to_max": fill_to_max,
        }

    @staticmethod
    def validate_item(item):
        if not item["name"]:
            raise ValueError("Item name is required.")
        return item

    @staticmethod
    def build_sample_items():
        return [
            {
                "name": "BoxA",
                "WHD": (20, 20, 20),
                "weight": 5,
                "qty": 3,
                "color": "#FF6666",
                "updown": True,
                "fill_to_max": False,
            },
            {
                "name": "BoxB",
                "WHD": (30, 20, 10),
                "weight": 4,
                "qty": 2,
                "color": "#66CC66",
                "updown": True,
                "fill_to_max": False,
            },
            {
                "name": "TallItem",
                "WHD": (15, 40, 15),
                "weight": 6,
                "qty": 1,
                "color": "#6699FF",
                "updown": False,
                "fill_to_max": False,
            },
        ]