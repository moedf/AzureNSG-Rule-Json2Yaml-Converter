import csv

def generate_import_block(nsg_name, rule_name, resource_group, subscription_id):
    return f"""
import {{
  to = module.network.azurerm_network_security_rule.nsg_rule["{nsg_name}_{rule_name}"]
  id = "/subscriptions/{subscription_id}/resourceGroups/{resource_group}/providers/Microsoft.Network/networkSecurityGroups/{nsg_name}/securityRules/{rule_name}"
}}
"""

input_file_path = "rules_input.csv"  # update this to the path of your CSV file

with open('imports.tf', 'w') as output_file:
    with open(input_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Using strip() to remove any leading/trailing whitespaces from the keys/values
                import_block = generate_import_block(row['NSG_Name'].strip(), row['Rule_Name'].strip(), row['Resource_Group'].strip(), row['Subscription_ID'].strip())
                output_file.write(import_block)
            except KeyError as e:
                print(f"A key error occurred: {e} - Available keys: {', '.join(row.keys())}")

print("Import blocks have been written to imports.tf")
