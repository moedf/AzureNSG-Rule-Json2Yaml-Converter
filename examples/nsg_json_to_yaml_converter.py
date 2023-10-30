import json

def wrap_asterisk(value):
    return f'"{value}"' if value == "*" else value

def format_protocol(protocol):
    protocol_mapping = {
        "ICMP": "Icmp",
        "TCP": "Tcp",
        "UDP": "Udp",
        "icmp": "Icmp",
        "tcp": "Tcp",
        "udp": "Udp"
    }
    return protocol_mapping.get(protocol, protocol)

def custom_yaml_representation(data):
    yaml_output = ""
    
    # Dynamically identifying the NSG name key
    for key in data['parameters']:
        if key.lower().startswith("networksecuritygroups_") and key.lower().endswith("_name"):
            nsg_name_key = key
            break
    else:
        print("NSG name key not found.")
        return
    
    nsg_name = data['parameters'][nsg_name_key]['defaultValue']
    yaml_output += f"{nsg_name}:\n  rules:\n"
    
    for rule in data.get('resources', [])[0].get('properties', {}).get('securityRules', []):
        properties = rule.get('properties', {})
        yaml_output += f"    {rule.get('name', '')}:\n"
        
        description = properties.get('description')
        if description:
            yaml_output += f"      description: {description}\n"
        
        # Function to handle single and multiple values
        def handle_values(field_json, field_yaml):
            values = properties.get(field_json)
            if values:
                if isinstance(values, list):
                    yaml_output_nonlocal = f"      {field_yaml}:\n"
                    for value in values:
                        yaml_output_nonlocal += f"        - {wrap_asterisk(value)}\n"
                else:
                    yaml_output_nonlocal = f"      {field_yaml}: {wrap_asterisk(values)}\n"
                return yaml_output_nonlocal
            return ""
        
        yaml_output += handle_values('sourcePortRange', 'source_port_range')
        yaml_output += handle_values('sourcePortRanges', 'source_port_ranges')
        yaml_output += handle_values('destinationPortRange', 'destination_port_range')
        yaml_output += handle_values('destinationPortRanges', 'destination_port_ranges')
        yaml_output += handle_values('sourceAddressPrefix', 'source_address_prefix')
        yaml_output += handle_values('sourceAddressPrefixes', 'source_address_prefixes')
        yaml_output += handle_values('destinationAddressPrefixes', 'destination_address_prefixes')
        yaml_output += handle_values('destinationAddressPrefix', 'destination_address_prefix')
        yaml_output += f"      access: {wrap_asterisk(properties.get('access', ''))}\n"
        yaml_output += f"      direction: {wrap_asterisk(properties.get('direction', ''))}\n"
        yaml_output += f"      priority: {properties.get('priority', '')}\n"
        yaml_output += f"      protocol: {wrap_asterisk(format_protocol(properties.get('protocol', '')))}\n"
        
    return yaml_output

# Load JSON data from a file
with open('input.json', 'r') as file:
    json_data = json.load(file)

# Get the custom YAML representation
yaml_result = custom_yaml_representation(json_data)

# Output the YAML result
if yaml_result:
    print(yaml_result)

    # Save the YAML result to a file
    with open('output.yml', 'w') as file:
        file.write(yaml_result)
