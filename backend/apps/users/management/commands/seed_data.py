from datetime import date

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.books.models import Author, Book, Category
from apps.inventory.models import Floor, LibraryBranch, Rack, Shelf
from apps.subscriptions.models import SubscriptionPlan


class Command(BaseCommand):
    help = "Seed initial application data"

    def handle(self, *args, **kwargs):
        User = get_user_model()

        self.stdout.write("Creating users...")

        # Admin User
        admin_user, created = User.objects.get_or_create(
            username="admin",
            defaults={
                "email": "admin@smartlibrary.com",
                "is_staff": True,
                "is_superuser": True,
            },
        )

        if created:
            admin_user.set_password("Admin@123")
            admin_user.save()

        # Test User
        test_user, created = User.objects.get_or_create(
            username="gaurav",
            defaults={
                "email": "test@test.com",
                "phone_number": "9999999999",
            },
        )

        if created:
            test_user.set_password("StrongPass123")
            test_user.save()

        self.stdout.write("Creating categories...")

        categories = [
            "Python",
            "Django",
            "Programming",
            "DevOps",
            "Database",
            "History",
            "Science",
            "Business",
            "Self Help",
        ]

        category_map = {}

        for category_name in categories:
            category, _ = Category.objects.get_or_create(name=category_name)
            category_map[category_name] = category

        self.stdout.write("Creating authors...")

        authors = [
            {
                "name": "Eric Matthes",
                "bio": "Author of Python Crash Course",
            },
            {
                "name": "Mark Lutz",
                "bio": "Python expert and trainer",
            },
            {
                "name": "Robert Martin",
                "bio": "Clean Code author",
            },
            {
                "name": "Martin Fowler",
                "bio": "Software architecture expert",
            },
            {
                "name": "James Clear",
                "bio": "Author of Atomic Habits",
            },
        ]

        author_map = {}

        for author_data in authors:
            author, _ = Author.objects.get_or_create(
                name=author_data["name"], defaults={"bio": author_data["bio"]}
            )
            author_map[author_data["name"]] = author

        self.stdout.write("Creating books...")

        books = [
            {
                "title": "Python Crash Course",
                "isbn_13": "9781593279288",
                "author": "Eric Matthes",
                "category": "Python",
                "price": 799.00,
                "publication_date": date(2023, 1, 1),
            },
            {
                "title": "Learning Python",
                "isbn_13": "9781449355739",
                "author": "Mark Lutz",
                "category": "Python",
                "price": 999.00,
                "publication_date": date(2022, 5, 10),
            },
            {
                "title": "Clean Code",
                "isbn_13": "9780132350884",
                "author": "Robert Martin",
                "category": "Programming",
                "price": 899.00,
                "publication_date": date(2021, 8, 15),
            },
            {
                "title": "Refactoring",
                "isbn_13": "9780201485677",
                "author": "Martin Fowler",
                "category": "Programming",
                "price": 1099.00,
                "publication_date": date(2020, 3, 20),
            },
            {
                "title": "Atomic Habits",
                "isbn_13": "9780735211292",
                "author": "James Clear",
                "category": "Self Help",
                "price": 599.00,
                "publication_date": date(2019, 10, 1),
            },
        ]

        for book_data in books:
            Book.objects.get_or_create(
                isbn_13=book_data["isbn_13"],
                defaults={
                    "title": book_data["title"],
                    "author": author_map[book_data["author"]],
                    "category": category_map[book_data["category"]],
                    "price": book_data["price"],
                    "publication_date": book_data["publication_date"],
                    "description": f"{book_data['title']} sample book",
                },
            )

        self.stdout.write(self.style.SUCCESS("Creating library branches..."))

        branches = [
            {
                "name": "Pune Central Library",
                "code": "PUN001",
                "address": "Wakad, Pune",
                "city": "Pune",
                "state": "Maharashtra",
                "postal_code": "411057",
                "phone": "9876543210",
                "email": "pune@smartlibrary.com",
            },
            {
                "name": "Mumbai Central Library",
                "code": "MUM001",
                "address": "Andheri East, Mumbai",
                "city": "Mumbai",
                "state": "Maharashtra",
                "postal_code": "400069",
                "phone": "9876543211",
                "email": "mumbai@smartlibrary.com",
            },
            {
                "name": "Nashik Central Library",
                "code": "NAS001",
                "address": "College Road, Nashik",
                "city": "Nashik",
                "state": "Maharashtra",
                "postal_code": "422005",
                "phone": "9876543212",
                "email": "nashik@smartlibrary.com",
            },
        ]

        for branch in branches:
            LibraryBranch.objects.get_or_create(
                code=branch["code"],
                defaults=branch,
            )

        self.stdout.write(self.style.SUCCESS("Library branches created successfully."))

        self.stdout.write(self.style.SUCCESS("Creating library floors..."))

        floors = [
            {
                "branch_code": "PUN001",
                "name": "Ground Floor",
                "code": "GF",
            },
            {
                "branch_code": "PUN001",
                "name": "First Floor",
                "code": "FF",
            },
            {
                "branch_code": "MUM001",
                "name": "Ground Floor",
                "code": "GF",
            },
        ]

        for floor in floors:
            branch = LibraryBranch.objects.get(code=floor["branch_code"])

            Floor.objects.get_or_create(
                branch=branch,
                code=floor["code"],
                defaults={
                    "name": floor["name"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Creating racks..."))

        racks = [
            {
                "branch": "PUN001",
                "name": "Programming Rack",
                "code": "RACK-A",
            },
            {
                "branch": "PUN001",
                "name": "Technology Rack",
                "code": "RACK-B",
            },
            {
                "branch": "MUM001",
                "name": "Programming Rack",
                "code": "RACK-A",
            },
        ]

        for rack in racks:
            branch = LibraryBranch.objects.get(code=rack["branch"])

            Rack.objects.get_or_create(
                branch=branch,
                code=rack["code"],
                defaults={
                    "name": rack["name"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Racks created successfully."))
        self.stdout.write(self.style.SUCCESS("Creating shelves..."))

        shelves = [
            {
                "branch": "PUN001",
                "rack": "RACK-A",
                "name": "Shelf A1",
                "code": "A1",
                "capacity": 100,
            },
            {
                "branch": "PUN001",
                "rack": "RACK-A",
                "name": "Shelf A2",
                "code": "A2",
                "capacity": 100,
            },
            {
                "branch": "PUN001",
                "rack": "RACK-B",
                "name": "Shelf B1",
                "code": "B1",
                "capacity": 100,
            },
            {
                "branch": "MUM001",
                "rack": "RACK-A",
                "name": "Shelf A1",
                "code": "A1",
                "capacity": 100,
            },
        ]

        for shelf in shelves:
            branch = LibraryBranch.objects.get(code=shelf["branch"])

            rack = Rack.objects.get(
                branch=branch,
                code=shelf["rack"],
            )

            Shelf.objects.get_or_create(
                rack=rack,
                code=shelf["code"],
                defaults={
                    "name": shelf["name"],
                    "capacity": shelf["capacity"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Shelves created successfully."))
        subscription_plans = [
            {
                "name": "Basic",
                "monthly_fee": 350,
                "deposit_amount": 1000,
                "max_active_books": 1,
                "duration_days": 30,
            },
            {
                "name": "Standard",
                "monthly_fee": 450,
                "deposit_amount": 1000,
                "max_active_books": 2,
                "duration_days": 30,
            },
            {
                "name": "Premium",
                "monthly_fee": 600,
                "deposit_amount": 1000,
                "max_active_books": 3,
                "duration_days": 30,
            },
        ]
        self.stdout.write("Creating subscription plans...")

        for plan in subscription_plans:
            SubscriptionPlan.objects.get_or_create(
                name=plan["name"],
                defaults={
                    "monthly_fee": plan["monthly_fee"],
                    "deposit_amount": plan["deposit_amount"],
                    "max_active_books": plan["max_active_books"],
                    "duration_days": plan["duration_days"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Subscription plans created"))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))
