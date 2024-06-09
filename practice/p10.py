import psycopg2

# Database connection parameters
host = "localhost"
port = "5432"
dbname = "Paystack_Team"
user = "postgres"
password = "cos101"

try:
    # Connect to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )
    connection.autocommit = True  # Enable autocommit mode

    # Create a cursor object
    cursor = connection.cursor()

    # Function to fetch team members in the Revenue Division
    def get_revenue_team_members():
        cursor.execute('''
        SELECT * FROM Paystack_Team WHERE division = 'Revenue'
        ''')
        return cursor.fetchall()

    # Function to fetch team members in Growth and Product Division whose age is between 30 and 35
    def get_growth_product_members_age_30_to_35():
        cursor.execute('''
        SELECT * Paystack_Team 
        WHERE division = 'Growth' OR division = 'Product'
        AND age > 30 AND age < 35
        ''')
        return cursor.fetchall()

    # Function to fetch team members in Modules 1, 3, and 5
    def get_members_in_modules_1_3_5():
        cursor.execute('''
    SELECT * FROM Paystack_Team WHERE module IN (1, 3, 5)
    ''')
        return cursor.fetchall()

    # Function to fetch team members in Modules 4 and Product Division
    def get_members_in_module_4_and_product():
        cursor.execute('''
        SELECT * FROM Paystack_Team WHERE module = 4 OR division = 'Product'
        ''')
        return cursor.fetchall()

    # Fetch and print the results for each query
    print("Paystack Team in Revenue Division:")
    for member in get_revenue_team_members():
        print(member)

    print("\nPaystack Team in Growth and Product Division whose age is greater than 30 years but less than 35 years:")
    for member in get_growth_product_members_age_30_to_35():
        print(member)

    print("\nPaystack Team in Modules 1, 3 and 5:")
    for member in get_members_in_modules_1_3_5():
        print(member)

    print("\nPaystack Team in Modules 4 and Product Division:")
    for member in get_members_in_module_4_and_product():
        print(member)


    # Close the cursor and connection
    cursor.close()
    connection.close()
    

except Exception as error:
    print(f"Error inserting data: {error}")