
# AI-Powered Product Recommendation System
# MCA Generative AI Lab - Q.2

products = [
    {"name": "HP Laptop", "category": "Laptop", "price": 45000,
     "description": "programming coding students"},
    {"name": "Dell Laptop", "category": "Laptop", "price": 55000,
     "description": "gaming programming performance"},
    {"name": "Lenovo Laptop", "category": "Laptop", "price": 38000,
     "description": "students study coding"},
    {"name": "Samsung Mobile", "category": "Mobile", "price": 20000,
     "description": "photography daily use"},
    {"name": "Redmi Mobile", "category": "Mobile", "price": 12000,
     "description": "students budget daily use"},
    {"name": "iPhone", "category": "Mobile", "price": 65000,
     "description": "photography video premium"},
    {"name": "Boat Headphones", "category": "Audio", "price": 1800,
     "description": "music online classes"},
    {"name": "Sony Headphones", "category": "Audio", "price": 6000,
     "description": "music gaming"},
    {"name": "USB Drive", "category": "Storage", "price": 600,
     "description": "files backup storage"},
    {"name": "External SSD", "category": "Storage", "price": 5000,
     "description": "fast storage programming"},
    {"name": "Wireless Mouse", "category": "Accessories", "price": 800,
     "description": "computer office"},
    {"name": "Mechanical Keyboard", "category": "Accessories",
     "price": 2500, "description": "typing programming gaming"},
    {"name": "Monitor", "category": "Accessories", "price": 12000,
     "description": "display office coding"},
    {"name": "Webcam", "category": "Accessories", "price": 2200,
     "description": "video meetings online classes"},
    {"name": "Tablet", "category": "Mobile", "price": 18000,
     "description": "reading notes study"},
     {"name": "Acer Laptop", "category": "Laptop", "price": 42000,
     "description": "programming coding students"}
]


def recommend_products(category, budget, purpose):
    results = []
    keywords = set(purpose.lower().split())

    for product in products:
        if product["price"] > budget:
            continue

        if category.lower() != "any":
            if product["category"].lower() != category.lower():
                continue

        description_words = set(
            product["description"].lower().split()
        )
        name_words = set(product["name"].lower().split())
        matches = keywords & (description_words | name_words)
        score = len(matches)

        results.append((score, product, matches))

    results.sort(key=lambda item: (-item[0], item[1]["price"]))
    return results[:3]


def main():
    print("\nAI-POWERED PRODUCT RECOMMENDATION SYSTEM")
    print("----------------------------------------")
    print("Categories: Laptop, Mobile, Audio, Storage, Accessories, Any")

    category = input("Enter product category: ").strip() or "Any"

    try:
        budget = float(input("Enter maximum budget (Rs.): "))
        if budget < 0:
            print("Budget cannot be negative.")
            return
    except ValueError:
        print("Please enter a valid numeric budget.")
        return

    purpose = input("Enter intended use: ").strip()

    if not purpose:
        print("Please enter your intended use.")
        return

    recommendations = recommend_products(category, budget, purpose)

    print("\nTOP 3 RECOMMENDED PRODUCTS")
    print("==========================")

    if not recommendations:
        print("No matching products found. Try another budget or category.")
        return

    for rank, (score, product, matches) in enumerate(
        recommendations, start=1
    ):
        print(f"\n{rank}. {product['name']}")
        print("Category:", product["category"])
        print("Price: Rs.", product["price"])
        print("Description:", product["description"])

        if matches:
            print("Reason: Matches your interests in",
                  ", ".join(sorted(matches)))
        else:
            print("Reason: Matches your category and budget.")

        print("Relevance score:", score)


if __name__ == "__main__":
    main()
