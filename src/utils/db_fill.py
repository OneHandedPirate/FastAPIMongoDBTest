import asyncio

from src.database import collection


FORM_TEMPLATES = [
    {
        "name": "Registration Form",
        "user_name": "text",
        "user_email": "email",
        "user_phone": "phone",
        "created_at": "date"
    },
    {
        "name": "Order Form",
        "order_id": "text",
        "customer_email": "email",
        "customer_phone": "phone",
        "created_at": "date"
    },
    {
        "name": "Contact Form",
        "contact_name": "text",
        "contact_email": "email",
        "message": "text",
        "submitted_at": "date"
    },
    {
        "name": "Subscription Form",
        "subscriber_email": "email",
        "subscribed_at": "date"
    }
]


if __name__ == "__main__":
    async def main():
        res = await collection.insert_many(FORM_TEMPLATES)
        print(f"Form templates saved to DB: {len(res.inserted_ids)}")

    asyncio.run(main())
