import asyncio

import httpx

from environ import APP_PORT

TEST_FORMS = [
    {
        "user": "OneHandedPirate",  # Invalid form
        "phone": "+7 999 999 99 99",
        "email": "example@example.com",
    },
    {
        "user_name": "Plagueis",  # Invalid form
        "user_email": "example@example.com",
        "user_phone": "+ 7 999 999 99 99",
        "created_at": "12.12.1982",
    },
    {
        "user_name": "Hello",  # Invalid form
        "user_email": "example@example.com",
    },
    {
        "subscriber_email": "example@example.com",  # Valid form, return Subscription Form name
        "subscribed_at": "12.12.1982",
        "some_additional_field": "additional data",
        "valid": "Yes"
    },
    {
        "subscriber_email": "example@example",  # Invalid email, return text type
        "subscribed_at": "1982-12-12",
    },
    {
        "contact_name": "OneHandedPirate",  # Valid form, return Contact Form name
        "contact_email": "example@example.com",
        "message": "Hello World!",
        "submitted_at": "12.12.1982",
        "valid": "Yes"
    },
    {
        "contact_name": "OneHandedPirate",
        "contact_email": "example@example.com",
        "message": "Hello World!",
        "submitted_at": "12.1982",   # Invalid date format thus the whole form
    },
    {
        "user_name": "OneHandedPirate",  # Valid form, return Registration Form name
        "user_email": "example@example.com",
        "user_phone": "+7 999 999 99 99",
        "created_at": "12.12.1982",
        "valid": "Yes"
    },
    {
        "user_name": "OneHandedPirate",
        "user_email": "example@example.com",
        "user_phone": "+7 999 999 99",  # Invalid phone format thus the whole form
        "created_at": "12.12.1982",
    },
    {
        "order_id": "4353453",      # Valid form, return Order Form name
        "customer_email": "example@google.ru",
        "customer_phone": "+7 999 435 76 42",
        "created_at": "12.12.2022",
        "valid": "Yes"
    },
    {
        "order_id": "4353453",      # Invalid form
        "customer_email": "example@",
        "customer_phone": "+ 7 999 435 76",
        "created_at": "12.12",
    },
]


async def test_get_form_endpoint(data: list) -> None:
    async with httpx.AsyncClient() as client:
        for form in data:
            print(f"Request data: {form}")
            res = await client.post(f'http://localhost:{APP_PORT}/get_form', json=form)
            _json = res.json()
            print(f"Response data: {_json}\n")
            assert bool(form.get("valid")) == bool(_json.get("template_name"))


if __name__ == "__main__":
    asyncio.run(test_get_form_endpoint(TEST_FORMS))
