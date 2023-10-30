
import {
  to = module.network.azurerm_network_security_rule.nsg_rule["app-nsg_NGINX"]
  id = "/subscriptions/12345/resourceGroups/rg-01/providers/Microsoft.Network/networkSecurityGroups/app-nsg/securityRules/NGINX"
}

import {
  to = module.network.azurerm_network_security_rule.nsg_rule["app-nsg_app-inbound"]
  id = "/subscriptions/12345/resourceGroups/rg-01/providers/Microsoft.Network/networkSecurityGroups/app-nsg/securityRules/app-inbound"
}

import {
  to = module.network.azurerm_network_security_rule.nsg_rule["app-nsg_app-outbound"]
  id = "/subscriptions/12345/resourceGroups/rg-01/providers/Microsoft.Network/networkSecurityGroups/app-nsg/securityRules/app-outbound"
}
