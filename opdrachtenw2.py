"""Opdracht 1"""
def records(file_path):
    """Lijst maken van het geimporteerde csv bestand met de cijfers van een klas."""
    records = []
    with open(file_path, 'r') as file:
      csv_reader = csv.DictReader(file)
      for row in csv_reader:
        records.append(row)
def average(records):
    """ bereken het gemiddelde door alle recods bij elkaar op te tellen en te delen door het totaal"""
    total = sum(float(record['Grade']) for record in records)
    average = total / len(records)

    print(f"Average Grade: {average}")
    print("--------------------")
def filter(records):
    """Wanneer cijfer hoger is dan 80.0 dan print name en cijfer student"""
    filtered_records = [record for record in records if float(record['Grade']) >= 80.0]

    print("Student Report")
    print("--------------")
    for record in filtered_records:
        print(f"Name: {record['Name']}")
        print(f"Grade: {record['Grade']}")
        print("--------------------")
file_path = input("Enter the path to the CSV file: ")

