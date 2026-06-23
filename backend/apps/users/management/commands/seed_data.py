from datetime import date

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from apps.books.models import Author, Book, Category
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
                "isbn": "9781593279288",
                "author": "Eric Matthes",
                "category": "Python",
                "price": 799.00,
                "publication_date": date(2023, 1, 1),
            },
            {
                "title": "Learning Python",
                "isbn": "9781449355739",
                "author": "Mark Lutz",
                "category": "Python",
                "price": 999.00,
                "publication_date": date(2022, 5, 10),
            },
            {
                "title": "Clean Code",
                "isbn": "9780132350884",
                "author": "Robert Martin",
                "category": "Programming",
                "price": 899.00,
                "publication_date": date(2021, 8, 15),
            },
            {
                "title": "Refactoring",
                "isbn": "9780201485677",
                "author": "Martin Fowler",
                "category": "Programming",
                "price": 1099.00,
                "publication_date": date(2020, 3, 20),
            },
            {
                "title": "Atomic Habits",
                "isbn": "9780735211292",
                "author": "James Clear",
                "category": "Self Help",
                "price": 599.00,
                "publication_date": date(2019, 10, 1),
            },
        ]

        for book_data in books:
            Book.objects.get_or_create(
                isbn=book_data["isbn"],
                defaults={
                    "title": book_data["title"],
                    "author": author_map[book_data["author"]],
                    "category": category_map[book_data["category"]],
                    "price": book_data["price"],
                    "publication_date": book_data["publication_date"],
                    "description": f"{book_data['title']} sample book",
                },
            )

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
