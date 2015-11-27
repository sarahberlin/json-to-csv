# json-to-csv
Scrapes JSON files of Virginia election results, converts them into CSV format, then merges CSV files into a single CSV. Run a separate script to identify winners, and create new CSV with only the winners.


VA_election_scrape.py scapes election result pages ans saves a JSON file of each locality
VA_json2csv.py converts JSON files in the same directory to CSVs
VA_merged.py merges JSON files in the same directory to a single CSV
VA_winners.py identifies winners and creates a new CSV of winners
