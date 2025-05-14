from faker import Faker

fake = Faker()

def display_fake_profile():
    """Generates and displays a fake user profile."""
    print("\n---Generating Fake Profile---\n")

    profile = {
        "Name": fake.name(),
        "Username": fake.user_name(),
        "Date of Birth": fake.date_of_birth(minimum_age=18, maximum_age=30),
        "Email": fake.email(),
        "Address": fake.address(),
        "Phone number": fake.phone_number(),
        "Job": fake.job(),
        "Website": fake.url(),
        "Company": fake.company()
    }

    for key, value in profile.items():
        print(f"{key}: {value}")

    print("\n---Fake Profile Generated Successfully---\n")



