# NSG-Converter

This repository contains scripts that facilitate the conversion and management of NSG (Network Security Group) rules for Azure. These scripts are particularly useful when working with NSG rules in Terraform. The tools in this repository allow you to count NSG rules, convert them from JSON to YAML format, and create terraform import blocks.

## Prerequisites
- **Python:** These scripts are written in Python. Ensure that Python is installed in your environment.
- **PyYAML:** This is a Python module necessary to run the scripts. You can install it using the following command:
  ```bash
  pip install PyYAML

## Files and Usage

```plaintext
AzureNSG-Rule-Json2Yaml-Converter/
│
├── nsg_json_to_yaml_converter.py      # Script for JSON to YAML conversion
├── nsg_rule_counter.py                # Script to count NSG rules
├── nsg_rule_import_block_creator.py   # Script to create terraform import blocks
│
├── input.json                         # Input: NSG rules in JSON format
├── rules_input.csv                    # Input: Data for import blocks
│
├── output.yml                         # Output: Converted NSG rules in YAML
├── imports.tf                         # Output: Generated terraform import blocks
│
├── README.md


input.json
This file is required and can be downloaded from the Azure portal or CLI. It should contain the entire NSG template in JSON format.

nsg_rule_counter.py
Outputs the number of NSG rules and their names.

nsg_json_to_yaml_converter.py
Converts the JSON file to YAML format, which can be used in the terraform NSG resource block.

rules_input.csv
To create the import blocks, you need to populate the data in this CSV file. It requires NSG_Name, Rule_Name, Resource_Group, and Subscription_ID.

nsg_rule_import_block_creator.py
Creates terraform import blocks for the NSG rules.
