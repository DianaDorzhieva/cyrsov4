import json
from utils import filter_and_sorted, get_date, mask_account_num, mask_card_num, final_mask

with open("operations.json", "r", encoding="utf-8") as file:
    all_information = json.load(file)

for i in range(5):
    inform_filter = filter_and_sorted(all_information)[i]
    print(get_date(inform_filter["date"]), inform_filter["description"])
    if "from" in inform_filter:
        print(f"""{final_mask(inform_filter["from"])} -> {mask_account_num(inform_filter["to"])}""")
    else:
        print(f"""Перевод на {mask_account_num(inform_filter["to"])} """)
    print(inform_filter["operationAmount"]["amount"], inform_filter["operationAmount"]["currency"]["name"])
    print("-------")