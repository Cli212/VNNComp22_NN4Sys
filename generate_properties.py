import os
import sys
import csv
from haoyu_gen import main as card_main
from cheng_gen import main as index_main

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate_properties.py <random seed>")
        exit(1)
    print("Generating cardinality specifications, this may take around ten minutes...")
    if not os.path.exists('spec'):
        os.makedirs('spec')
    seed = sys.argv[1]
    csv_data = []
    csv_data.extend(index_main(seed))
    csv_data.extend(card_main(seed))
    print(f"Successfully generate {len(csv_data)} files!")
    print(f"Total timeout is {sum([int(i[-1]) for i in csv_data])}")
    with open('nn4sys.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerows(csv_data)
