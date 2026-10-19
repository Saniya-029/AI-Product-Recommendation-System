
import streamlit as st

st.set_page_config(
    page_title="Product Recommendation System",
    page_icon="🛍️"
)

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
     "description": "reading notes study"}
]


def recommend(category, budget, purpose):
    keywords = set(purpose.lower().split())
    results = []

    for product in products:
        if product["price"] > budget:
            continue

        if category != "Any" and product["category"] != category:
            continue

        words = set(
            (product["name"] + " " + product["description"]).lower().split()
        )
        matches = keywords & words
        results.append((len(matches), product, matches))

    results.sort(key=lambda x: (-x[0], x[1]["price"]))
    return results[:3]


st.title("🛍️ AI-Powered Product Recommendation System")
st.write("Find products that match your category, budget, and intended use.")

category = st.selectbox(
    "Select product category",
    ["Any", "Laptop", "Mobile", "Audio", "Storage", "Accessories"]
)

budget = st.number_input(
    "Maximum budget (₹)",
    min_value=0,
    value=50000,
    step=1000
)

purpose = st.text_input(
    "Intended use",
    placeholder="e.g. programming coding students"
)

if st.button("Recommend Products"):
    if not purpose.strip():
        st.warning("Please enter your intended use.")
    elif budget <= 0:
        st.warning("Please enter a budget greater than zero.")
    else:
        recommendations = recommend(category, budget, purpose)

        if not recommendations:
            st.info("No matching products found. Try changing your budget or category.")
        else:
            st.subheader("Top 3 Recommendations")

            for rank, (score, product, matches) in enumerate(
                recommendations, start=1
            ):
                st.markdown(f"### {rank}. {product['name']}")
                st.write("**Category:**", product["category"])
                st.write("**Price:** ₹", f"{product['price']:,}")
                st.write("**Description:**", product["description"])

                if matches:
                    st.write(
                        "**Reason:** Matches your interests in "
                        + ", ".join(sorted(matches))
                    )
                else:
                    st.write("**Reason:** Matches your category and budget.")

                st.write("**Keyword relevance score:**", score)
                st.divider()

st.caption("Educational project using category, budget, and keyword matching.")
