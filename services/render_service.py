class RenderService:
    @staticmethod
    def build_item_tree_row(item, dim_formatter, weight_formatter, number_formatter):
        display_w = number_formatter(dim_formatter(item["WHD"][0]))
        display_h = number_formatter(dim_formatter(item["WHD"][1]))
        display_d = number_formatter(dim_formatter(item["WHD"][2]))
        display_weight = number_formatter(weight_formatter(item["weight"]))

        return (
            item["name"],
            f"{display_w} x {display_h} x {display_d}",
            display_weight,
            "AUTO" if item.get("fill_to_max", False) else item["qty"],
            item["color"],
            item["updown"],
        )