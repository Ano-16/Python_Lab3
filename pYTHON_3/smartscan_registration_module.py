import base64

# In-memory storage
users = []

# Lambda functions
create_user_record = lambda name, email: {"name": name, "email": email}
insert_user_record = lambda user: users.append(user)
fetch_all_users = lambda: users

# Function to decode SmartScan Code
def decode_smartscan_code(encoded_data):
    # Decode the base64 encoded string
    decoded_bytes = base64.b64decode(encoded_data)
    decoded_string = decoded_bytes.decode('utf-8')
    # Split the string to extract user data
    name, email = decoded_string.split(',')
    return name, email

# Function to register user from SmartScan Code
def RegisterUserFromSmartScan(encoded_data):
    # Decode the SmartScan Code to extract user data
    name, email = decode_smartscan_code(encoded_data)
    
    # Create and insert the user record using lambda functions
    user = create_user_record(name, email)
    insert_user_record(user)
    
    # Fetch and print all users
    all_users = fetch_all_users()
    print(all_users)



