import base64
import smartscan_registration_module as srm

encoded_data = base64.b64encode(b"John Doe,johndoe@example.com").decode('utf-8')

# Register the user using the SmartScan Code
srm.RegisterUserFromSmartScan(encoded_data)
