tables = [
    "users", "employees", "products", "orders", "customers",
    "inventory", "sales", "payments", "suppliers", "categories",
    "departments", "transactions", "logs", "messages", "notifications",
    "reviews", "feedback", "settings", "roles", "permissions"
]
columns = [
    "id", "name", "email", "phone", "address",
    "created_at", "updated_at", "status", "role", "department",
    "price", "quantity", "total", "description", "category",
    "start_date", "end_date", "comments", "rating", "type"
]
for t in tables:
    for c in columns:
        print(F'SELECT Count(*) FROM {t} WHERE {c} IS NULL')