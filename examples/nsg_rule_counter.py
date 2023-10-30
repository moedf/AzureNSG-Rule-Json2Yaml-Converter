import json

def extract_nsg_rules(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Dynamically find the key for the NSG name
    for key in data['parameters']:
        if key.startswith("networkSecurityGroups_") and key.endswith("_name"):
            nsg_name_key = key
            break
    else:
        print("NSG name key not found.")
        return

    nsg_name = data['parameters'][nsg_name_key]['defaultValue']
    print(f"NSG Name: {nsg_name}")

    inbound_rules = set()
    outbound_rules = set()

    resources = data['resources']

    for resource in resources:
        if "securityRules" in resource['properties']:
            for rule in resource['properties']['securityRules']:
                if rule['properties']['direction'] == "Inbound":
                    inbound_rules.add(rule['name'])
                elif rule['properties']['direction'] == "Outbound":
                    outbound_rules.add(rule['name'])

    print(f"Number of Inbound rules: {len(inbound_rules)}")
    for rule in inbound_rules:
        # print(f"  - Rule Name: {rule}")
       print(f"   {rule}")

    print(f"\nNumber of Outbound rules: {len(outbound_rules)}")
    for rule in outbound_rules:
        # print(f"  - Rule Name: {rule}")
        print(f"   {rule}")

# Path to your JSON file
json_file_path = "input.json"
extract_nsg_rules(json_file_path)
